# Пустой список для хранения строк
strings = []

# Считываем количество строк, которое хотим ввести
n = int(input("Введите количество строк: "))

# Считываем строки с клавиатуры и добавляем их в список
for i in range(n):
    string = input(f"Введите строку {i+1}: ")
    strings.append(string)

# Упорядочиваем строки по их длине
sorted_strings = sorted(strings, key=len)

# Выводим упорядоченный список
print("Строки, упорядоченные по длине:")
for string in sorted_strings:
    print(string)
