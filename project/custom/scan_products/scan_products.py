#!/usr/bin/python3
# -*- coding: utf-8 -*-

from grab import Grab
import sys
import os
import time
import re

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
    grab.setup(timeout=timeout, connect_timeout=connect_timeout, user_agent_file=user_agent_file, method=method, log_dir=log_dir, charset=charset, reuse_cookies=reuse_cookies, cookiefile=cookiefile)
    return grab

def parse_gen(grab, url):
    for i in range(1,57):
        grab.go(url + str(i))
        elements  = grab.xpath_list(".//li[@class='cpl-item js-catalogue-item clearfix']")
        temp = [ [i for i in elem.text_content().split('\n') if i != ''] for elem in elements]
        result = []
        for prod in temp:
            data = {"cost": prod[1], "name": prod[3], "description": prod[-1]}
            result.append(data)
        yield result


def execute_command():
    try:
        print('Run shell script')
        url = "http://avtoservis-zholnin.blizko.ru/tovary/?page="
        grab = config_query(Grab())
        result = []
        for item in parse_gen(grab, url):
            result.append(item)
            time.sleep(3)

        with open(r"./sys/res.txt", 'w') as file:
            print(result, file=file)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    execute_command()
