# 뒤집힌 문자열
def solution(my_string):
    x=len(my_string)
    answer = ''
    for i in range(x,0,-1):
        answer+=my_string[i]
    return answer


#짝수의 합
def solution(n):
    answer=0
    for i in range(2,n+1,2):
       answer = answer+i
    return answer
