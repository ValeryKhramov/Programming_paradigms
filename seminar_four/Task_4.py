# Изменяемое состояние (Не функциональный стиль)
numbers = [1, 2, 3, 4]
total = 0

for num in numbers:
    total += num
    print()

# Без изменяемого состояния (Функциональный стиль)
numbers = [1, 2, 3, 4]
total = sum(numbers)  # Создаем новое значение "total"
