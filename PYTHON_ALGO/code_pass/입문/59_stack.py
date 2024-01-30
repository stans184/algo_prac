n = int(input())

stack = []

for i in range(n):
    order = list(map(str, input().split()))
    if order[0] == 'i': stack.append(int(order[1]))
    elif order[0] == 'o':
        if stack: print(stack.pop())
        else: print('empty')
    elif order[0] == 'c': print(len(stack))