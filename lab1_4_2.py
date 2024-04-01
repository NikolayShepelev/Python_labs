def find_and_remove_median(numeric_sample):
    """Находит и удаляет медианное значение из списка"""
    n = len(numeric_sample)
    # Сортируем список
    sorted_sample = sorted(numeric_sample)
    mid_index = n // 2
    # Для нечетного числа элементов
    if n % 2 == 1:
        median = sorted_sample[mid_index]
    # Для четного числа элементов берем нижнюю медиану
    else:
        median = sorted_sample[mid_index - 1]

    # Удаление медианного значения из исходного списка
    numeric_sample.remove(median)

    return median, numeric_sample

def main():
    sample = ["3", "1", "2", "5", "6", "8", "7"]
    numeric_sample = [int(x) for x in sample]  # Преобразуем в числа

    print("Исходный набор:", numeric_sample)

    while numeric_sample:
        median, numeric_sample = find_and_remove_median(numeric_sample)
        print("Медиана:", median)
        print("Оставшиеся элементы:", numeric_sample)

if __name__ == "__main__":
    main()
