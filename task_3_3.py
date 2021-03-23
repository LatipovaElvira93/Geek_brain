

def thesaurus(*args):
    result_dict = {}
    for item in args:
        first_char_name = item[0]
        if not result_dict.get(first_char_name):
            result_dict[first_char_name] = [item]
        else:
            result_dict[first_char_name].append(item)

    return result_dict

names_result = thesaurus('Амелия', 'Амир', 'Артур', 'Эльвира', 'Оксана', 'Руслан', 'Борис', 'Владимир')
print(names_result)
print(dict(sorted(names_result.items())))
# {'А': ['Амелия', 'Амир', 'Артур'], 'Э': ['Эльвира'], 'О': ['Оксана'], 'Р': ['Руслан'], 'Б': ['Борис'], 'В': ['Владимир']}
# {'А': ['Амелия', 'Амир', 'Артур'], 'Б': ['Борис'], 'В': ['Владимир'], 'О': ['Оксана'], 'Р': ['Руслан'], 'Э': ['Эльвира']}

