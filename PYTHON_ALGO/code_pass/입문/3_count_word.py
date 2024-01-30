# 임의의 문장을 입력받아 각 단어별로 나눈 후에 단어들의 중복되는 개수를 구하는 프로그램을 작성하시오.

 

# < 처리조건 >

# (1) 입력된 스트링은 글자의 제한은 없다. 즉, 알파벳 대.소문자, 공백, ', ' 등도 입력으로 들어올 수 있다. 

# (2) 입력된 문장에서 각 단어사이의 구분은 공백으로 한다. 

# (3) 단어에는 공백을 제외한 모든 문자들이 포함된다.​ 

# 임의의 문장을 입력받는다.(문장의 길이는 200 이하)

# 하나의 결과가 나온 후에도 계속 새로운 입력을 받다가, "END"가 입력되면 프로그램을 종료한다. (문장의 개수를 30을 넘지 않는다.)

# 각 문장 단위로 단어들의 발생 빈도를 오름차순 크기(아스키코드)순으로 출력한다.

from collections import Counter
import re

def count_word_frequencies():
    while True:
        sentence = input("문장을 입력하세요 (종료하려면 'END' 입력): ")
        if sentence == "END":
            break
        words = re.findall(r'\b\w+\b', sentence)
        frequencies = Counter(words)
        for word in sorted(frequencies, key=lambda x: (frequencies[x], x)):
            print(f"'{word}': {frequencies[word]}")
        print()

count_word_frequencies()