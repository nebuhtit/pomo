# -*- coding: utf-8 -*-
##  POMOgalki  ##

# cd "venv\Scripts"
# venv\Scripts.\pip.exe install requests, bs4, pandas, openpyxl, selenium


import json
import sys
import traceback

import current as current
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import selenium
from selenium import webdriver
import  time
import datetime
from pprint import pprint
import base64
import threading


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


def clean_up_repetitive(list, Return='not_repetitive'):
    repetitive = []
    not_repetitive = []
    for q in list:
        if q not in not_repetitive:
            not_repetitive.append(q)
        else:
            repetitive.append(q)

    if Return == 'not_repetitive':
        return not_repetitive
    if Return == 'repetitive':
        return repetitive


def url_to_b64(link_to_file, file_name=None):
    # скачивает файл по ссылке и записывает его в виде base64
    fileB64 = base64.b64encode(requests.get(link_to_file).content).decode('utf8')
    if file_name == None:
        return fileB64
    else:
        write_f(fileB64, file_name)


arts = read_f('arti.txt').split('\n')


def func(art):
    link = 'https://datasheet.eaton.com/datasheet.php?model='+art+'&locale=ru_RU'
    page = requests.get(link).content
    title_ = bs(page, features='html.parser').find('div', class_='ds-header-content-product-description').text
    return title_


