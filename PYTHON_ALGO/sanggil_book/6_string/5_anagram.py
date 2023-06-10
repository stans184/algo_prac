# https://leetcode.com/problems/group-anagrams/

strs = ["eat","tea","tan","ate","nat","bat"] ## input
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

import collections


def group_anagram(strs:list[str]) -> list[list[str]]:
    anagram = collections.defaultdict(list)
    
    for word in strs:
        anagram[''.join(sorted(word))].append(word)
    
    return list(anagram.values())

print(group_anagram(strs))
