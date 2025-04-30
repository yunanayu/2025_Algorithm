def solution(money):
    cup = money // 5500
    num = money - cup*5500
    answer = [cup,num]
    return answer