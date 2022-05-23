# Сформировать список из N членов последовательности. Для N = 5: 1, -3, 9, -27, 81 и т.д.7 
 
# N = int(input("Введите число N")) 
# result = [] 
# for i in range(N): 
#     result.append(3**i) 
# for i in range(0,N-1,2): 
#     result[i+1] = -(result[i+1]) 
# print(result)
6
    # Для натурального n создать словарь индекс-значение, состоящий из элементов 
# последовательности 3n + 1. Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# def new_dictionary(number):
#     dictionary = {}
#     for i in range(number):
#         values = (3*(i+1)+1)
#         dictionary[f'{i+1}'] = f'{values}'
#     return dictionary

# print("Введите N ")
# N = int(input())
# dictionary = new_dictionary(N)
# print(dictionary)

# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

# string_one = input("Введите первую строку ")
# string_two = input("Введите вторую строку ")
# count = string_one.count(string_two)
# if count > 0:
#     print(f"Вторая строка входит {count} раз в первую строку")
# else:
#     print("Вторая строка не входит в первую строку")

# #Подсчитать сумму цифр в вещественном числе.
# def DigitToInt(digit):
#     digit = digit.replace(",",".")
#     digit = digit.replace(".","")
#     digit = int(digit) 
#     return digit 

# print("Введите вещественное число ")
# digit = input()
# digit = DigitToInt(digit)
# sum = 0
# while digit!=0:
#     sum = sum + digit%10
#     digit = digit//10
# print(sum)

# # Написать программу получающую набор произведений чисел от 1 до N. 
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]

print("Введите N ")
N = int(input())
power = 1
result = []
for i in range(1,N+1):
    power*=i
    result.append(power)
print(result)

