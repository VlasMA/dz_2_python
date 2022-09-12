# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]  (1, 1*2, 1*2*3, 1*2*3*4)

num = int(input('Введите число: '))
number = 1
list_1 = []
for i in range(1, num + 1):
    number *= i
    list_1.append(number)
    # print(number)
print(f"Произведения чисел от 1 до {num}:  {list_1}")