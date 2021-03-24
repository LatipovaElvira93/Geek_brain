
product = [57.8, 46.51, 97, 56.43, 67, 45.6, 64, 89.89, 78.9, 86.5]

for i in product:
    rub = int(i // 1)
    kop = int(i % 1 * 100)
print(f'{rub} руб {kop:02} коп')

product.sort()
for i in product:
    rub = int(i // 1)
    kop = int(i % 1 * 100)
print(f'{rub} руб {kop:02} коп')

reversed_prod = product[::-1]

for i in reversed_prod[0:5]:
    print(f'{int(i // 1)} руб {int(i % 1 * 100)} коп')

