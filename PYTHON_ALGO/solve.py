from collections import Counter

def solution(participant, completion):
    dict_h = {}
    sum_h = 0
    
    for person in participant:
        dict_h[hash(person)] = person
        sum_h += hash(person)
    
    for person in completion:
        sum_h -= hash(person)
    
    return dict_h[sum_h] 

def solution2(participant, completion):
    hashDict = {}
    sumHash = 0
    
    # 1. Hash : Participant의 dictionary 만들기
    # 2. Participant의 sum(hash) 구하기
    for part in participant:
        hashDict[hash(part)] = part
        sumHash += hash(part)
    
    # 3. completion의 sum(hash) 빼기
    for comp in completion:
        sumHash -= hash(comp)
    
    # 4. 남은 값이 완주하지 못한 선수의 hash 값이 된다
    return hashDict[sumHash]

p = ["mislav", "stanko", "mislav", "ana"]
print(Counter(p))
c = ["stanko", "ana", "mislav"]

print(solution(p, c))
print(solution2(p, c))


answer = Counter(p) - Counter(c)
print(list(dict(answer).keys())[0])