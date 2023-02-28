# l_68 (Практические задания)
 # string = str(input())
 # print(string.upper())

string = str(input())
print(string.lower())

# l_79
a = input("Введите первое число")
b = input("Введите первое число")
if a.isdigit() and b.isdigit():
    print("Сумма = " + str(int(a) + int(b)))    
else:
    print("Вы ввели не число")

# l_73
string = input()
if len(string) >= 2 :
    print(string[0] + string[-1])
else:
    print('Ошибка')


# l_75
string = input()
if len(string) >= 5 :
    print(string[:3], string[-3:])
else: 
    print('Ошибка')

# l_77
string = input()
string = string.replace(" ", "").lower()
if string == string[::-1] :
    print('да')
else:
    print('нет')

# l_78
number = input()
if len(number) >= 8 and number.isdigit() :
    stars_count = len(number)-4
    stars = "*" * stars_count
    print(stars + number[-4:])
else:
    print("Ошибка")
    
    
# l_79
text = input("Введите любой текст")
sharp_index = text.find('#')
if sharp_index != -1 :
    print(text[:sharp_index])
else: 
    print(text)
    
