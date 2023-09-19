"""
 Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
 Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
 Достаточно вернуть один допустимый вариант.
 Верните все возможные варианты комплектации рюкзака.
"""
print('Введите количество вещей для похода')
count_thing = int(input())
print(f'Введите вещи через пробел, количество вещей = {count_thing}')
list_thing = list(input().split())
print(f'Введите массу вещи через пробел,количество вещей = {count_thing}')
list_weight = list(map(int, input().split()))
print('Максимальная грузоподъемность')
max_weight = int(input())
thing_dict = dict(zip(list_thing,list_weight))
print(thing_dict)
summ_thing = {}

for key,value in thing_dict.items():
    if max_weight-value >= 0:
        summ_thing[key] = value
        max_weight -= value

for key, value in summ_thing.items():
    print(key, ' : ', value)

print(f'Поместилось всего {len(summ_thing)} вещи, весом {sum(summ_thing.values())} кг.')