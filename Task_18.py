# Требуется найти в массиве A[0..N-1] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел A[i]. Последняя строка содержит число X


num = int (input("Введите количество элементов списка: "))
list1 = [0]*num
for i in range(len(list1)):
    list1[i] = int(input (f"Введите {i} элемент списка: "))
numbers = int (input ("Введите число для поиска ближайшего к нему: "))
i=0
while numbers == list1[i]:
    i+=1
numbers = list1[i]
for list in list1:
    if list != numbers:
        if abs (list - numbers) < abs (numbers1 - numbers):
            numbers1 = list
print(f"Ближайшее число к числу {numbers} это {numbers1}")
