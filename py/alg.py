import builtins
import mock
# 1. Составить алгоритм: если введенное число больше 7, то вывести “Привет”.
def number_over_seven():
    try:
        num = int(input("Введите число: "))
        if num > 7:
            print("Привет")
    except ValueError:
        print("Это не число")


number_over_seven()

# 2. Составить алгоритм: если введенное имя совпадает с Вячеслав, то вывести “Привет, Вячеслав”,
# если нет, то вывести "Нет такого имени"
def name_checker():
    name = input("Введите имя:")
    if name == "Вячеслав":
        print(f"Привет, {name}")
    else:
        print("Нет такого имени")


name_checker()

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

# 4. Дана скобочная последовательность: [((())()(())]]
# - Можно ли считать эту последовательность правильной?
# - Если ответ на предыдущий вопрос “нет” - то что необходимо в ней изменить, чтоб она стала правильной?

# Ответ: Нет. В начале не хватает открытой скобки "]", в конце перед квадратными скобками не хватает закрытой ")"
def bracket_checker():
    s = "[((())()(())]]"
    stack = []
    is_good = True
    for i in s:
        if i in "({[":
            stack.append(i)
        elif i in "]})":
            if not stack:
                is_good = False
                break
            close_bracket = stack.pop()
            if close_bracket == "(" and i == ")":
                continue
            if close_bracket == "[" and i == "]":
                continue
            if close_bracket == "{" and i == "}":
                continue
            is_good = False
            break

    if is_good and len(stack) == 0:
        print("YES")
    else:
        print("NO")


bracket_checker()
