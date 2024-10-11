import os, time

directory = '.'
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        f_size = os.stat(file).st_size
        parent_dir = os.path.abspath(os.path.join(root, os.pardir))
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {f_size} байт, '
              f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
