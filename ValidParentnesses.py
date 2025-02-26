def Valid(a: str) -> bool:
    skobki = {')': '(', '}': '{', ']': '['}
    steck = []

    for char in a:
        if char in skobki:
            if steck and steck[-1] == skobki[char]:
                steck.pop()
            else:
                return False
        else:
            steck.append(char)

    return not steck


print(Valid("(){}]"))
print(Valid("()[]{}"))
print(Valid("(]"))
print(Valid("()"))
print(Valid("([)]"))
print(Valid("{[]}"))
