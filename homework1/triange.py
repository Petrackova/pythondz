# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

side_a = int(input())
side_b = int(input())
side_c = int(input())
if side_a + side_b > side_c \
        and side_a + side_c > side_b \
        and side_b + side_c > side_a:

    if side_a != side_b != side_c:
        print('Разносторонний')
    elif side_a == side_b == side_c:
        print('Равносторонний')
    else:
        print('Равнобедренный')

else:
    print('Треугольника с такими сторонами не существует')