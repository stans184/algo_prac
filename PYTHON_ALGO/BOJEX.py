# ax + by = c
# dx + ey = f

# 1 3 -1 4 1 7
# 2 -1

# 2 5 8 3 -4 -11
# -1 2

# x = (c - by)/a

# d*c/a + (e - d*b/a)*y = f
# (f - d*c/a)/(e-d*b/a) = y
import sys
input = sys.stdin.readline

a,b,c,d,e,f = map(int, input().split())

y = int((f - d*c/a)/(e-d*b/a))
x = int((c-b*y)/a)
print(x, y)