def is_armstrong_number(number):
    num = str(number)
    length = len(str(num))
    
    sum = 0
    for i in range(0,length):
        sum += float(num[i]) ** length

    if sum == number:
        return True
    else:
        return False

