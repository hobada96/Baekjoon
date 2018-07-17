stack = list()
a = input()
b = 0

try:
    for i in (a):
        if i == '(' : stack.append('(')
        elif i == '[' : stack.append('[')
        elif len(stack) == 0 and i == ')' : b = b+2
        elif len(stack) == 0 and i == '}' : b = b+3
        elif len(stack) != 0 and i == ')' : b = b*2
        elif len(stack) != 0 and i == '}' : b = b*3
    print(b)
except:
    print("0")