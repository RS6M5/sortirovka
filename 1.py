def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Флаг для оптимизации: если за проход не было ни одной перестановки, алгоритм завершается
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Меняем элементы местами
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # Если не было ни одной перестановки за проход, массив уже отсортирован
        if not swapped:
            break

    return arr


# Пример использования
array = [64, 34, 25, 12, 22, 11, 90]
sorted_array = bubble_sort(array)
print("Отсортированный массив:", sorted_array)