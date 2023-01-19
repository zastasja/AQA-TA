# 1. Составить алгоритм: если введенное число больше 7, то вывести “Привет”.
def number_over_seven():
    try:
        num = int(input("Введите число: "))
        if num > 7:
            print("Привет")
    except ValueError:
        print("Это не число")


number_over_seven()