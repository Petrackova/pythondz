import logging
import argparse

FORMAT = '{asctime}, {levelname}, {msg}'
logging.basicConfig(filename='logs_1.log', filemode='w', encoding='utf-8', level=logging.NOTSET,  format=FORMAT, style='{')
logger = logging.getLogger(__name__)

MIN_NUMBER = 0
MAX_NUMBER = 100_000


def log_dec(func):
    def wrapper(*args, **kwargs):
        logger.info(msg='Задача из семинара №1. Определение простоты числа из диапазона')
        try:
            logger.info(msg=f'{func(*args, **kwargs)}')
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f'Возникла ошибка {e} в функции {func.__name__} при аргументах {args}, {kwargs}')
        return None
    return wrapper


@log_dec
def simple_number(number):
    number = int(number)
    if MIN_NUMBER < number <= MAX_NUMBER:
        count = 0
        divider = 1
        LIMIT_COUNTER = 2
        while divider <= number:
            if number % divider == 0:
                count += 1
            divider += 1
        if count > LIMIT_COUNTER:
            return 'Composite'
        else:
            return 'Simple'

def par():
    parser = argparse.ArgumentParser()
    parser.add_argument('x1')
    args = parser.parse_args()
    return simple_number(args.x1)


print(par())

#if __name__ == '__main__':
#    d = input()
#    simple_number(d)