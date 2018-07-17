import copy

stack = list()
exlist = list()
e = 0

repeat = int(input())
for i in range(repeat) :
    stack.append(int(input()))
    if i > 0 and stack[i-1] - stack[i] >  1 :
        bstack = copy.deepcopy(stack)
        bstack.sort()
        for j in range(i+1):
            if j > 0 and bstack[j] - bstack[j-1] != 1 : 
                e = 1
                
if e == 0 :
    
else : print("NO")
print(stack)