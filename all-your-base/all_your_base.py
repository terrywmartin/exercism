def rebase(input_base, digits, output_base):
    
    # for input.
    if input_base < 2:
        raise ValueError("input base must be >= 2")

    # another example for input.
    for digit in digits:
        if digit < 0  or digit >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")

    # or, for output.
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    if len(digits) == 0:
        digits.append(0)

    total = 0
    for i in range(len(digits)):
        total += digits[i] * (input_base ** ((len(digits)-1) - i))

    n = total
    output = []
    if n == 0:
        output.append(0)
    while n != 0:
        output.append(n % output_base)
        n = int(n / output_base)
    
    output.reverse()
    return output
