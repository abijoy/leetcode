def isValid(s:str) -> bool:
    if len(s) < 2 and len(s) % 2 != 0:
        return False

    opening_brackets = ['(', '{', '[']
    closing_brackets = [')', '}', ']']

    closing_dict = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    stack = []

    for i in s:
        print(f'STACK: {stack}')
        if i in opening_brackets:
            stack.append(i)
        elif i in closing_brackets and len(stack) and closing_dict[i] == stack[-1]:
            stack.pop()
        else:
            return False
    return True if len(stack) == 0 else False 
print(isValid("(]"))