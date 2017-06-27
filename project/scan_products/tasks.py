from celery.task import Task
from celery.registry import tasks
from grab import Grab
import time
from services import models
import re
from django.core.exceptions import ObjectDoesNotExist


class GrabTask(Task):
    @staticmethod
    def config_query(grab):
        timeout = 15 # integer
        connect_timeout = 10 # integer
        user_agent_file = "./custom/scan_products/sys/user_agents.txt" # string
        method = "GET" # string
        post = None # sequence or dict or string
        multipart_post = None # sequence or dict
        headers = None #dict
        reuse_cookies = True # bool
        cookies = None # dict
        cookiefile = "./custom/scan_products/sys/cookie.json" # string
        referer = "http://avtoservis-zholnin.blizko.ru/tovary" # string
        reuse_referer = True # bool
        proxy = None # server:port string
        proxy_userpwd = None # username:password string
        proxy_type = None # “http”, “socks4” и “socks5” string
        encoding = "gzip" # string
        charset = "utf-8" # string
        log_file = "./custom/scan_products/sys/log.txt" # string
        log_dir = "./custom/scan_products/log_dir" # string
        follow_refresh = False # bool
        follow_location = True # bool
        nobody = False # bool
        body_maxsize = None # integer
        debug_post = False # bool
        hammer_mode = False # bool
        hammer_timeouts =   ((2, 5), (5, 10), (10, 20), (15, 30)) # list or tuple
        userpwd = None # username:password string
        lowercased_tree = False # bool
        strip_null_bytes = True # bool
        strip_xml_declaration = True # bool

        grab.setup()
        return grab

    def run(self):
        try:
            print('Run shell script')
            url = "http://avtoservis-zholnin.blizko.ru/tovary/"
            prefix = "/?page="
            reg_cars = {"ГАЗ": re.compile(r"ГАЗ"), "Джипы": re.compile(r"Джип", re.I), "ВАЗ": re.compile(r"ВАЗ"), "УАЗ": re.compile(r"УАЗ")}
            reg = re.compile(r"\([^\(\)]+\)$")

            grab = Grab()
            grab.go(url)
            links = grab.doc.select(".//a[@class='prl-title js-prl-count']")
            data = [(link.attr("href"), int(link.attr("data-count")), link.text()) for link in links]
            if data:
                print("Начало")
                for href,count,text in data:
                    try:
                        service_type = models.ServiceType.objects.get(type_name=text)
                    except ObjectDoesNotExist:
                        service_type = models.ServiceType.objects.create(type_name=text)
                        print("Создана запись в таблице ServiceType")
                    count_page = count // 20 + 1 if  count % 20 > 0 else count // 20
                    count = 1
                    for i in range(1, count_page + 1):
                        number_try = 3
                        current_try = 1
                        elements_text = None
                        while current_try <= number_try:
                            time.sleep(5)
                            print("Получение страницы")
                            grab.go(href + prefix + str(i))
                            print("Получение тегов")
                            elements = grab.doc.select(".//li[@class='cpl-item js-catalogue-item clearfix']")
                            if elements.__class__.__name__ == 'SelectorList':
                                elements_text  = [[ i for i in  elem.split("\n") if i != ''] for elem in  [ j.node().text_content() for j in elements]]
                                break
                            else:
                                print("Ошибка!!! попытка номер %d"%(current_try))
                                current_try += 1
                        print("Парсинг текста")

                        if elements_text:
                                for prod in elements_text:
                                    service_entry = models.Service.objects.create(service_cost=prod[1], service_name=re.sub(r"\([^\(\)]+\)$", "", prod[3]),service_description=prod[-1], service_type=service_type)
                                    if re.search(reg, prod[3]):
                                        cars = []
                                        if text == "Антикоррозионная обработка":
                                            if models.Service.objects.filter(service_name=re.sub(r"\(.+\)", "", prod[3])).count() == 0:
                                                material_name = "BODY"
                                            else:
                                                material_name = "ТАНТАЛ"

                                            service_entry.material_used = models.MaterialUsed.objects.get(material_name=material_name)
                                            service_entry.save()

                                            if not re.findall(r"\d+", prod[3]):
                                                cars.append(re.search(reg, prod[3]).group()[1:-1])
                                            flag = True
                                        else:
                                            for entry in re.search(reg, prod[3]).group()[1:-1].split(','):
                                                cars.append(entry.strip())
                                            flag = False
                                        for car in cars:
                                            if flag:
                                                car_type = car
                                            else:
                                                car_type = car.split(" ")[-1]
                                                for key in reg_cars:
                                                    if re.search(reg_cars[key], car):
                                                        car_type = key
                                            try:
                                                car_entry = models.ServicedCar.objects.get(car_type=car_type)
                                            except ObjectDoesNotExist:
                                                car_entry = models.ServicedCar.objects.create(car_type=car_type)
                                                print("Создана запись в таблице ServicedCar")
                                            finally:
                                                service_entry.serviced_cars.add(car_entry)
                        else:
                            print("Ошибка! Не удалось получить текстовое содержимое тегов")
                            print("Колличество проходов=%d"%(count))
                            break
                        print("Колличество проходов=%d"%(count))
                        count += 1
            else:
                print("Ошибка!!! Не удалось получить ссылки")

        except Exception as e:
            print(e)
            with open(r"./custom/scan_products/log_dir/log.txt", 'w') as file:
                print(e, file=file)
        print("Конец")



tasks.register(GrabTask)



