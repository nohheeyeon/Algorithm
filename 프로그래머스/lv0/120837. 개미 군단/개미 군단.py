def solution(hp):
    answer = 0
    if hp>=5:
        answer = hp//5
        hp = hp % 5
    if hp>=3:
        answer = hp//3 + answer
        hp = hp % 3
    if hp>=1:
        answer += hp
    return answer