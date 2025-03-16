def solution(a, b):
    combined_value = int(f'{a}{b}')
    multiplied_value = 2*a*b
    if combined_value > multiplied_value :
        return combined_value
    else:
        return multiplied_value