import os, time

directory = '.'
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        parent_dir = os.path.dirname(filepath)
        f_size = os.stat(filepath).st_size
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {f_size} байт, '
              f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
