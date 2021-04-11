


with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    result_dict = {}
    line = f.readline().strip()
    while line:
        data = line.split()
        if result_dict.get(0):
            result_dict[data[0]] += 1
        else:
            result_dict[data[0]] = 1

        line = f.readline().strip()

print(max(result_dict, key=result_dict.get))
