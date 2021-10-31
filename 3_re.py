# re library : Regural Expressions : 정규식 : 정해진 형태를 의미하는 식
# ex) 주민등록번호의 정규식 : 6자리숫자-7자리숫자
# ex2) email adress : ___@gmail.com
# ex3) 차량 번호 : 11가 1234 or 123가 1234
# ex4) IP 주소 : 192.168.0.1

# w3schools.com/python/python_regex_asp or docs.python.org/3/library/re.html

# < re summary > ❗ KEY CODES ❗
# 1. p = re.compile("정규식; 원하는 형태")
# 2. m = p.func("비교할 문자열") # func() : 정규식 p를 괄호안의 문자열과 어떻게 비교할 것인지 알맞는 함수 넣기

import re

p = re.compile("ca.e")  # p: pattern ; ca.e / (): which re will you compile
# . (ca.e) : 하나의 문자를 의미 > care, cafe, case (O) | caffe (X)
# ^ (^de)  : 문자열의 시작 > desk, destination (O) | fade (X)
# $ (se$)  : The end of string. > case, base (O) | face (X)


def print_match(m):
    # group(): If succeeding matching, print matched group. If failing to match, error occur
    # print(m.group())
    if m:
        print("m.group():", m.group())  # group() : 일치하는 문자열 반환 >> care
        # 입력받은 문자열 반환 >> careless / "string" is var
        print("m.string:", m.string)
        # 일치하는 문자열의 시작 index >> 0 (:careless와 care은 index 0 번째부터 일치)
        print("m.start()", m.start())
        print("m.end()", m.end())  # 일치하는 문자열의 끝 index >> 4
        print("m.span()", m.span())  # 일치하는 문자열의 시작과 끝 index 함께 표시 >> (0, 4)
    else:
        print("매칭되지 않음")


# Check whether "p"[패턴;정규식] match with the brackets or not
# m = p.match("careless") # match(): 주어진 문자열[괄호 값]의 처음부터 일치하는지 확인하기 때문에 careless도 매치에 성공함 ; 뒤 less 같이 있어도 상관없음
# print_match(m)

# m = p.search("careless")  # search : 주어진 문자열 [괄고 값] 중에 "p"와 일치하는게 있는지 확인
# print_match(m)  # success >> care

# findall() : 일치하는 모든 것을 리스트 형태로 반환; 괄호안에서 "p"와 일치하는게 여러개 있으면 다 반환
lst = p.findall("good care cafe")
print(lst)  # >> ['care', 'cafe']
