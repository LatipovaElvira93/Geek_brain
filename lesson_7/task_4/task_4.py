import os


path = r'C:\Users\Артур\PycharmProjects\Geek_brain\homeworks\lesson_7\task_4\some_data'
result_dict = {100: 0, 1000: 0, 10000: 0, 100000: 0}
for file in os.listdir(path):
    file_path = os.path.join(path, file)
    size = os.stat(file_path).st_size
    if size < 100:
        result_dict[100] += 1
    if size < 1000:
        result_dict[1000] += 1
    if size < 10000:
        result_dict[10000] += 1
    if size < 100000:
        result_dict[100000] += 1

print(result_dict)