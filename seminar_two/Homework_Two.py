# Я написал скрипт, используя процедурную парадигму, так как в дальнейшем можно будет переиспользовать данную функцию
def multiplication_table(num):
    for i in range(1, num + 1):
        print(f"{num} * {i} = {i * num}")
    print()


multiplication_table(8)

multiplication_table(5)

