n = int(input())
white_stones = []
for i in range(n):
    white_stones.append(list(map(int, input().split())))



for i in range(1, 20):
    for j in range(1, 20):
        if [i, j] in white_stones: print(1, end=" ")
        else: print(0, end=" ")
    print()