def threads(func, List):
    import os
    if not os.path.exists('pomo_timely_files'):
        os.mkdir('pomo_timely_files')


    delitel = round(len(List) / 20)

    count = 1
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = []
    list7 = []
    list8 = []
    list9 = []
    list10 = []
    list11 = []
    list12 = []
    list13 = []
    list14 = []
    list15 = []
    list16 = []
    list17 = []
    list18 = []
    list19 = []
    list20 = []
    # print(List)

    for q in List:
        if count <= delitel:
            list1.append(q)
        # print(list1)

        if (2 * delitel) >= count > delitel:
            list2.append(q)
        # print(list2)

        if (3 * delitel) >= count > (2 * delitel):
            list3.append(q)
        # print(list3)

        if (4 * delitel) >= count > (3 * delitel):
            list4.append(q)
        # print(list4)

        if (5 * delitel) >= count > (4 * delitel):
            list5.append(q)
        # print(list5)

        if (6 * delitel) >= count > (5 * delitel):
            list6.append(q)
        # print(list6)

        if (7 * delitel) >= count > (6 * delitel):
            list7.append(q)
        # print(list7)

        if (8 * delitel) >= count > (7 * delitel):
            list8.append(q)
        # print(list8)

        if (9 * delitel) >= count > (8 * delitel):
            list9.append(q)
        # print(list9)

        if (10 * delitel) >= count > (9 * delitel):
            list10.append(q)
        # print(list10)

        if (11 * delitel) >= count > (10 * delitel):
            list11.append(q)
        # print(list11)

        if (12 * delitel) >= count > (11 * delitel):
            list12.append(q)
        # print(list12)

        if (13 * delitel) >= count > (12 * delitel):
            list13.append(q)
            # print(list13)

        if (14 * delitel) >= count > (13 * delitel):
            list14.append(q)
            # print(list14)

        if (15 * delitel) >= count > (14 * delitel):
            list15.append(q)
            # print(list15)

        if (16 * delitel) >= count > (15 * delitel):
            list16.append(q)
            # print(list16)

        if (17 * delitel) >= count > (16 * delitel):
            list17.append(q)
            # print(list17)

        if (18 * delitel) >= count > (17 * delitel):
            list18.append(q)
            # print(list18)

        if (19 * delitel) >= count > (18 * delitel):
            list19.append(q)
            # print(list19)

        if count > (19 * delitel):
            list20.append(q)
            # print(list20)

        count += 1

    def forOneList(OneList, NumberFile):
        time_old = time.time()
        l = []
        for q in OneList:
            res = func(q)
            l.append(res)
        write_j(l, 'pomo_timely_files/file'+str(NumberFile)+'.json')
        current_time = time.time() - time_old
        print( current_time)

    listOfItems1 = threading.Thread(target=forOneList, args=(list1, 1,))
    listOfItems2 = threading.Thread(target=forOneList, args=(list2, 2,))
    listOfItems3 = threading.Thread(target=forOneList, args=(list3, 3,))
    listOfItems4 = threading.Thread(target=forOneList, args=(list4, 4,))
    listOfItems5 = threading.Thread(target=forOneList, args=(list5, 5,))
    listOfItems6 = threading.Thread(target=forOneList, args=(list6, 6,))
    listOfItems7 = threading.Thread(target=forOneList, args=(list7, 7,))
    listOfItems8 = threading.Thread(target=forOneList, args=(list8, 8,))
    listOfItems9 = threading.Thread(target=forOneList, args=(list9, 9,))
    listOfItems10 = threading.Thread(target=forOneList, args=(list10, 10,))
    listOfItems11 = threading.Thread(target=forOneList, args=(list11, 11,))
    listOfItems12 = threading.Thread(target=forOneList, args=(list12, 12,))
    listOfItems13 = threading.Thread(target=forOneList, args=(list13, 13,))
    listOfItems14 = threading.Thread(target=forOneList, args=(list14, 14,))
    listOfItems15 = threading.Thread(target=forOneList, args=(list15, 15,))
    listOfItems16 = threading.Thread(target=forOneList, args=(list16, 16,))
    listOfItems17 = threading.Thread(target=forOneList, args=(list17, 17,))
    listOfItems18 = threading.Thread(target=forOneList, args=(list18, 18,))
    listOfItems19 = threading.Thread(target=forOneList, args=(list19, 19,))
    listOfItems20 = threading.Thread(target=forOneList, args=(list20, 20,))
    listOfItems1.start()
    listOfItems2.start()
    listOfItems3.start()
    listOfItems4.start()
    listOfItems5.start()
    listOfItems6.start()
    listOfItems7.start()
    listOfItems8.start()
    listOfItems9.start()
    listOfItems10.start()
    listOfItems11.start()
    listOfItems12.start()
    listOfItems13.start()
    listOfItems14.start()
    listOfItems15.start()
    listOfItems16.start()
    listOfItems17.start()
    listOfItems18.start()
    listOfItems19.start()
    listOfItems20.start()

    listOfItems1.join()
    listOfItems2.join()
    listOfItems3.join()
    listOfItems4.join()
    listOfItems5.join()
    listOfItems6.join()
    listOfItems7.join()
    listOfItems8.join()
    listOfItems9.join()
    listOfItems10.join()
    listOfItems11.join()
    listOfItems12.join()
    listOfItems13.join()
    listOfItems14.join()
    listOfItems15.join()
    listOfItems16.join()
    listOfItems17.join()
    listOfItems18.join()
    listOfItems19.join()
    listOfItems20.join()

    lis1 = read_j('pomo_timely_files/file1.json')
    lis2 = read_j('pomo_timely_files/file2.json')
    lis3 = read_j('pomo_timely_files/file3.json')
    lis4 = read_j('pomo_timely_files/file4.json')
    lis5 = read_j('pomo_timely_files/file5.json')
    lis6 = read_j('pomo_timely_files/file6.json')
    lis7 = read_j('pomo_timely_files/file7.json')
    lis8 = read_j('pomo_timely_files/file8.json')
    lis9 = read_j('pomo_timely_files/file9.json')
    lis10 = read_j('pomo_timely_files/file10.json')
    lis11 = read_j('pomo_timely_files/file11.json')
    lis12 = read_j('pomo_timely_files/file12.json')
    lis13 = read_j('pomo_timely_files/file13.json')
    lis14 = read_j('pomo_timely_files/file14.json')
    lis15 = read_j('pomo_timely_files/file15.json')
    lis16 = read_j('pomo_timely_files/file16.json')
    lis17 = read_j('pomo_timely_files/file17.json')
    lis18 = read_j('pomo_timely_files/file18.json')
    lis19 = read_j('pomo_timely_files/file19.json')
    lis20 = read_j('pomo_timely_files/file20.json')


    listOfItems = lis1 + lis2 + lis3 + lis4 + lis5 + lis6 + lis7 + lis8 + lis9 + lis10 + lis11 + lis12 + lis13 + lis14 + lis15 + lis16 + lis17 + lis18 + lis19 + lis20
    return listOfItems


old = time.time()
res = threads(func, arts)
current = time.time() - old
print(len(res))
print("summ time", current)





class dicts:

    def func_for_each(list_with_dict, func, key, key2=None, key3=None, key4=None, key5=None):
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

    def remove_element(list_with_dict, key, key2=None, key3=None, key4=None, key5=None):

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

    def dicts_to_xlsx(list_with_dict, file_name):
        # CHOSE LIST WITH DICTS OR PUTH TO JSON
        if type(list_with_dict) == str:
            list_with_dict = read_j(list_with_dict)
        df = pd.DataFrame(list_with_dict).to_excel(file_name)


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



