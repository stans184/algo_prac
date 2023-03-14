from collections import deque
import heapq
# 위에 두개 비교해보기

import sys
input = sys.stdin.readline

def fibo(n):
    if n <= 2:
        return 1
    else:
        a, b = 1, 1
        for i in range(n-2):
            a, b = b, a+b
        return b

number = int(input())
print(fibo(number), number-2)