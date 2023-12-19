# https://leetcode.com/problems/longest-palindromic-substring/

def longest_palindrome(s:str) -> str:
    # palindrome 판별 및 투 포인터 확장
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    # 해당 사항이 없으면 리턴
    if len(s) < 2 or s == s[::-1]:
        return s
    
    # 슬라이딩 윈도우 우측으로 이동
    result = ''
    for i in range(len(s)-1):
        # expand(i, i+1) 과 expand(i, i+2) 로 나뉜 것은
        # palindrome 단어가 짝수로 만들어질 수도 있고, 홀수로 만들어질 수도 있기 때문
        result = max(result, expand(i, i+1), expand(i, i+2), key=len)
    
    return result

print(longest_palindrome("babadbadbfdfsdfsfsfffffdsdffaadbadbadbad"))
