# https://leetcode.com/problems/reverse-string/

# 내 풀이
def reverse_mysolve(s: list) -> list:
    answer = []
    while len(s) > 0:
        answer.append(s.pop())
    return answer

print(reverse_mysolve(["H", "a", "n", "n", "a", "h"]))

# pythonic way
def reverse_pythonic(s: list) -> list:
    s.reverse()
    print(s)

reverse_pythonic(["h", "e", "l", "l", "o"])
