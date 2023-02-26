incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}

# summ = 0
# for i in incomes.values():
#     summ +=i

summ = sum([i for i in incomes.values()])

for key in incomes:
    if incomes[key] == min(incomes.values()):
        malo = key

incomes.pop(malo)

for i_2 in incomes:
    print(i_2, incomes[i_2])
