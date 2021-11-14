# Сортировка вставками
# thanks to -> https://www.youtube.com/watch?v=jMWvNTp_wFA
# https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D1%80%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B0_%D0%B2%D1%81%D1%82%D0%B0%D0%B2%D0%BA%D0%B0%D0%BC%D0%B8
# https://airtucha.github.io/SortVis/
# вычислительная сложность O(N^2)

lst = [7, -11, 3, 4, 0, -1, 5]
n = len(lst)  # длина списка = число элементов

for i in range(1, n):
    for j in range(i, 0, -1):
        # j принимает значения от i до 1 (0 не включается в диапазон) в обратном направлении с шагом 1
        # в нашем случае j поочереди = 1,   2, 1,   3, 2, 1,   4, 3, 2, 1,   5, 4, 3, 2, 1 ...
        if lst[j] < lst[j - 1]:
            lst[j], lst[j - 1] = lst[j - 1], lst[j]
        else:
            break
print(lst)

# при появлении новых элементов, этот алгоритм позволяет досортировывать
# что экономит ресурсы
