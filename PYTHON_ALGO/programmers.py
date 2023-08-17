# 완전탐색 level1 모의고사
def sol1(answers):
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    scores = [0, 0, 0]
    
    # answers list의 index와 값을 동시에 반복
    for i, ans in enumerate(answers):
        # pattern list의 index와 값을 동시에 반복
        for j, pattern in enumerate(patterns):
            # 같은 answer 와 index를 받아서, pattern list에서 반복하면서 결과값 가져오기
            if ans == pattern[i % len(pattern)]:
                scores[j] += 1
    # 최고 득점자 조회
    max_score = max(scores)
    # score list를 돌면서, 최고 득점자와 같다면 결과값에 추가
    winner = [i + 1 for i, score in enumerate(scores) if score == max_score]
    
    return winner


# 해쉬 level2 전화번호 목록 (zip을 이용한 풀이와 hash를 이용한 풀이 모두 확인하기)
def sol2(phone_book):
    
    phone_book.sort()
    print(phone_book)
    book_size = len(phone_book)
    
    for i in range(book_size):
        for j in range(i, book_size):
            if len(phone_book[i]) < len(phone_book[j]):
                if phone_book[j].startswith(phone_book[i]):
                    return False

    return True

def sol3(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    print(hash_map)
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            print(temp, end=" ")
            if temp in hash_map and temp != phone_number:
                answer = False
            print()
    return answer

phone_book = ["12","123","1235","567","88"]


print(sol3(phone_book))