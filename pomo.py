# -*- coding: utf-8 -*-
##  POMOgalki  ##

# cd "venv\Scripts"
# venv\Scripts.\pip.exe install requests, bs4, pandas, openpyxl, selenium, simplejson, jmespath, xmltodict, json2xml,
# icecream, varname, qrcode, ByteSplitter
# cd venv/bin
# pip install requests, bs4, pandas, openpyxl, selenium, jmespath, xmltodict, json2xml, icecream, varname, qrcode

# NOTES:

# Find elements by part of text:
# element = d.find_elements(By.XPATH, "//*[text()[contains(.,'PART OF TEXT')]]") # https://stackoverflow.com/questions/3655549/xpath-containstext-some-string-doesnt-work-when-used-with-node-with-more


# Shows network from page on chromedriver:
# test = d.execute_script('var performance = window.performance || window.mozPerformance || window.msPerformance || window.webkitPerformance || {}; var network = performance.getEntries() || {}; return network;')



import sys
import os
import traceback

import json
import  time
import datetime
from varname import nameof
from pprint import pprint
import base64
import threading
from concurrent.futures import ThreadPoolExecutor
import varname
import xmltodict
from json2xml import json2xml
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import re
import zlib
import bysp
import shutil
import jmespath



try:
    from icecream import ic # print with number line and function
    ic.configureOutput(includeContext=True)
    print = ic
except:
    pass
try:
    import selenium
    from selenium import webdriver
    from selenium.webdriver.common.by import By
except:
    pass


# Simplification of the link fence by BeautifulSoup
def bss(url):
    return bs(url, 'html.parser')


# Making it easier to read json
def read_j(file_name, encod='utf8'):
    with open(file_name, 'r', encoding=encod) as f:
        F = json.load(f)
        return F


# Making it easier to write json
def write_j(data, file_name=None, type_='w', indent=4, ensure_ascii=False, encod='utf8'):
    if file_name == None:
        file_name = varname.nameof(data, frame=2) + '.json'

    with open(file_name, type_, encoding=encod) as f:
        json.dump(data, f, indent=indent, ensure_ascii=ensure_ascii)


# Making it easier to read file
def read_f(file_name, type_='r', encod='utf8'):
    with open(file_name, type_, encoding=encod) as f:
        F = f.read()
        return F


# Making it easier to write file
def write_f(data, file_name=None, type_='w', encod='utf8'):
    # print(data)
    if file_name == None:
        file_name = varname.nameof(data, frame=2)
        if type(data) == list or type(data) == dict:
            write_j(data, file_name+'.json')
        elif type(data) == str:
            file_name = file_name + '.txt'
            with open(file_name, type_, encoding=encod) as f:
                f.write(data)
        elif type(data) == bytes:
            with open(file_name, mode='wb', encoding=None) as f:
                f.write(data)
    else:
        with open(file_name, type_, encoding=encod) as f:
            f.write(data)


# Looks for repetitive in the list
def repetitive(list, repetitive=False):
    repetitive = []
    already = []
    not_repetitive = []
    for q in list:
        if q not in already and q not in repetitive:
            already.append(q)
            not_repetitive.append(q)
        else:
            repetitive.append(q)
            try:
                not_repetitive.remove(q)
            except ValueError: pass

    if repetitive == False:
        return not_repetitive # Выдает не повторяющиеся
    if repetitive == True:
        return repetitive # Выдает повторяющиеся


# Is there elements from one list in another list?
def is_there(needed_object_or_list, in_this_list, show_missed=True):
    # Показывает каких объектов из одного списка нет в другом. или какие там есть.
    # Если выбран один объект выдает количиство таких объектов в списке.
    if type(needed_object_or_list) != list:
        c = 0
        for object in in_this_list:
            if object == needed_object_or_list:
                c += 1
            else:
                pass
        return c # количество объектов в списке
    else:
        if show_missed == True:
            missed = []
            for object in needed_object_or_list:
                if object not in in_this_list:
                    missed.append(object)
            return missed
        if show_missed == False:
            not_missed = []
            for object in needed_object_or_list:
                if object in in_this_list:
                    not_missed.append(object)
            return not_missed


