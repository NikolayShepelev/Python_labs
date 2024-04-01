def is_local_maximum(arr, index):
    # Проверяем, находится ли индекс в пределах массива
    if index >= 0 and index < len(arr):
        # Для первого элемента сравниваем только со вторым
        if index == 0:
            return arr[index] > arr[index + 1]
        # Для последнего элемента сравниваем только с предпоследним
        elif index == len(arr) - 1:
            return arr[index] > arr[index - 1]
        # Для остальных сравниваем со значениями с обеих сторон
        else:
            return arr[index] > arr[index - 1] and arr[index] > arr[index + 1]
    else:
        # Индекс вне диапазона массива
        return False

# Данный массив
array = [3, 6, 4, 8, 3, 6, 2]

# Индекс для проверки
index = 1

# Вызываем функцию и выводим результат
print(f"Элемент по индексу {index} является локальным максимумом: {is_local_maximum(array, index)}")
