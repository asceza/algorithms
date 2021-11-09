# сортировка пузырьком
# thanks to -> https://www.youtube.com/watch?v=5BuCMzKYagg
# https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D1%80%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B0_%D0%BF%D1%83%D0%B7%D1%8B%D1%80%D1%8C%D0%BA%D0%BE%D0%BC
# вычислительная сложность O(N^2)

lst = [-14, 2, 0, 12, 9, -2]
n = len(lst)  # длина списка = число элементов

for i in range(0, n - 1):  # достаточно пройти на одну итерацию меньше
    for j in range(0, n - 1 - i):
        # проход по оставшимся не отсортированным парам
        # при i = 0, проходим все пары
        # при i = 1, проходим все кроме последней пары
        if lst[j] > lst[j + 1]:  # поменять знак для сортировки по убыванию
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

print(lst)
