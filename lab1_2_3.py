import random

# Исходная строка
original_string = "Дана строка в которой записаны слова через пробел"
print(original_string)

# Разбиваем строку на список слов
words = original_string.split()

# Перемешиваем список слов
random.shuffle(words)

# Объединяем перемешанные слова обратно в строку
shuffled_string = ' '.join(words)

# Вывод результата
print(shuffled_string)
