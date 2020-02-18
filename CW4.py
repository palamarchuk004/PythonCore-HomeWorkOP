          # 1.1. Вивести всі парні числа менші 100. Через цикл while i for.
# i = 0
# while i < 100:
#     if i % 2 == 0:
#         print(i)
#     i = i + 1

# for i in range(0,100,2):
#     print(i)



          # 1.2. Вивести всі непарні числа менші 100. Оператор continue та без нього.
# for i in range(0,100):
#     if not i % 2 == 1:
#         continue
#     print(i)

# for i in range(0,100):
#      if not i % 2 == 0:
#          print(i)



          # 1.3. Перевірити чи список містить непарні числа. Опратор break
# a = [2,3,4,55,6,3,1,67,8,5,3,22]
# for i in a:
#     if i % 2 != 0:
#          print('Список містить непарні числа')
#          break
# else:
#      print('Список не містить непарних чисел')



          # 1.4. Список цілочисельного типу. Функція float.
# a = [2,3,4,55,6,3,1,67,8,5,3,22]
# for i in a:
#      print(float(i))



          # 1.5. Числа Фібоначі
# fib1 = 0 
# fib2 = 1
# n = int(input())
# print(fib1, end=' ')
# print(fib2, end=' ')
# for i in range(2, n+1):
#      fib1, fib2 = fib2, fib1 + fib2
#      if fib2 <= n+1:
#           print(fib2, end=' ')



          # 1.6. Список з елементів типу string. Вивести елементи по черзі за допомогою циклу for.
# sp = ['ad', 'gf', 'b', 'zz']
# for i in sp:
#      print(i)



          # 2.1. Порівняти введене число. Більше, менше.
# a = int(input("Введіть число A: "))
# b = int(input("Введіть число B: "))
# if a > b:
#     print("Число A більше ніж число B")
# else:
#     print("Число B більше ніж число A")



          #2.2. Перевірити введене число. Парне, непарне.
# a=int(input("Введіть число: "))
# if a % 2==0:
#     print("Число парне.")
# else:
#     print("Число непарне.")



          #2.3. Факторіал числа.
# i=int(input("Введіть чило: "))
# factorial = 1
# while i > 1:
#     factorial *= i
#     i -= 1
# print(factorial)

