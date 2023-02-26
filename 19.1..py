squares = dict()

chislo = int(input('Введите числоO:'))

for i in range(1,chislo+1):
    squares[i] = i*i
    print(i,'-', squares[i])


print(squares)