
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
#result = [23, 1, 3, 10, 4, 11]

def get_unique_list(num_list):
    unique_nums = set()
    all_nums = set()
    for num in num_list:
        if num not in all_nums:
            unique_nums.add(num)
        else:
            unique_nums.discard(num)
        all_nums.add(num)
    return [num for num in num_list if num in unique_nums]

result = get_unique_list(src)
print(result)