def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# Функция для проверки, является ли число простой цифрой (2, 3, 5, или 7)
def is_prime_digit(x):
    return x in [2, 3, 5, 7]


# Функция для подсчета суммы простых цифр числа
def sum_of_prime_digits(n):
    return sum(int(digit) for digit in str(n) if is_prime_digit(int(digit)))


# Основная программа
def main():
    # Ввод исходного числа
    n = int(input("Введите число: "))

    # Подсчет суммы простых цифр исходного числа
    sum_primes = sum_of_prime_digits(n)

    # Счетчик для подсчета количества нужных чисел
    count = 0

    for i in range(1, n):
        # Проверка условий: не является делителем исходного числа,
        # не взаимнопростое с исходным числом и взаимнопростое с суммой простых цифр
        if n % i != 0 and gcd(n, i) != 1 and gcd(sum_primes, i) == 1:
            count += 1

    # Вывод результата
    print("Количество нужных чисел:", count)


# Запуск программы
if __name__ == '__main__':
    main()
