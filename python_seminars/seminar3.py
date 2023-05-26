'''
Дан список чисел. Определите, сколько в нем
встречается различных чисел.

Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6
'''

# myList=[1, 1, 2, 0, -1, 3, 4, 4]
# print(len(set(myList)))

'''
Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]
'''

# myList=[1, 2, 3, 4, 5]
# k=int(input('Введите число сдвигов: ')) % len(myList)
# print(myList[k:]+myList[:k])

######### вариант 2

# myList=[1, 2, 3, 4, 5]
# k=int(input('Введите число сдвигов: ')) % len(myList)
# for i in range(k):
#     myList.insert(0, myList.pop())
# print(myList)

'''
Напишите программу для печати всех уникальных
значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
":" S007 "}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
'''

# myList=[{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},{"VI": "S005"}, 
#    {"VII": " S005 "}, {"V":" S009 "}, {"VIII":" S007 "}]
# result=[]
# for item in myList:
#     result.append(list(item.values())[0])
# print(set(result))

'''
Дан массив, состоящий из целых чисел. Напишите
программу, которая подсчитает количество
элементов массива, больших предыдущего (элемента
с предыдущим номером)
Input: [0, -1, 5, 2, 3]
Output: 2 (-1 < 5, 2 < 3)
'''

# myList=[0, -1, 5, 2, 3]
# count=0

# for i in range(1,len(myList)):
#     if myList[i]>myList[i-1]:
#         count+=1

# print(count)

# result=[myList[i] for i in range(1,len(myList)) if myList[i]>myList[i-1]]
# print(result)