def square_of_sum(number):
   
   return sum([ x for x in range(1,number+1)]) ** 2

def sum_of_squares(number):

    return sum([ x ** 2 for x in range(1,number+1)])


def difference_of_squares(number):
    num1 = square_of_sum(number)
    num2 = sum_of_squares(number)

    return num1 - num2 if num1 > num2 else num2 - num1
