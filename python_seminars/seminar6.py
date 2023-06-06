'''39
Даны два массива чисел. Требуется вывести те элементы
первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит
число N - количество элементов в первом массиве, затем N
чисел - элементы массива. Затем число M - количество
элементов во втором массиве. Затем элементы второго массива
'''

'''41
Дан массив, состоящий из целых чисел. Напишите
программу, которая в данном массиве определит
количество элементов, у которых два соседних и, при
этом, оба соседних элемента меньше данного. Сначала
вводится число N — количество элементов в массиве
Далее записаны N чисел — элементы массива. Массив
состоит из целых чисел.
Ввод:       Ввод:
5           5
1 2 3 4 5   1 5 1 5 1
Вывод:      Вывод:
0           2
(каждое число вводится с новой строки)
'''
# arr=[1,5,1,5,1]    
# count=0
# for i in range(1,len(arr)-1):
#     if arr[i-1]<arr[i]>arr[i+1]:
#         count+=1
# print(count)




''' 43
Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках.
'''

# arr=[1, 2, 3, 2, 3,1,0,3,6,2,6,8,3,7]
# count=0
# arr2=[]
# for i in range(len(arr)):
#     if arr[i] in arr2:
#         count+=1
#         arr2.remove(arr[i])
#     else:
#         arr2.append(arr[i])

# print(count)

'''
Два различных натуральных числа n и m называются
дружественными, если сумма делителей числа n
(включая 1, но исключая само n) равна числу m и
наоборот. Например, 220 и 284 – дружественные числа.
По данному числу k выведите все пары дружественных
чисел, каждое из которых не превосходит k. Программа
получает на вход одно натуральное число k, не
превосходящее 105
. Программа должна вывести все
пары дружественных чисел, каждое из которых не
превосходит k. Пары необходимо выводить по одной в
строке, разделяя пробелами. Каждая пара должна быть
выведена только один раз (перестановка чисел новую
пару не дает).
Ввод:   Вывод:
300     220 284
'''

# def sum_of_dividers(num):
#     sum = 1
#     for i in range(2, num // 2 + 1):
#         if num % i == 0 :
#             sum += i
#     return sum

# k=int(input('Введите предел: '))

# for i in range(2, k):
#     partner=sum_of_dividers(i)
#     if i==sum_of_dividers(partner) and i<partner:
#         print(i, partner)