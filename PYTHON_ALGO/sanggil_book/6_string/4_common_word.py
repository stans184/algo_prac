# https://leetcode.com/problems/most-common-word/

import collections
import re

# 이걸 코테에서 쓸 수 있나?
# 안된다면 다른 대안은 있나?

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

def most_common_word(paragraph:str, banned:list[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() 
             if word not in banned]
    
    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]

print(most_common_word(paragraph, banned))
