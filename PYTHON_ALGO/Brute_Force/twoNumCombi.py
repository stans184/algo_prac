# 임의의 숫자 조합
arr = [30, 40, 20, 13, 28, 39, 17, 39]
# 두 수 의 합을 저장하는 도구
res = []

for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        res.append(arr[i] + arr[j])

print(res)
print(min(res))
print(max(res))