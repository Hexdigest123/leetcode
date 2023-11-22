cases = ['()', '([)]', '{}[]()']


def is_valid(s):
    stack = []
    for c in s:
        if c in '([{':
            stack.append(c)
        else:
            if not stack or \
                    (c == ')' and stack[-1] != '(') or \
                    (c == '}' and stack[-1] != '{') or \
                    (c == ']' and stack[-1] != '['):
                return False
            stack.pop()
    return not stack


for i in cases:
    print(is_valid(i))
