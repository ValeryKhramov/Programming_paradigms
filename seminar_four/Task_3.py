# lambda - выражения

# Простой калькулятор на лямбда-выражениях в Python

# Операции калькулятора
add = lambda x, y: x + y
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
divided = lambda x, y: x / y

while True:
    print("Выберите операцию:\n"
          "1. Сложение\n"
          "2. Вычитание\n"
          "3. Умножение\n"
          "4. Деление\n"
          "5. Выход")

    choice = input("Введите номер операции: ")

    if choice == '5':
        print("Выход из калькулятора.")
        break

    if choice not in ('1', '2', '3', '4'):
        print("Недопустимая операция. Пожалуйста, выберите операцию их списка.")
        continue

    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    # if choice == '1':
    #     print("Результат: ", add(num1, num2))
    # elif choice == '2':
    #     print("Результат: ", subtract(num1, num2))
    # elif choice == '3':
    #     print("Результат: ", multiply(num1, num2))
    # elif choice == '4':
    #     if num2 == '0':
    #         print("Деление на ноль невозможно.")
    #     else:
    #         print("Результат: ", divided(num1, num2))

    match choice:
        case '1':
            print("Результат: ", add(num1, num2))
        case '2':
            print("Результат: ", subtract(num1, num2))
        case '3':
            print("Результат: ", multiply(num1, num2))
        case '4':
            if num2 == '0':
                print("Деление на ноль невозможно.")
            else:
                print("Результат: ", divided(num1, num2))

