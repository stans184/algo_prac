# https://school.programmers.co.kr/learn/courses/30/lessons/42842
import math

# my code
# 안됨
# 무언가 조건을 놓치고 있는듯

def sol_my(brown, yellow):
    area = brown + yellow
    ans = []
    
    for i in range(1, int(math.sqrt(area)) + 1):
        if area % i == 0:
            ans.append(i)
            ans.append(area // i)
    
    ans.sort(reverse=True)
    
    if area%2 == 0:
        return [ans[len(ans)//2 - 1], ans[len(ans)//2]]
    else:
        return [ans[len(ans)//2], ans[len(ans)//2]]
    

# search
# 코드 분석해보기
# 가로를 a 세로를 b라고 했을 때 갈색과 노란색 칸 수를 구해보면 수식은 2a - 2b - 4 = Brown이 된다.
# 가로 * 세로를 했을 때 각 겹치는 모서리 부분을 빼줘야 하기 때문에 -4를 해준다. 즉, 저 수식에서 a 값만 구하면 b값을 알 수 있게 된다.
# 다른 답안들도 참조해봐야함

def solution(brown, yellow):
    area = brown + yellow
    
    for height in range(1, area+1):
        if (area / height) % 1 == 0:
            width = area // height
        
            if width >= height:
                if (width * 2) + (height * 2) == brown + 4:
                    return [width, height]

print(solution(8,1))
print(solution(10,2))
print(solution(24,24))