# Prints time left
def time_left(c, pro, old_time, items):
    # Вcтавить вне цикла:
    # C = 1
    # pro = 0
    # Вставить в начале цикла:
    # old_time = time.time()
    # C += 1
    left = (len(items) - c)
    finish_time = time.time()
    timer_for_one = finish_time - old_time
    time_left = (timer_for_one * left)
    time_till = time.strftime("%H:%M", time.localtime(time.time() + time_left))
    # print(timer_for_one)
    # print(left)
    if pro != round(100 - (100 / (len(items)) * (len(items) - c)), 1):
        pro = round(100 - (100 / (len(items)) * (len(items) - c)), 1)
        print(pro, '%')
        print(time_till)


# Divides the list or str
def divider_list(list_or_str, lenOfElement, lenOfResultlist=None, NameOfFolder=None):
    global path_data, makedirs, path, sum, name_data
    print("lenOfElement",lenOfElement, type(lenOfElement))
    if lenOfElement != None:
        lenOfElement = int(lenOfElement)
    if lenOfResultlist != None:
        lenOfResultlist = int(lenOfResultlist)
    if lenOfElement != None and lenOfResultlist != None:
        print('Choose lenOfElement or lenOfResultlist')
        1/0
    if lenOfResultlist != None:
        lenOfElement = round(len(list_or_str)/lenOfResultlist)+1
        print(lenOfElement)
    if type(list_or_str) == str and NameOfFolder != None:
        from os import makedirs, path
        name_data = path.splitext(path. basename(list_or_str))[0]
        path_data =path.dirname(list_or_str)
        print("name_data", name_data)
        list_or_str = read_j(list_or_str)

    if type(list_or_str) == list:
        c = 1
        little = []
        sum = []
        for q in list_or_str:
            if c < lenOfElement:
                c += 1
                little.append(q)
            if c == lenOfElement:
                c = 1
                little.append(q)
                sum.append(little)
                little = []
        if little != []:
            sum.append(little)
    if type(list_or_str) == str and NameOfFolder == None:
        lenOfElement = lenOfElement + 1
        c = 1
        little = ''
        sum = []
        for q in list_or_str:
            if c < lenOfElement:
                c += 1
                little = little + q
            if c == lenOfElement:
                c = 1
                # little = little + q
                sum.append(little)
                little = ''
        if little != '':
            sum.append(little)
    if NameOfFolder != None:

        if NameOfFolder == True:
            NameOfFolder = name_data+ '_divided'
            if not path.exists(path_data+'/'+NameOfFolder):
                makedirs(path_data+'/'+NameOfFolder)
        else:
            if not path.exists(NameOfFolder):
                makedirs(path_data+'/'+NameOfFolder)
        n_fold = 1
        for part in sum:
            write_j(part, path_data+'/'+NameOfFolder + '/' + name_data + str(n_fold) + '.json')
            n_fold += 1

    return sum


# Downloads the file from the link and writes it as base64
def url_to_b64(link_to_file, file_name=None):
    # скачивает файл по ссылке и записывает его в виде base64
    fileB64 = base64.b64encode(requests.get(link_to_file).content).decode('utf8')
    if file_name == None:
        return fileB64
    else:
        write_f(fileB64, file_name)


# Experementally. Don't use. Just for example.
def save_results(List_of_arts):
    # не тестил. Должна сохранять результаты хороших и ошибок.
    import os
    if not os.path.exists('pomo_timely_files'):
        os.mkdir('pomo_timely_files')

    write_j([], 'pomo_timely_files/error.json')
    write_j([], 'pomo_timely_files/save.json')
    write_j([], 'pomo_timely_files/save1.json')

    already_error = read_j('pomo_timely_files/error.json')

    for q in already_error:
        List_of_arts.append(q)

    downloaded = []
    already_downloaded = read_j('pomo_timely_files/save.json')
    for e in already_downloaded:
        downloaded.append(list(e.keys())[0])

    already_downloaded_1 = read_j('pomo_timely_files/save1.json')
    for r in already_downloaded_1:
        downloaded.append(list(r.keys())[0])

    save = already_downloaded
    # print(norm)
    save1 = already_downloaded_1
    # print(morethan6)
    error = []

    def save(one_dict):
        # key of one dict shoot be article
        save.append(one_dict)
        write_j(data=save, file_name='pomo_timely_files/save.json')

    def save1(one_dict):
        save1.append(one_dict)
        write_j(data=save1, file_name='pomo_timely_files/save1.json')


