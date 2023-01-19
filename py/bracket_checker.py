# 4. Дана скобочная последовательность: [((())()(())]]
# - Можно ли считать эту последовательность правильной?
# - Если ответ на предыдущий вопрос “нет” - то что необходимо в ней изменить, чтоб она стала правильной?

# Ответ: Нет.

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