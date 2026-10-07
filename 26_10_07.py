#배열 뒤집기
def solution(num_list):
    answer = num_list[::-1]
    return answer

#문자 반복 출력하기
def solution(my_string, n):
    answer = ""
    for i in range(len(my_string)):
        answer += my_string[i]*n
    return answer