# Xml to json
def xml_to_json(xml_file_or_path, file_json=None):
    if type(xml_file_or_path) == str:
        f = read_f(xml_file_or_path)
    else:
        f = xml_file_or_path
        xml_file_or_path = None

    j = xmltodict.parse(f)
    if file_json != None:
        write_j(data=j, file_name=file_json)
    return j


# Json_to_xml
def json_to_xml(dict_or_json, name_xml=None, replHTMLsymb=True):
    if type(dict_or_json) == str:
        d = read_j(dict_or_json)
    else:
        d = dict_or_json
        dict_or_json = None
    x = json2xml.Json2xml(d).to_xml()
    if replHTMLsymb == True:
        if '&quot;' in x:
            x = re.sub('&quot;', '"', x)

        if '&apos;' in x:
            x = re.sub('&apos;', "'", x)

        if '&lt;' in x:
            x = re.sub('&lt;', '<', x)

        if '&gt;' in x:
            x = re.sub('&gt;', '>', x)

        if '&amp;' in x:
            x = re.sub('&amp;', '&', x)

    if name_xml != None:
        write_f(x, name_xml)
    return x


# Executes a passed-in function in multi-threaded mode. The number of threads is regulated.
def threads(func, List, max_workers=20, file_name=None):
    # Выполняет переданную внутрь функцию в много поточном режиме. Регулируется кол-во потоков.
    # Пока что проблемы с глобальными переменными вне этой функции.
    futures = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:

        for i in List:
            futures.append(executor.submit(func, i))

        # ждем, когда закончат выполняться задачи

        list_res = []
        for future in futures:
            list_res.append(future.result())

            if file_name != None:
                write_j(data=list_res, file_name=file_name)


    return(list_res)


# Reduces the weight of the stock if it is rational. Returns base64 text by default
def rationally_compress(text, b64=True):
    # Уменьшает вес стоки если это рационально. По умолчанию возвращает текст base64
    text1 = text.encode('utf-8')
    print(text1, len(text1))
    text_compressed = zlib.compress(text.encode('utf-8'))
    print(text_compressed, len(text_compressed))
    if len(text_compressed) >= len(text1):
        if b64 == True:
            text_b64 = base64.b64encode(text1).decode('utf-8')
            return text_b64
        else:
            return text1
    else:
        if b64 == True:
            # print(text_compressed, type(text_compressed))
            text_b64 = base64.b64encode(text_compressed).decode('utf-8')
            return text_b64
        else:
            return text_compressed


# Recovers compressed text
def rationally_DEcompress(text_or_bytes):
    # Восстанавливает сжатый текст
    if type(text_or_bytes) == str:
        try:
            decompresed = zlib.decompress(base64.b64decode(text_or_bytes)).decode('utf-8')
            return decompresed
        except:
            de_b64 = base64.b64decode(text_or_bytes).decode('utf-8')
            return de_b64
    else:
        try:
            decompresed = zlib.decompress(text_or_bytes).decode('utf-8')
            return decompresed
        except:
            de_b64 = text_or_bytes.decode('utf-8')
            return de_b64
        
# Деление файлов

# Чтобы восстановить нужно прописать имя вайла без
#
# расширения "№.part" на конце, иначе будет ошибка


### Split file
# parts = bysp.split_file()

### Restore file
# bysp.combine_file()


def split_files_in_folder(folder_path, split_count=10, save=True, dest_folder=None):
    # folder_path_ = os.path.join(folder_path)
    for item in os.listdir(folder_path):
        full_path = os.path.join(folder_path, item)
        print(folder_path)
        nameofile = os.path.basename(full_path)
        print(nameofile)
        newfolder = os.path.join(dest_folder, nameofile)
        print(newfolder)
        if nameofile == 'temp':
            pass
        else:
            if os.path.isdir(newfolder):
                pass
            else:
                os.mkdir(newfolder)
            bysp.split_file(full_path, split_count=split_count, save=save, destination=newfolder)


