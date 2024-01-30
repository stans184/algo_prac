import itertools

def print_all(a):
    for n in a:
        print(n, end=" ")
    print()

t, a, b = map(int, input().split())

if t == 1:
    for p in itertools.combinations_with_replacement(range(1, b+1), a):
        print_all(p)
else:
    for p in itertools.combinations(range(1, b+1), a):
        print_all(p)