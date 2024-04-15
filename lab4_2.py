def count_longest_word_occurrences(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            words = file.read().split()

        # Находим самое длинное слово
        longest_word = max(words, key=len)
        longest_length = len(longest_word)

        # Подсчитываем количество вхождений самого длинного слова в тексте
        count = 0
        for word in words:
            if len(word) == longest_length:
                count += 1

        return f"Самое длинное слово '{longest_word}' встречается {count} раз(а)."
    except FileNotFoundError:
        return "Файл не найден."
    except Exception as e:
        return f"Произошла ошибка: {e}"


# Пример использования функции
file_path = 'text.txt'  # укажите путь к вашему файлу
result = count_longest_word_occurrences(file_path)
print(result)
