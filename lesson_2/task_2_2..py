

arr = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
arr_2 = []
i = 0

for item in arr:
    is_number = False
    if item.isnumeric():
        elem = f'{int(item):02}'
        is_number = True
    elif item[0] in ['+', '-'] and item[1:].isnumeric():
        elem = f'{item[0]}{int(item[1:]):02}'
        is_number = True
    if is_number:
        arr_2.append('"')
        arr_2.append(elem)
        arr_2.append('"')
    else:
        arr_2.append(item)

print(arr_2)
print(" ".join(arr_2))




