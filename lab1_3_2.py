text = "Пример строки для поиска символов кириллицы"

alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

unused_chars = ""

for char in alphabet:
    if char not in text:
        unused_chars += char

print(unused_chars)
