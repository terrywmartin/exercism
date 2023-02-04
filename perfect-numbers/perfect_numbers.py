def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    total = 0

    total = sum([ x if x == 1 or number % x == 0 else 0 for x in range(1,number)])

    if total == number:
        return "perfect"
    if total > number:
        return "abundant"
    return "deficient"
