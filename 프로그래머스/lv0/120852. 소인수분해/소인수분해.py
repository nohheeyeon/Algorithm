def solution(n):
    factors = set()
    divisor = 2
    
    while n >= divisor:
        if n % divisor == 0:
            factors.add(divisor)
            n = n // divisor
        else:
            divisor += 1
    
    return sorted(factors)

     