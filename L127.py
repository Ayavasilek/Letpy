catalog = {}
for i in range(3):
    name = input('Введите наименование товара: ')
    quantity = int(input('Введите количество товара: '))
    if name in catalog:
        catalog[name] += quantity
    else:
        catalog[name] = quantity
for c, h in catalog.items():
    print(c, ':', h)
