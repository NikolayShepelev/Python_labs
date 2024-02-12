# Функция 1 Найти сумму непростых делителей числа.


def sum_divider(n):
    sum = 0
    for i in range(4, n+1):
        if n % i == 0:
            delit = i
            for j in range(4, delit+1):
                if delit % j == 0:
                    sum += delit
                    break
    return sum

number = 24
result = sum_divider(number)
print(f"Сумма непростых делителей числа {number} равна {result}")
