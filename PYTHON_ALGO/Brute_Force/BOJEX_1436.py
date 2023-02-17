n = int(input())
count = 0
i = 660

while True:
    check = list(map(int, str(i)))

    for j in range(len(check)-2):
        if check[j] == check[j+1] == check[j+2] == 6:
            count += 1
            break
    
    if count == n: 
        print(i)
        break
    i += 1