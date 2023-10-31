import logging
import argparse


FORMAT = '{asctime}, {levelname}, {msg}'
logging.basicConfig(filename='logs_2.log', filemode='w', encoding='utf-8', level=logging.NOTSET,  format=FORMAT, style='{')
logger = logging.getLogger(__name__)

def log_dec(func):
    def wrapper(*args, **kwargs):
        logger.info(msg=f'Задача из домашней работы №2. Определение шестнадцатеричного вида введенного числа')
        try:
            logger.info(msg=f'Шестнадцатеричное число: {func(*args)}')
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f'Возникла ошибка {e} в функции {func.__name__} при аргументах {args}, {kwargs}')
        return None
    return wrapper

@log_dec
def hex_numbers(number):
    number = int(number)
    hex_string = "0123456789ABCDEF"
    hex_number = ""
    while number > 0:
        remains = number % 16
        hex_strings = hex_string[remains]
        hex_number = hex_strings + hex_number
        number //= 16
    return hex_number


#d = input()
#hex_numbers(d)

def par():
    parser = argparse.ArgumentParser()
    parser.add_argument('x1')
    args = parser.parse_args()
    return hex_numbers(args.x1)


print(par())