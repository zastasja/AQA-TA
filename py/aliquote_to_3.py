# 3. Составить алгоритм: на входе есть числовой массив, необходимо вывести элементы массива кратные 3
def aliquote_to_3():
    try:
        num = map(int, input("Введите числа через пробел:").split())
        entered_list = list(num)
        new_list = [x for x in entered_list if x % 3 == 0 and x != 0]
        print(*new_list)
    except ValueError:
        print("Это не цифры")


aliquote_to_3()