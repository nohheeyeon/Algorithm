def solution(n):
    even = 0
    odd = 0
    if n % 2 == 0:
        for i in range(1, n+1):
            if i % 2 == 0:
                even += i**2
        return even
    else:
        for i in range(1, n+1):
            if i % 2 != 0:
                odd += i
        return odd
