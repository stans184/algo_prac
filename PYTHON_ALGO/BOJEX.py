t = int(input())

for i in range(t):
    arr = list(map(int, input().split()))
    max = 0
    for num in arr: 
        if num > max: max = num

    print(f'#{i+1} {max}')