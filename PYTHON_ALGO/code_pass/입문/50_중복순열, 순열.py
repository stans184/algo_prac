# T=1, 중복 순열
# 1부터 K까지 자연수 중에서 중복 있이 N개를 나열하는 모든 경우 출력
# ex) T=1, N=2, K=3
# (1,1) (1,2) (1,3) (2,1) (2,2) (2,3) (3,1) (3,2) (3,3)

# T=2, 순열
# 1부터 K까지 자연수 중에서 중복 없이 N개를 나열하는 모든 경우 출력

# ex) T=2, N=2, K=3
# (1,2) (1,3) (2,1) (2,3) (3,1) (3,2)

import itertools

def print_all(a):
    for n in a:
        print(n, end=" ")
    print()

t, a, b = map(int, input().split())

if t == 1:
    for p in itertools.product(range(1, b+1), repeat=a):
        print_all(p)
else:
    for p in itertools.permutations(range(1, b+1), a):
        print_all(p)