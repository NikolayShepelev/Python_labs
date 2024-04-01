# Ввод списка элементов
input_str = input("Введите элементы списка, разделенные пробелом: ")
input_list = input_str.split()

# Словарь для подсчета количества каждого элемента
count_dict = {}

for item in input_list:
    # Подсчет количества каждого элемента в списке
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1

# Список для элементов, встретившихся более трех раз
result_list = []

for item, count in count_dict.items():
    if count > 3:
        result_list.append(item)

# Вывод результата
print("Элементы, встретившиеся более трех раз:", result_list)
