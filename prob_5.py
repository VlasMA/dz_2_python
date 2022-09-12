# Реализовать алгоритм перемешивания списка.

import random as rand

list_1 = []
list_2 = []
n = int(input('Размер списка: '))
for i in range(n):
	list_1.append(rand.randint(0, 50))
print(list_1)
for i in range(n):
	m = rand.randint(0, len(list_1)-1)
	print(m)
	m2 = list_1.pop(m)
	list_2.append(m2)
print(list_2)



# from random import randint

# for i in range(5):
# 	a = randint(1,100)
# 	print(list[a])