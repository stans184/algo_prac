# input = 4
# output
# 4! = 4 * 3!
# 3! = 3 * 2!
# 2! = 2 * 1!
# 1! = 1
# 24

def facto(n):
    if n >= 2:
        print(f"{n}! = {n} * {n-1}!")
        return facto(n-1) * n
    else:
        print(f"{n}! = {n}")
        return 1
    
print(facto(int(input())))