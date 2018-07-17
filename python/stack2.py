astack = list()
bstack = list()

for i in range(int(input())):
    astack.append(i+1)
    bstack.append(int(input()))

for i in range(bstack[0]) : print("+")

if bstack[i] > bstack[i+1] : print("-")
else bstack[i] < bstack[i+1] : print("+")
print(astack,bstack)