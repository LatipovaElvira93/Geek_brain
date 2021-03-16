cube = [ ]
for x in range(0, 1001):
    if x % 2 != 0:
        cube.append(x**3)
#print(cube)

result_1 = 0
for i in cube:
    sum = 0
    while i != 0:
        sum = sum + i % 10
        i = i // 10
    if sum % 7 == 0:
        result_1 = result_1 + sum
#print("Result 1: " + str(result_1))

result_2 = 0
for index, elem in enumerate(cube):
    test = elem + 17
    cube[index] = test
    sum = 0
    while test != 0:
        sum = sum + test % 10
        test = test // 10
    if sum % 7 == 0:
        result_2 = result_2 + sum
#print("Result 2: " + str(result_2))

