small_storage = {'Гайка': 500, 'Дрель': 5000, 'Гвоздь': 20}


print(small_storage)

poisk = input('Введите наименованеи: ')

if poisk in small_storage:
    print(small_storage[poisk])
else:
    print('Такого товара нет')
