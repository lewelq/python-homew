'''Напишите функцию группового переименования файлов. Она должна:
принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
принимать параметр количество цифр в порядковом номере.
принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
принимать параметр расширение конечного файла.
принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.'''

import os

def rename(name, file_ext, end_file_ext, range_start, range_end, num_count = 1):
    directory = 'dz9/rnd_dir'
    files_check = os.listdir(directory)

    for i, file in enumerate(files_check, start=1):
        if file.endswith(file_ext):
            file_name = os.path.basename(file)
            file_name_split = os.path.splitext(file_name) [0]
            file_range = file_name_split[range_start - 1:range_end - 1]
            dir_path = os.path.join(directory, file)
            numeration = str(i).zfill(num_count)
            new_path = os.path.join(directory, f'{file_range}{name}{numeration}{end_file_ext}')
            os.rename(dir_path, new_path)

name = 'abcd'
file_ext = '.txt'
end_file_ext = '.py'
num_count = 3
range_start = 3
range_end = 6

print(rename(name, file_ext, end_file_ext, range_start, range_end, num_count))
