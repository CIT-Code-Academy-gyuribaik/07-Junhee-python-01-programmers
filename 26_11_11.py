#옷가게 할인받기
def solution(price):
    if 100000<=price<300000:
        answer = price - price/20
    elif 300000<=price<500000:
        answer = price - price/10
    elif 500000<=price:
        answer = price - price/5
    else:
        answer = price
    return int(answer)


#배열 두 개 만들기
# 인덱싱을 잘 기억을 못해서 복습하고 문제를 풀었습니다. 다른 코드를 작성하고 제출을 해버려 덮어씌워져 저장이 되지 않았습니다.

#가위 바위 보
def solution(rsp):
    answer = ''
    for i in range(len(rsp)):
        if rsp[i] == '2':
            answer = answer + '0'    
        elif rsp[i] == '5':
            answer = answer +'2'
        else:
            answer = answer + '5'
    return answer

#문자열 정렬하기(2)
def solution(my_string):
    answer = ""
    for x in sorted(my_string.lower()):
        answer += x
    return answer
#lower 메서드와 sort 메서드를 함께 쓰는 것을 헷갈려해서, sorted 함수를 써볼 수 있도록 했습니다.
