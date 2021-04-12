# Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#    |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
#
#
# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
# (они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача, которая решена, например, во фреймворке django.

import os

def create_file(path, dir_name, file_name):
    file_path = os.path.join(path, "templates", dir_name)
    if not os.path.isdir(file_path):
        os.makedirs(file_path)
    file = os.path.join(file_path, file_name)
    with open('file', 'w', encoding='utf-8') as f:
        print(f'{file} created')

path = r'C:\Users\Артур\PycharmProjects\Geek_brain\homeworks\lesson_7\task_2\my_project'
for root, dirs, files in os.walk(path):
    for file in files:
        if file.split('.')[-1] == 'html':
            folder_name = os.path.split(root)[-1]
            create_file(path, folder_name, file)