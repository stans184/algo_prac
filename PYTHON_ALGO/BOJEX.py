import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    order = input().rstrip()
    n = int(input())
    numbers = deque(input().rstrip()[1:-1].split(','))

    isReverse, isNormal = False, True

    if n == 0: numbers = deque([])

    for o in order:
        if o == 'R': isReverse = not isReverse
        elif o == 'D':
            if not numbers:
                isNormal = not isNormal
                print('error')
                break
            else:
                if isReverse: numbers.pop()
                else: numbers.popleft()
    if isNormal:
        if isReverse:
            numbers.reverse()
            print('[' + ','.join(numbers) + ']')
        else:
            print('[' + ','.join(numbers) + ']')