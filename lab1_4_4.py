def max_char_frequency(s):
    """
    Возвращает частоту наиболее часто встречающегося символа в строке.
    """
    # Создаем словарь для подсчета встречаемости каждого символа
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Находим максимальную частоту встречаемости символа
    max_frequency = max(char_count.values())
    return max_frequency


def sort_strings_by_most_common_char_frequency(strings):
    """
    Возвращает список строк, отсортированный по возрастанию частоты
    самого распространенного символа в каждой строке.
    """
    return sorted(strings, key=max_char_frequency)


# Пример списка строк
strings = ["abccc", "ddeeff", "ggghhhhhii", "jjjjjjjjjjjjjjj", "kkkk"]

# Сортировка строк
sorted_strings = sort_strings_by_most_common_char_frequency(strings)

# Вывод отсортированного списка строк
print("Отсортированный список строк по частоте встречаемости самого распространенного символа:")
for string in sorted_strings:
    print(string)
