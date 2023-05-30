# https://leetcode.com/problems/valid-palindrome/
import collections


# 1 리스트를 이용한 풀이
def palindrome_list(s: str) -> bool:
    strs = []
    for c in s:
        if c.isalnum():
            strs.append(c.lower())
    
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
        
    return True

print(palindrome_list(input()))

# 2 deque를 이용한 풀이 (list 보다 속도가 빠름)
def palindrome_deque(s: str) -> bool:
    strs = collections.deque()
    
    for c in s:
        if c.isalnum():
            strs.append(c.lower())
    
    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    
    return True

print(palindrome_deque(input()))
