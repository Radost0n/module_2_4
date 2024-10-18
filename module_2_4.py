# Исходный список чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# списки для простых и непростых чисел
primes = []
not_primes = []

# Проверки простоты числа
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Функция для преобразования чисел, написанных словами
def parse_int(s):
    if s == 'ноль':
        return 0
    units = {'ноль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5, 'шесть': 6, 'семь': 7, 'восемь': 8,
             'девять': 9}
    dozens = {'десять': 10, 'двадцать': 20, 'тридцать': 30, 'сорок': 40, 'пятьдесят': 50, 'шестьдесят': 60,
              'семьдесят': 70, 'восемьдесят': 80, 'девяносто': 90}
    hundreds = {'сто': 100}
    thousands = {'тысяча': 1000}

    s = s.replace('-', ' ')
    s = s.split()
    result = []

    for i, val in enumerate(s):
        if val == 'и':
            continue
        try:
            result.append(units[val])
        except KeyError:
            try:
                result.append(hundreds[val])
            except KeyError:
                try:
                    result.append(dozens[val])
                except KeyError:
                    try:
                        result.append(thousands[val])
                    except KeyError:
                        continue
    return sum(result)

# Заполнение списков простыми и непростыми числами
for number in numbers:
    if number == 1:
        continue
    if is_prime(number):
        primes.append(number)
    else:
        not_primes.append(number)

# Вывод списка простого и непростого числа
print("Primes:", primes)
print("Not Primes:", not_primes)

# Предупреждение для пользователя
print("\nВнесите число, можно словами. Если надоест вносить числа, напишите 'стоп'.")

# Цикл для ввода чисел
while True:
    user_input = input("\nВведите число или 'стоп' для завершения: ").lower()

    if user_input == 'стоп':
        print("Вы завершили ввод.")
        break

    if user_input.isdigit():
        number = int(user_input)
    else:
        try:
            number = parse_int(user_input)
            if number == 0 and user_input != 'ноль':
                print("Введите корректно!")
                continue
        except Exception:
            print("Введите корректно!")
            continue

    # Проверка на простое введенное число
    if is_prime(number):
        print(f"Число {number} - это простое число.")
    else:
        print(f"Число {number} - это непростое число.")