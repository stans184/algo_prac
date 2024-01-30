# 주어진 문자열에서 연속 3개의 문자가 IOI 이거나 KOI인 문자열이 각각 몇 개 있는지 찾는 프로그램을 작성하라.


# 문자열은 알파벳의 대문자로만 이루어진다. 

# 예를 들어 "KOIOIOI"라는 문자열은 KOI 1개 , IOI 2개가 포함되어있다.

# 입력은 한 줄이며 10,000자 이하의 알파벳 대문자로 구성된다.
# 출력은 2줄이며, 첫 번째 줄에는 KOI의 개수, 두 번째 줄에는 IOI의 개수를 각각 출력하라.

def count_patterns(s):
    koi_count = 0
    ioi_count = 0
    for i in range(len(s) - 2):
        if s[i:i+3] == "KOI":
            koi_count += 1
        elif s[i:i+3] == "IOI":
            ioi_count += 1
    return koi_count, ioi_count

# 입력 예시
input_str = input()
koi, ioi = count_patterns(input_str)

# 출력
print(koi)  # KOI의 개수
print(ioi)  # IOI의 개수