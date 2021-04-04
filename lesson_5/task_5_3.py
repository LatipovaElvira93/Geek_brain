tutors = [
    'Ivan', 'Anastasiya', 'Petr', 'Sergey', 'Dmitriy', 'Boris', 'Elena',
]
klasses = [
    '9A', '7V', '9B', '9V', '8B', '10A'
]

def tutors_klasses(first_list, second_list):
    none_klass = len(first_list) - len(second_list)
    if none_klass > 0:
        second_list.extend([None for i in range(none_klass)])
    for row_1, row_2 in zip(first_list, second_list):
        yield row_1, row_2

gen = tutors_klasses(tutors, klasses)
print(list(gen))
