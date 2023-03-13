# push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 덱에 들어있는 정수의 개수를 출력한다.
# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

import sys
input = sys.stdin.readline

def push_front(arr, x):
    return [x] + arr

def push_back(arr, x):
    return arr + [x]

def pop_front(arr):
    if arr:
        print(arr[0])
        return arr[1:]
    else: 
        print(-1)
        return arr

def pop_back(arr):
    if arr:
        print(arr[-1])
        return arr[:len(arr)-1]
    else: 
        print(-1)
        return arr

def size(arr):
    print(len(arr))

def empty(arr):
    print(0 if arr else 1)

def front(arr):
    if arr: print(arr[0])
    else: print(-1)

def back(arr):
    if arr: print(arr[-1])
    else: print(-1)

data = []

for _ in range(int(input())):
    order = list(map(str, input().split()))
    if order[0] == 'push_front':
        data = push_front(data, int(order[1]))
    elif order[0] == 'push_back':
        data = push_back(data, int(order[1]))
    elif order[0] == 'pop_front':
        data = pop_front(data)
    elif order[0] == 'pop_back':
        data = pop_back(data)
    elif order[0] == 'size':
        size(data)
    elif order[0] == 'empty':
        empty(data)
    elif order[0] == 'front':
        front(data)
    elif order[0] == 'back':
        back(data)