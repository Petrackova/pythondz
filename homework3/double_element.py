"""
Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
"""
print('Введите числа через пробел')
my_list = list(map(int, input().split()))
new_list = []
DOUBLE_ELEMENT = 2

for i in range(len(my_list)):
    if my_list.count(my_list[i]) >= DOUBLE_ELEMENT:
        if my_list[i] not in new_list:
            new_list.append(my_list[i])
print(new_list)