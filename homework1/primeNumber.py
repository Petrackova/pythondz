# Напишите код, который запрашивает число и сообщает, является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

number = int(input())
MIN_NUMBER = 0
MAX_NUMBER = 100_000
if MIN_NUMBER < number <= MAX_NUMBER:
    count = 0
    divider = 1
    LIMIT_COUNTER = 2

    while divider <= number:
        if number % divider == 0:
            count += 1
        divider += 1

    if count > LIMIT_COUNTER:
        print('Composite')
    else:
        print('Simple')
else:
    print('Error input')
