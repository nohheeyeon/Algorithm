def solution(babbling):
    answer = 0
    for word in babbling:
        for w in [ "aya", "ye", "woo", "ma" ]:
                 word = word.replace(w, ' ', 1) 
        if len(word.strip()) == 0:
            answer += 1
    return answer