# 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
# 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
# 마지막 도착 계단은 반드시 밟아야 한다.
# 점수의 최대값은?

# 6
# 10, 20, 15, 25, 10, 20
'''
i+1 과 i+2의 크기를 비교해서 더 큰놈을 밟기     >> 리스트 인덱스 슬라이싱으로 하면 out of range 안뜬다
반복은 i가 n보다 작을때가지 >> 여기서 마지막까지 밟는거 신경써서 설정
연속된 3개를 이어서 밟으면 안된다...        >> 여기가 난관이네

다시, 더한 값들을 한번에 합치지 말고
(i-1) + i + (i+1) 이게 안되면
(i-3) + (i-1) + i 이렇게도 생각해봐야지.. 
리스트로 넣어주기

'''
import sys
input = sys.stdin.readline

n = int(input())
stair = []
for _ in range(n):
    stair.append(int(input()))

stepped = [0]*n

if n <= 2:
    print(sum(stair))
else:
    stepped[0] = stair[0]
    stepped[1] = stair[0] + stair[1]
    for i in range(2,n):
        stepped[i] = max(stepped[i-2] + stair[i], stepped[i-3] + stair[i-1] + stair[i])
    print(stepped[-1])