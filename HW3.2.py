          #2. Знайти добуток числа, записати його в реверсивному порядку та посортувати.

a = int(input("Введіть чотирьохзначне натуральне число: "))
d4 = a % 10 #Четверта цифра
a = a // 10
d3 = a % 10 #Третя цифра
a = a // 10
d2 = a % 10 #Друга цифра
a = a // 10
d1 = a % 10 #Перша цифра
print("Добуток цифер числа рівний:", d1*d2*d3*d4)
print("Число в реверсному порядку:", d4, d3, d2, d1)
print("Посортованні цифри за зростанням:", sorted([d1, d2, d3, d4]))