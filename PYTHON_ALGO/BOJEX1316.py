n = int(input())
words = []
for _ in range(n):
    words.append(input())

groupWordCnt = 0

# 어떤 알파벳이 나왔는데
# 바로 다음 순서에서 동일한게 나오면 커서를 그거로 옮기고 다시 검색
# 만약 다음 순서에서 다르게 나오면 그 뒤에 문자열 중에서 동일한 문자가 있나 검색
for word in words:
    checker = True
    for i in range(len(word)-1):
        if word[i] == word[i+1]: continue
        else:
            for j in range(i+1, len(word)):
                if word[i] == word[j]: checker = False
    if checker: groupWordCnt += 1

print(groupWordCnt)