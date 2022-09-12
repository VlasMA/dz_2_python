# 1 Подсчитать сумму цифр в вещественном числе

number = int(input('Введите число: '))
sum = 0
count=1

while number > 0:
    count = number % 10
    sum = int(sum + count)
    number = number / 10

print(sum)