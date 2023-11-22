# Императивно: Сортировка списка в обратном порядке

def sort_list_imperative(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


numbers = [4, 7, 346, 7856, 45, 67, 12, 65, 34, 87, 23]
sort_list_imperative(numbers)
print("Отсортированный список в обратном порядке (императивно):", numbers)


# Декларативно: Сортировка списка в обратном порядке
numbers = [4, 7, 346, 7856, 45, 67, 12, 65, 34, 87, 23]
numbers.sort(reverse=True)
print("Отсортированный список в обратном порядке (декларативно):", numbers)
