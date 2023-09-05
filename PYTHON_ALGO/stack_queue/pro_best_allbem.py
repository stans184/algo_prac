# https://school.programmers.co.kr/learn/courses/30/lessons/42579

# genres	plays	return
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
# answer [4, 1, 3, 0]

def solution(genres, plays):
    
    albems = {}
    arr = []
    ans = []
    
    # 1번 조건
    # genre와 play를 hash를 이용해서 하나의 데이터로 만듬
    for genre, play in zip(genres, plays):
        # 동일한 genre 값이 있다면 계속 더해주는 것
        albems[genre] = albems.get(genre, 0) + int(play)
    # play의 수가 큰 순서대로 albem을 정렬
    sort_albem = sorted(albems.items(), key=lambda x:x[1], reverse=True)
    
    # 2번 조건
    # 답안을 도출하기 위해 index를 포함한 genre, play 정보를 list에 담아줌
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        arr.append([idx, genre, play])
    # play 수가 큰 순서대로 정렬
    sort_arr = sorted(arr, key=lambda x:x[2], reverse=True)
    
    # 1) play 총합이 많은 장르부터
    # 2) 개별 play 회수가 가장 많은 순서대로 돌면서
    # 최대 2개까지 답안에 넣을 수 있도록
    for albem,_ in sort_albem:
        cnt = 0
        for i in sort_arr:
            if cnt == 2: break
            elif i[1] == albem:
                ans.append(i[0])
                cnt += 1
                
    return ans
        
    
print(solution(genres, plays))