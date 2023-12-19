def fn(x):
    n = len(x)
    for i in range(1, n):
        now = x[i]
        j = i-1
        while j >= 0 and x[j] > now:
            x[j+1] = x[j]
            j -= 1
            x[j+1] = now

x = [5,8,2,1,4,3]
fn(x)
print(x)

# import this
from collections import Counter

paragraph = "Bob hit a ball, the bit BALL flew far after it was hit"
banned = ['hit']

print(paragraph.split())
paragraph = paragraph.replace(',', ' ')
print(paragraph.split())

b = 'xdnwkfk'
print(sorted(b))