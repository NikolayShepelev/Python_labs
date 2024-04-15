import heapq


def solve(file_path):
    with open(file_path, 'r') as file:
        # Считываем N и K
        N, K = map(int, file.readline().split())
        # Считываем список измерений
        measurements = [int(file.readline().strip()) for _ in range(N)]

    # Проверяем, возможно ли выбрать три измерения с заданным интервалом
    if N < 2 * K + 1:
        return 'Невозможно найти три измерения с заданным интервалом'

    # Инициализируем три мин-кучи для хранения возможных значений
    heap1, heap2, heap3 = [], [], []
    min_sum = float('inf')  # Начинаем с бесконечно большой суммы

    # Заполняем кучу первых возможных элементов
    for i in range(N - 2 * K):
        heapq.heappush(heap1, (measurements[i], i))

    # Заполняем кучу вторых возможных элементов
    for j in range(K, N - K):
        # Удаляем из первой кучи элементы, которые уже нельзя использовать
        while heap1 and heap1[0][1] < j - K:
            heapq.heappop(heap1)
        if heap1:
            heapq.heappush(heap2, (measurements[j], j))

        if j >= 2 * K:  # Теперь добавляем элементы в третью кучу
            while heap2 and heap2[0][1] < j - K:
                heapq.heappop(heap2)
            if heap2:
                heapq.heappush(heap3, (measurements[j + K], j + K))

            if heap1 and heap2 and heap3:
                # Получаем минимальные значения из каждой кучи
                val1 = heap1[0][0]
                val2 = heap2[0][0]
                val3 = heapq.heappop(heap3)[0]  # Берем и удаляем мин элемент
                current_sum = val1 + val2 + val3
                min_sum = min(min_sum, current_sum)

    if min_sum == float('inf'):
        return 'Не найдены подходящие три измерения'
    return min_sum


# Вызов функции для решения и вывод результата
result = solve('27-165b.txt')
print(result)
