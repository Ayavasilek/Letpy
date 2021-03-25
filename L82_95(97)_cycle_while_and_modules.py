# l_82_83
# i = 0
# while i<20:
#     i+=2
#     print(i)

i = 33
while i>11:
    i-= 2
    print(i)

# l_84
# string = input()
# if len(string):
#     word = len(string) 
#     print(word)
# else: 
#     print('введите строку')
    
    # string = str(input())
# if string.count:
#     word = str(string [:1])
#     print(word)
# else: 
#     print('введите текст')
# while string():
    
    
 # string = str(input()) 
 # while string.count:
 #     word = str(string [:1])
 #     print(word)

string = input("Введите любую строку")
i = 0
while i < len(string):
    print(string[i])
    i += 1

# l_86
# string = input("Введите любую строку")
# i = 0
# while i < len(string):
#     if  i != len(string)-1 and string[i] == '#' and string[i+1] == '#':
#         break
#     print(string[i])
#     i += 1
    
    
    
    string = input("Введите любую строку")
i = 0
while i < len(string):
    if string[i:i+2] == "##":
        break
    print(string[i])
    i += 1
    
    
    
    string = input("Введите любую строку")
i = 0
sharps_pos = string.find("##")
while i < len(string):
    if i == sharps_pos:
        break
    print(string[i])
    i += 1


# l_88
string = input("Введите любую строку")
i = 0
while i < len(string):
    if string[i:i+2] == "##":
        break
    print(string[i])
    i += 1
else:
    print('Проверено')

# l_89
import time
print(time.asctime())

import math
print(math.atanh(0.5))

# l_91
# import canvas
# canvas.stroke_rect(50,50,100,100)
# canvas.fill_rect(80,80,50,50)
# canvas.draw()


import canvas
canvas.fill_rect(50, 50, 50, 50)
canvas.stroke_rect(150, 150, 100, 100)
canvas.draw()

# l_93
import canvas
import time
x = 0
delta = 2
while True :
    x < 350
    canvas.clear()
    canvas.fill_rect(x,100,50,50)
    canvas.draw()
    time.sleep(0.01)
    x = x + delta
    if x < 0 or x > 300:
        delta = -delta
        
        
# import canvas

# x = 0
# delta = 2
# while x < 350:
#     if x < 0 or x > 300:
#         delta = -delta
#     canvas.clear()
#     canvas.fill_rect(x, 100, 50, 50)
#     canvas.draw()
#     x = x + delta 


# l_95_97
first_list = [1,2,3,4,5]
second_list = [ 'a,b,c']
third_list = [1,'a',5,'c']
