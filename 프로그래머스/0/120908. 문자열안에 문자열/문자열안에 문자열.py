def solution(str1, str2):
    answer = 2
    l = len(str2)
    for i in range(len(str1)-l+1):
        if str1[i:i+l] == str2:
            answer = 1
            break
    return answer