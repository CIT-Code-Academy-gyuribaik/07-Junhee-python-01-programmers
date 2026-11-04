#문자열 안에 문자열
def solution(str1, str2):
    if str2 in str1:
        return 1
    else:
        return 2

#제곱수 판별하기
def solution(n):
    i = int(n ** 0.5)
    if i*i == n:
        return 1
    else:
        return 2
