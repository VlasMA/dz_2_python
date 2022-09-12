# Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов
# на указанных позициях. Позиции хранятся в списке positions - создайте этот список (например:
# positions = [1, 3, 6]).

n = int(input('укажите N: '))
l = '1, 3, 6'
s = 0
c = 1
l1 = []
for i in range(-n, n+1):
    l1.append(i)
l2 = l.split(',')
print(l1)
print(l2)
for i in l2:
    print(i)
    c = c * l1[int(i.strip())]
print(c)

    