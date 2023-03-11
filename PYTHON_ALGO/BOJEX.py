# 7 3
# <3, 6, 2, 7, 5, 1, 4>
# 1234567
# 3 456712
# 6 71245
# 2 4571
# 7 145
# 5 14
# 1
# 4


# from collections import deque
# import sys
# input = sys.stdin.readline

# n, k = map(int, input().split())
# # n, k = 4,5

# q = deque([i for i in range(1, n+1)])
# remove_cnt = ''
# while q:
#     if len(q) >= k:
#         for _ in range(k):
#             q.append(q.popleft())
#         remove_cnt += str(q.popleft()) + ", "
#     else:
#         remove_cnt += str(q.popleft()) + ", "

# print("<" + remove_cnt[:-2] + ">")

from collections import deque
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

q = deque([i for i in range(1, n+1)])
remove_cnt = []

while q:
    q.rotate(-(k-1))
    remove_cnt.append(str(q.popleft()))

print("<" + ", ".join(remove_cnt) + ">")