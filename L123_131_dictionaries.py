# l_123
catalog = {}
for i in range(3):
    name = input('Введите наименование товара') 
    quantity = int(input('Введите количество товара'))
    if name in catalog:
         catalog [name] += quantity
    else:
       catalog[name] = quantity
for c in catalog:
    print(c, ':', catalog[c])
    
    
    
    
# letpy's code   
# catalog = {}
# for i in range(3):
#     name = input('Введите наименование товара')
#     count = int(input('Введите количество товара'))
#     # если ключ (наименование товара) уже есть
#     # в словаре
#     if name in catalog:
#         # увеличиваем его значение на count
#         catalog[name] += count
#     else:
#         # иначе создаем ключ со значением count 
#         catalog[name] = count    

# for k in catalog:
#     print(k, ':', catalog[k])


# l_124
string = input()
string = string.lower()
string = string.replace('.', ' ')
string = string.replace(',', ' ')
string = string.split()

catalog = {}
for word in string:
    if word in catalog:
        catalog[word] += 1
    else:
        catalog[word] = 1
        
for word in catalog:
    print(word, ':', catalog[word])


# программировали, программировали, да не выпрограммировали


# l_126
user_input = input()
user_input = user_input.lower()
user_input = user_input.replace('.', ' ')
user_input = user_input.replace(',', ' ')
user_input = user_input.split()

catalog = {}
for word in user_input:
    if word in catalog:
        catalog[word] += 1
    else:
        catalog[word] = 1
keys = list(catalog.keys())
keys.sort()    
for word in keys:
    print(word, ':', catalog[word])


# l_127
catalog = {}
for i in range(3):
    name = input('Введите наименование товара') 
    quantity = int(input('Введите количество товара'))
    if name in catalog:
         catalog [name] += quantity
    else:
       catalog[name] = quantity
for c, h in catalog.items():
    print (c, ':', h)
    

# l_128
import random

list_ = []
for i in range(5):
    a = {}
    a['x'] = random.randint(0, 100) 
    list_.append(a)
print (list_)


# l_131
import canvas
import random
import time
colors = ('Red','Blue','Green',
        'Black','Pink')
        
circles = []
for i in range(5):
    circle = {
        'x': random.randint(20, 330),
        'y': random.randint(20, 330),
        'dx': random.choice([5,-5]),
        'dy': random.choice([5,-5]),
        'color': colors[i]
    }
    circles.append(circle)
    
while True :
    canvas.clear()
    
    for circle in circles:
        canvas.set_color(circle['color'])
        if circle['x']> 330 or circle['x'] < 20:
            circle['dx'] *= -1
        if circle['y']> 330 or circle['y'] < 20:
            circle['dy'] *= -1
            
        circle["x"] += circle["dx"]
        circle["y"] += circle["dy"]
        canvas.circle(circle["x"], circle["y"], 20)
        
    canvas.draw()
    time.sleep(0.01)

            
    