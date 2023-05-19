def solution(s):
    nums = s.split()
    result = 0
    prev_num = 0
    
    for num in nums:
        if num == "Z":
            result -= prev_num
        else:
            prev_num = int(num)
            result += prev_num
    
    return result