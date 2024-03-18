# Исходная строка
original_string = "a1b2c3d4e5f"
print(original_string)

# Переменные для цифр и букв
digits = ''
letters = ''

# Разделяем цифры и буквы
for char in original_string:
    if char.isdigit():
        digits += char
    else:
        letters += char

# Объединяем цифры и буквы в новую строку
new_string = digits + letters

# Вывод результата
print(new_string)
