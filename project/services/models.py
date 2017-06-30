from django.db import models
from project.settings.base import PROJECT_ROOT
from os import path

# Create your models here.

class MaterialUsed(models.Model):
    class  Meta:
        app_label = 'services'
        db_table = 'MaterialUsed'
        verbose_name='Используемый материал'
        verbose_name_plural = 'Используемые материалы'
    material_name = models.CharField(null=False, blank=False, max_length=500,  verbose_name="Название материала")
    material_description = models.TextField(null=True, blank=True, verbose_name="Описание")
    is_active = models.BooleanField(default=True, verbose_name="Активность")

    def __str__(self):
        return self.material_name

class ServicedCar(models.Model):
    class Meta:
        app_label = 'services'
        db_table = 'ServicedCar'
        verbose_name='Обслуживаемый автомобиль '
        verbose_name_plural = 'Обслуживаемые автомобили'
    car_type = models.CharField(null=False, blank=False, max_length=500,  verbose_name="Тип автомобиля", default="Тип авто", unique=True)
    is_active = models.BooleanField(default=True, verbose_name="Активность")

    def __str__(self):
        return self.car_type

class ServiceType(models.Model):
    class Meta:
        app_label = 'services'
        db_table = 'ServiceType'
        verbose_name='Тип услуги'
        verbose_name_plural = 'Типы услуг'
    type_name = models.CharField(null=False, blank=False, max_length=500, unique=True, verbose_name="Название", default="Тип услуги")
    serviced_cars = models.ManyToManyField(ServicedCar,verbose_name="Обслуживаемые авто", blank=True, null=True)
    image = models.CharField(null=True, blank=True, max_length=100, verbose_name="Название картинки", default="image_07.img")
    is_active = models.BooleanField(default=True, verbose_name="Активность")

    def __str__(self):
        return self.type_name

class Service(models.Model):
    class Meta:
        app_label = 'services'
        db_table = 'Service'
        verbose_name='Услуга'
        verbose_name_plural = 'Услуги'
    service_name = models.CharField(null=False, blank=False, max_length=500,  verbose_name="Название", default="Наименование услуга")
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE, verbose_name="Тип услуги", blank=True, null=True)
    material_used = models.ForeignKey(MaterialUsed, verbose_name="Используемый материал", blank=True, null=True)
    serviced_cars = models.ManyToManyField(ServicedCar, verbose_name="Тип автомобиля", blank=True, null=True)
    service_cost = models.CharField(null=False, blank=False, max_length=100,  verbose_name="Стоимость", default="Договрная")
    service_description = models.TextField(null=True, blank=True, verbose_name="Описание")
    is_active = models.BooleanField(default=True, verbose_name="Активность")

    def __str__(self):
        return self.service_name

