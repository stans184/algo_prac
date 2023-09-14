# https://school.programmers.co.kr/learn/courses/30/lessons/84512

word1 = "AAAAE" # 6
word2 = "AAAE"  # 10
word3 = "I"     # 1563
word4 = "EIO"   # 1189

# restriction
# word의 길이는 1 이상 5 이하입니다.
# word는 알파벳 대문자 'A', 'E', 'I', 'O', 'U'로만 이루어져 있습니다.

# 입력이 짧아서 순열을 이용해서 풀어도 되고
# 다른 수학적 접근을 활용해봐도 됨

from itertools import product

def solution(word):
    vows = ['A', 'E', 'I', 'O', 'U']
    words = []
    for i in range(len(vows)):
        for c in product(vows, repeat=i+1):
            words.append(''.join(list(c)))

    words.sort()
    return words.index(word) + 1

print(solution(word3))

def solution2(word):
    answer = 0
    for i, n in enumerate(word):
        answer += (5 ** (5 - i) - 1) / (5 - 1) * "AEIOU".index(n) + 1
    return answer