"""
Напишите функцию, принимающую на вход только ключевые
параметры и возвращающую словарь, где ключ — значение
переданного аргумента, а значение — имя аргумента. Если
ключ не хешируем, используйте его строковое представление.
"""


def function(**kwargs):
    res = {}
    for k, v in kwargs.items():
        if v.__hash__ is not None:
            res[v] = k
        else:
            v = str(v)
            res[v] = k
    return res


print(function(rev=True, acc="YES", stroka=4))