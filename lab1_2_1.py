import random

# Исходная строка
original_string = "Пример строки для перемешивания слов"
print(original_string)

# Разбиваем строку на список слов
words = original_string.split()

# Перемешиваем каждое слово в списке
shuffled_words = []
for word in words:
    if len(word) > 3:  # Перемешиваем только слова с длиной больше 3
        middle = list(word[1:-1])
        random.shuffle(middle)
        shuffled_word = word[0] + ''.join(middle) + word[-1]
        shuffled_words.append(shuffled_word)
    else:
        shuffled_words.append(word)

# Объединяем перемешанные слова обратно в строку
shuffled_string = ' '.join(shuffled_words)

# Выводим результат
print(shuffled_string)
