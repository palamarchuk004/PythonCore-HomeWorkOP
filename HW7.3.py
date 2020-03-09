def solution(number):
    a = 0
    while number > 0:
        number = number - 1        
        if number %5 == 0:
            a = a + number
        elif number %3 == 0:
            a = a + number
    return a
print(solution(10))

        