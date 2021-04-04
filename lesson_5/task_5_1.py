
def nums_gen(n):
    for num in range(1, n+1, 2):
        yield num


print(*nums_gen(15))