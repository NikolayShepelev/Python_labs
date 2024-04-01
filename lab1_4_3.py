def average_ascii(s):
    """Вычисляет среднее значение ASCII символов строки."""
    return sum(ord(char) for char in s) / len(s)

def max_triple_avg_ascii(s):
    """Находит максимальное среднее значение ASCII кода для троек подряд идущих символов."""
    max_avg = 0
    for i in range(len(s) - 2):  # Идем до предпоследнего символа, чтобы сформировать тройки
        current_avg = sum(ord(s[j]) for j in range(i, i + 3)) / 3
        max_avg = max(max_avg, current_avg)
    return max_avg

def sort_strings(strings):
    """Сортирует строки в соответствии с условием задачи."""
    # Вычисляем среднее значение ASCII кодов всех символов и максимальное среднее значение троек
    # Затем сортируем исходный список строк в порядке увеличения разницы этих значений
    strings.sort(key=lambda s: max_triple_avg_ascii(s) - average_ascii(s))
    return strings

# Тестовый список строк
strings = ["abc", "defgh", "ijklmno", "pqr", "stuv", "wxyz"]
sorted_strings = sort_strings(strings)

# Вывод отсортированного списка
print("Отсортированный список строк:")
for string in sorted_strings:
    print(string)
