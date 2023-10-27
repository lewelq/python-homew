'''Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
Для дочерних объектов указывайте родительскую директорию.
Для каждого объекта укажите файл это или директория.
Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом 
всех вложенных файлов и директорий.'''

import csv
import json
import pickle
import os
'''
def clear_files():
    # Очистка файла json
    with open("dz8/abc.json", 'w') as json_clear: 
        json.dump({}, json_clear)

    # Очистка файла csv
    with open('dz8/abc.csv', 'w') as csv_clear:
        pass

    # Очистка файла pickle
    with open('dz8/abc.pickle', 'wb') as pickle_clear:
        pass
'''

def rec(direct, parent_dir = ''):
    #clear_files()
    file_attributes = [] #список атрибутов файла (род.директория, тип, размер)
    
    for file in os.listdir(direct):
        file_attributes.clear()
        parent_dir = direct
        dir_path = os.path.join(direct, file)

        #запись атрибутов файла в список
        file_attributes.append(parent_dir) #род. директория

        if os.path.isdir(dir_path): #если директория
            file_attributes.append("directory")

            size = directory_size(dir_path) #определение размера директории
            file_attributes.append(size) #размер директории

            rec(dir_path, dir_path) #рекурсивный вызов для вложенной директории
        else: #если файл
            file_attributes.append("file")
    
            file_attributes.append(os.path.getsize(dir_path)) #размер (байт)

        file_name = os.path.basename(dir_path) #возврат имени файла

        #формирование словаря {имя:атрибуты}
        files_dict = {file_name: file_attributes}

        # json
        with open("dz8/abc.json", 'a') as doc:
            json.dump(files_dict, doc, indent=4)
            doc.write('\n')
            
        #csv
        with open("dz8/abc.csv", 'a', newline='', encoding='utf-8') as table:
            writer = csv.writer(table)
            writer.writerow(files_dict)

        #pickle
        with open('dz8/abc.pickle', 'ab') as p:
            pickle.dump(files_dict, p)

def directory_size(directory):
    total_size = 0
    for path, names, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(path, file)
            total_size += os.path.getsize(file_path)
    return total_size

rec('dz8/rand')




'''
def rec(direct):

    #очистка
    #with open("dz8/abc.json", 'w') as json_clear: 
       # json.dump({}, json_clear)
    #with open('dz8/abc.csv', 'w') as csv_clear:
       # pass
   # with open('dz8/abc.pickle', 'wb') as pickle_clear:
      #  pass

    files_check = os.listdir(direct)
    file_atributes = [] #список атрибутов файла (род.директория, тип, размер)
    dict_2 = {}
    #for root, dirs, files in os.walk(direct):
    for file in files_check:
        file_atributes.clear()
        dir_path = os.path.join(direct, file)

            #запись атрибутов файла в список
        file_atributes.append(os.path.dirname(dir_path)) #род. директория

        if os.path.isdir(dir_path): #тип
            file_atributes.append("direction")
            v = os.listdir(dir_path)
            print(v)
            x = 0
            for i in v:
                if os.path.isfile(os.path.join(dir_path, i)):
                    x += (os.path.getsize(os.path.join(dir_path, i)))
                else:
                    rec(os.path.join(dir_path, i)) #если папка: на уровень выше
            file_atributes.append(x)
        else:
            file_atributes.append("file")

        file_atributes.append(os.path.getsize(dir_path)) #размер (байт)
        file_name = os.path.basename(dir_path) #возврат имени файла

        #формирование словаря {имя:атрибуты}
        files_dict = {file_name:file_atributes}

        # json
        with open("dz8/abc.json", 'a') as doc:
            json.dump(files_dict, doc, indent=4)
            
        #csv
        with open("dz8/abc.csv", 'a', newline='', encoding='utf-8') as table:
            writer = csv.writer(table)
            writer.writerow(files_dict)

        #pickle
        with open('dz8/abc.pickle', 'ab') as p:
            pickle.dump(files_dict, p)

        #file_atributes.clear() #отчистка списка перед следующим запуском цикла

rec('dz8/rand')
'''