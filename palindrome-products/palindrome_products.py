def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    # if the max_factor is less than the min_factor
    if max_factor < min_factor:
        raise ValueError("min must be <= max")
    max_product = 0
    
    factors = []

    for i in range(max_factor, min_factor - 1, -1):
        is_bigger = False
        for j in range(max_factor, i - 1, -1):
            product = str(i * j)
            if int(product) >= max_product:
                is_bigger = True
                if product == product[::-1]:
                    if max_product == int(product):
                        factors.append(tuple((i,j)))
                    if max_product < int(product):
                        factors.clear()
                        factors.append(tuple((i,j)))
                        max_product = int(product)
        if not is_bigger:
            break

    if max_product == 0:
        max_product = None
    output = ( max_product, factors)
    return output


def smallest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if max_factor < min_factor:
        raise ValueError("min must be <= max")

    factors = []
    min_product = -1
    for i in range(min_factor, max_factor+1):
        is_smaller = False
        for j in range(i, max_factor+1):
            product = str(i * j)
            if int(product) <= min_product or min_product <= 0:
                is_smaller = True
                if product == product[::-1]:
                    if min_product == int(product):
                        factors.append(tuple((i,j)))
                    if min_product > int(product) or min_product <= 0:
                        factors.clear()
                        factors.append(tuple((i,j)))
                        min_product = int(product)
        if not is_smaller:
            break

    if min_product == -1:
        min_product = None
    output = ( min_product, factors)
    return output

print(smallest(min_factor=10, max_factor=99))