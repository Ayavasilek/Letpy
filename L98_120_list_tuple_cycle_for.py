# l_98 (Практические задания)
string = input()
words = string.split(" ")
print(len(words))


# l_105
string = input()
words = string.split(' ')
numbers = []
for w in words:
    if w.isdigit():
        numbers.append(int(w))
        numbers.sort()
        print(numbers)


# l_107
import canvas
for x in range (7, 180, 7):
    if x % 2 == 0:
        canvas.set_color("Red")
    else:
        canvas.set_color("Grey")
    canvas.circle(175, 175, x)

canvas.draw()
        
   #Letpy's code     
# import canvas

# for i in range(7,180,7):
#     if i % 2 == 0:
#         canvas.set_color('Red')
#     else:
#         canvas.set_color('Grey')
#     canvas.circle(175, 175, i)
# canvas.draw()


# l_112
string = input()
words = string.split()
for i, w in enumerate(words, 1):
    print(i, w)
    
    
# l_113
import canvas
import random
import time
colors = ('Red','Blue','Green',
        'Black','Pink','Yellow','Brown')
while True:
    x = random.randint(0,350)
    y = random.randint(0,350)
    for i, r in enumerate(range (150, 181, 5)):
        canvas.set_color(colors[i])
        canvas.circle(x, y, r)
        time.sleep(0.05)
        canvas.draw()

#    an exaple      
# import canvas
# import random
# import time

# colors = ('purple',
#           'red',
#           'blue',
#           'yellow',
#           'pink',
#           'lime',
#           'brown')
# while True:
#     x = random.randint(0,350)
#     y = random.randint(0,350)

#     for i, r in enumerate(range(150,181,5)):
#         canvas.set_color(colors[i])
#         canvas.circle(x, y, r)
#         canvas.draw()
#         time.sleep(0.05)

# l_120
first_dict = {'string': 5, ("kortage",): ['first, second'], 0.25: 'word'}
print(first_dict)