# Operations for dictation. Mostly specialized for my tasks.
class dicts:
    # Операции для диктов. Преимущественно специализированы под мои задачи.
    def func_for_each_value(list_with_dict, func, key, key2=None, key3=None, key4=None, key5=None):
        new_list = []
        # Применняет функцию к каждому значению елемента списка найденному по заданным ключам

        if key != None and key2 == None and key3 == None and key4 == None and key5 == None:
            for element in list_with_dict:
                element[key] = func(element[key])
                new_list.append(element)

        if key != None and key2 != None and key3 == None and key4 == None and key5 == None:
            for element in list_with_dict:
                element[key][key2] = func(element[key][key2])
                new_list.append(element)

        if key != None and key2 != None and key3 != None and key4 == None and key5 == None:
            for element in list_with_dict:
                element[key][key2][key3] = func(element[key][key2][key3])
                new_list.append(element)

        if key != None and key2 != None and key3 != None and key4 != None and key5 == None:
            for element in list_with_dict:
                element[key][key2][key3][key4] = func(element[key][key2][key3][key4])
                new_list.append(element)

        if key != None and key2 != None and key3 != None and key4 != None and key5 != None:
            for element in list_with_dict:
                element[key][key2][key3][key4][key5] = func(element[key][key2][key3][key4][key5])
                new_list.append(element)

        return new_list

    def remove_element_in_each(list_with_dict, key, key2=None, key3=None, key4=None, key5=None):

        # Удаляет необходимый ключ и его значение в каждом элементе списка. Находит по задонному пути из ключей

        if key != None and key2 == None and key3 == None and key4 == None and key5 == None:
            for element in list_with_dict:
                element.pop(key)

        if key != None and key2 != None and key3 == None and key4 == None and key5 == None:
            for element in list_with_dict:
                element[key].pop(key2)

        if key != None and key2 != None and key3 != None and key4 == None and key5 == None:
            for element in list_with_dict:
                element[key][key2].pop(key3)

        if key != None and key2 != None and key3 != None and key4 != None and key5 == None:
            for element in list_with_dict:
                element[key][key2][key3].pop(key4)

        if key != None and key2 != None and key3 != None and key4 != None and key5 != None:
            for element in list_with_dict:
                element[key][key2][key3][key4].pop(key5)

        return list_with_dict

    def func_for_each_key(list_with_dict, func):
        l = []
        for element in list_with_dict:
            new_element = {func(list(element.keys())[0]): list(element.values())[0]}
            l.append(new_element)
        return l

    def dict_to_xlsx(dict_or_json_with_dict, file_name, join_by=None):
        if type(dict_or_json_with_dict) == str:
            j = read_j(dict_or_json_with_dict)
        else:
            j = dict_or_json_with_dict
        keys = list(j.keys())
        values = list(j.values())

        c = 0
        k = {}
        for q in keys:
            d = {c: q}
            k.update(d)
            c += 1

        c1 = 0
        v = {}
        for w in values:
            if join_by != None:
                w = join_by.join(w)
            d1 = {c1: w}
            v.update(d1)
            c1 += 1

        res = {'KEYS': k, 'VALUES': v}
        # print(res)
        pd.DataFrame(res).to_excel(file_name)

    def dicts_to_xlsx(list_with_dict, file_name, transpose=False):
        # CHOSE LIST WITH DICTS OR PUTH TO JSON
        if type(list_with_dict) == str:
            list_with_dict = read_j(list_with_dict)
        if transpose == False:
            df = pd.DataFrame(list_with_dict).to_excel(file_name)
        else:
            df = pd.DataFrame(list_with_dict).transpose().to_excel(file_name)


    def xlsx_to_dict(file_name, na_filter=False, index_col=0, transpose=True, json_name=None):
        # Works only for special files

        if transpose == True:
            try:
                Dict = pd.DataFrame(pd.read_excel(file_name, na_filter=na_filter, index_col=index_col)).transpose().to_dict()
            except:
                try:
                    Dict = pd.DataFrame(file_name, na_filter=na_filter, index_col=index_col).transpose().to_dict()
                except:
                    Dict = file_name.transpose().to_dict()
        else:
            try:
                Dict = pd.DataFrame(pd.read_excel(file_name, na_filter=na_filter, index_col=index_col)).to_dict()
            except:
                try:
                    Dict = pd.DataFrame(file_name, na_filter=na_filter, index_col=index_col).to_dict()
                except:
                    Dict = file_name.to_dict()

        l = []
        for q in Dict:
            for w in Dict[q]:
                try:
                    Dict[q][w] = eval(str(Dict[q][w]))
                except: pass
            l.append(Dict[q])
        if json_name != None:
            write_j(l, json_name)
        return l

    def dicts_to_csv(list_with_dict, file_name):
        df = pd.DataFrame(list_with_dict).to_csv(file_name)


# Testing

# import qrcode
# text = """

# """
# text = pomo.rationally_compress(text)

# img = qrcode.make(text)
# img.save('hi.png')

# print(len(text))
