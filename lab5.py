def is_credit_card_number(card_number):
    card_number = card_number.replace(" ", "")
    if not card_number.isdigit() or len(card_number) not in range(13, 20):
        return False
    n_digits = len(card_number)
    checksum = 0
    is_even = False
    for i in range(n_digits - 1, -1, -1):
        digit = int(card_number[i])
        if is_even:
            digit *= 2
            if digit > 9:
                digit -= 9
        checksum += digit
        is_even = not is_even
    return (checksum % 10) == 0

def validate_credit_card_number(card_number):
    if not isinstance(card_number, str):
        raise ValueError("Некорректный аргумент: номер кредитной карты должен быть строкой")
    if is_credit_card_number(card_number):
        return True
    else:
        return False

def main():
    user_input = input("Введите номер кредитной карты для проверки: ")
    try:
        if validate_credit_card_number(user_input):
            print("Номер кредитной карты валиден.")
        else:
            print("Номер кредитной карты невалиден.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
