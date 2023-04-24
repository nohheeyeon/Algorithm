def solution(my_string):
    numbers = '1', '2', '3', '4', '5', '6', '7', '8', '9'
    for i in my_string:
        if i not in numbers:
            my_string = my_string.replace(i, '')
    return sum(map(int, my_string))