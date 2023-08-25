def solution(name):

    # 조이스틱 총 조작 횟수
    count = 0
    # 문자간 이동 횟수 (A가 없다고 생각했을 때)
    move = len(name) - 1
    
    # A로부터 각 문자들까지 가는 최소 거리를 확인
    for i, ch in enumerate(name):
        # A부터 출발해서 해당 문자까지 가는 거리
        move_up = ord(ch) - ord('A')
        # A에서 Z로 돌아가서 해당 문자까지 가는 거리
        move_down = ord('Z') - ord(ch) + 1
        # 둘중 최소값을 조이스틱 조작 회수에 더하기
        count += min(move_down, move_up)
        
        # 연속된 A를 찾기 위한 index
        next_a = i+1
        # name 보다 작은 길이면서, 다음 문자가 A라면
        while next_a < len(name) and name[next_a] == 'A'
            # A index 하나 증가시킴
            next_a += 1
            
        # 최소값을 찾는다
        # 1. 모든 문자를 다 돌아가는 경우
        # 2. index와 next_a 의 현재값을 기준으로, 'A' 뭉텅이의 왼쪽으로 도는 경우
        # 3. index와 next_a 의 현재값을 기준으로, 'A' 뭉텅이의 오른쪽으로 도는 경우
        # 움직여서 'A' 뭉텅이를 찾고, 다시 돌아와서 'A' 뭉텅이의 반대편으로 돌아가서 접촉한다
        
        # 2. 왼쪽으로 도는 경우
        # i만큼 오른쪽으로 간 상태에서 'A' 뭉텅이를 발견했으므로, 다시 왼쪽으로 i만큼 돌아와야 함
        # 오른쪽으로 진행하던 입장에서 찾았으므로, 'A' 뭉텅이를 제외한 나머지 문자들의 개수를 더해야 함
        circle_left = 2*i + (len(name) - next_a)
        
        # 3. 오른쪽으로 도는 경우
        # i만큼 오른쪽으로 간 상태에서 'A' 뭉텅이를 발견
        circle_right = i + 2*(len(name) - next_a)
        
        move = min(move, circle_left, circle_right)
        
    return count + move