# -*- coding: utf-8 -*-
##  POMOgalki  ##

# cd "venv\Scripts"
# venv\Scripts.\pip.exe install requests, bs4, pandas, openpyxl, selenium, simplejson, jmespath, xmltodict, json2xml, icecream



import sys
import traceback

# import json
import xmltodict
from json2xml import json2xml
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import re
import zlib
import jmespath
from icecream import ic
ic.configureOutput(includeContext=True)
import datetime

print = ic

try:
    import simplejson as json
except ImportError:
    import json

try:
    import selenium
    from selenium import webdriver
except:
    pass

import  time
import datetime
from pprint import pprint
import base64
import threading
from concurrent.futures import ThreadPoolExecutor

def bss(url):
    return bs(url, 'html.parser')

def read_f(file_name, encod='utf8'):
    with open(file_name, 'r', encoding=encod) as f:
        F = f.read()
        return F

def write_f(data, file_name, type='w', encod='utf8'):
    with open(file_name, type, encoding=encod) as f:
        f.write(data)


def read_j(file_name, encod='utf8'):
    with open(file_name, 'r', encoding=encod) as f:
        F = json.load(f)
        return F


def write_j(data, file_name, type='w', indent=4, ensure_ascii=False, encod='utf8'):
    with open(file_name, type, encoding=encod) as f:
        json.dump(data, f, indent=indent, ensure_ascii=ensure_ascii)


def repetitive(list, Return='not_repetitive'):
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

    if Return == 'not_repetitive':
        return not_repetitive
    if Return == 'repetitive':
        return repetitive

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



# Divides the list or str
def divider_list(list_or_str, lenOfElement, lenOfResultlist=None):
    if lenOfElement != None and lenOfResultlist != None:
        print('Choose lenOfElement or lenOfResultlist')
        1/0
    if lenOfResultlist != None:
        lenOfElement = round(len(list_or_str)/lenOfResultlist)+1
        print(lenOfElement)
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
    if type(list_or_str) == str:
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
    return sum



def url_to_b64(link_to_file, file_name=None):
    # скачивает файл по ссылке и записывает его в виде base64
    fileB64 = base64.b64encode(requests.get(link_to_file).content).decode('utf8')
    if file_name == None:
        return fileB64
    else:
        write_f(fileB64, file_name)


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

# xml_to_json('www-FLUKE.xml', 'fluke.json')


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

# json_to_xml('fluke.json', 'fluke.xml')


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

    def list_divider(list_or_file, amount_of_one, exported_file_name=True):
        import os
        # Принимает список или файл,
        # если файл по умолчанию сохранит копии если exported_file_name=True
        # если список сохранит если exported_file_name задать имя файла (директорию и имя файла)

        if type(list_or_file) == str:
            if exported_file_name == True:
                exported_file_name, f_ext = os.path.splitext(list_or_file)
                exported_file_name = os.path.basename(exported_file_name)
            else:
                pass
            print(exported_file_name)
            list_or_file = read_j(list_or_file)

        def adding(List, amount_of_one):
            C = 0
            c = 0
            L = []
            l = []
            for q in List:
                if c == 0:
                    L.append([])
                if c < amount_of_one:
                    L[C].append(q)
                    c += 1
                else:
                    c = 0
                    C += 1
            return L

        divided_list = adding(list_or_file, amount_of_one)

        if type(exported_file_name) != bool:

            c = 1
            for e in divided_list:
                name_of_file = exported_file_name + '(' + str(c) + ')' + '.json'
                write_j(e, name_of_file)
                c += 1
        return divided_list



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

