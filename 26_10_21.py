#배열 자르기
def solution(numbers, num1, num2):
    answer = numbers[num1:num2+1]
    return answer

#순서쌍의 개수
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i==0:
            answer = answer + 1
    return answer

#점의 위치 구하기
def solution(dot):
    if 0<dot[0] and 0<dot[1]:    
        answer = 1   
    elif dot[0]<0 and 0<dot[1]:    
        answer = 2
    elif dot[0]<0 and dot[1]<0:    
        answer = 3
    elif 0<dot[0] and dot[1]<0:    
        answer = 4
    return answer

# 숨어있는 숫자의 덧셈(1)
def solution(my_string):
    answer = 0
    for i in range(len(my_string)):
        if my_string[i].isdigit():
            answer=answer+int(my_string[i])   
    return answer
