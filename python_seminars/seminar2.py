#задача 13
#кол-во положительных чисел подряд
#input 6 -> -20 30 -40 50 10 -10
#output: 2
# n=int(input('Введите n:'))
# count=0
# max=0

# for i in range(n):
#     t=int(input('Введите температуру:'))
#     if t>0:
#         count+=1
#     elif count>=max:
#         max=count
#         count=0

# if count>max:
#     max=count

# print('Макс. положительных дней:',max)

'''
По данному целому неотрицательному n вычислите
значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
чисел от 1 до N) 0! = 1 Решить задачу используя цикл
while
'''

# n=int(input('Введите число n:'))
# res=1
# i=1
# while i<=n:
#     res*=i
#     i+=1
# print(f'{n}! = {res}')

'''
Дано натуральное число A > 1. Определите, каким по
счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не
является числом Фибоначчи, выведите число -1.
'''

# a=int(input('Введите число a>1:'))
# x=0
# y=1
# count=2

# while x+y<a:
#     count+=1
#     temp=x
#     x=y   
#     y=temp+y

# if x+y==a:
#     print(count+1)
# else:
#     print(f'F(-1)')

'''
Пользователь вводит одно число N – количество
арбузов. Вторая строка содержит N чисел,
записанных на новой строчке каждое. Здесь каждое
число – это масса соответствующего арбуза
'''

# n=int(input('Введите число n:'))
# min=100
# max=0

# for i in range(n):
#     x=int(input('Введите массу арбуза:'))
#     if x>max:
#         max=x
#     if x<min:
#         min=x
# print('min',min,'max',max)
