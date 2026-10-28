#배열 원소의 길이
def solution(strlist):
    answer = []
    for i in range(len(strlist)):
        answer.append(len(strlist[i]))
    return answer

#대문자와 소문자
def solution(my_string):
    answer = ''
    for i in range(len(my_string)):
        if my_string[i].isupper():
            my_string[i].append.lower()
        elif my_string[i].islower():
            my_string[i].upper()
    return answer

#약수 구하기
def solution(n):
    answer = []
    for i in range(1,n):
        if n%i==0:
            answer.append(i)
    answer.append(n)            
    return answer

#편지
def solution(message):
    return 2*len(message)
