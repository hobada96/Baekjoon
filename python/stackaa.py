for i in range(int(input())):
    stack = list()
    a = input()
    for j in a:
        if(j == '(') : 
            stack.append('(')
        elif(j == ')') :
            if (len(stack) == 0 or stack[0] != '(') : stack.append("Error")
            else : stack.pop()
    if(len(stack)==0) : print("YES")
    else : print("NO")