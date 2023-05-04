def solution(emergency):
    l = sorted(emergency, reverse=True)
    answer = []
    for i in emergency:
        answer.append(l.index(i)+1)
    return answer