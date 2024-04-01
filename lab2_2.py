# Считывание количества строк
n = int(input("Введите количество строк: "))

# Словарь для подсчета частоты каждого слова
word_freq = {}

# Считывание и обработка строк
for _ in range(n):
    line = input()
    words = line.split()
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

# Создание списка кортежей (частота, слово) из словаря
freq_words_list = [(freq, word) for word, freq in word_freq.items()]

# Сортировка списка по частоте, а при равенстве - лексикографически.
# Изменяем порядок кортежа на (слово, частота) и сортируем по убыванию частоты
# и по возрастанию слов лексикографически
sorted_list = sorted(freq_words_list, key=lambda x: (-x[0], x[1]))

# Вывод слов в требуемом порядке
for freq, word in sorted_list:
    print(word)
