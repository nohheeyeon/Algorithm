def solution(cipher, code):
    answer = ''
    code_str = str(code)
    for i in range(code-1, len(cipher), int(code_str)):
        answer += cipher[i]
    return answer