def steps(number):

    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    num = number
    counter = 0
    while (num > 1):
        counter += 1
        if num % 2 == 0:
            num = num / 2
        else:
            num = 3*num + 1
        
    if num == 1:
        return counter

