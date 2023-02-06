def answer(question):
    numbers = []
    operations = []
    valid_operations = [ 'plus', 'minus', 'multiplied', 'divided']
    invalid_operations = [ 'cubed', 'Who']

    parser = question.strip('?').split()
    answer = 0
    is_operand = False
    is_number = False
    for word in parser:
        print(f'word: {word}')
        if word in invalid_operations:
            raise ValueError("unknown operation")

        if is_operand and word == 'by':
            continue

        if word in valid_operations:
            if is_operand:
                raise ValueError("syntax error")
            
            operations.append(word)
            is_operand = True
            is_number = False

        if word.lstrip('-').isdigit() or word.lstrip('-').isdecimal():
            if is_number:
                raise ValueError("syntax error")
            
            numbers.append(int(word))
            is_number = True
            is_operand = False

    if len(operations) == 0 and len(numbers) == 0:
        raise ValueError("syntax error")

    while len(operations) != 0:
        operand = operations.pop(0)
        if len(numbers) < 2:
            raise ValueError("syntax error")
        num1 = numbers.pop(0)
        num2 = numbers.pop(0)
        if operand == valid_operations[0]:
            answer = num1 + num2
            numbers.insert(0,answer)
        elif operand == valid_operations[1]:
            answer = num1 - num2
            numbers.insert(0,answer)
        elif operand == valid_operations[2]:
            answer = num1 * num2
            numbers.insert(0,answer)
        elif operand == valid_operations[3]:
            answer = num1 / num2
            numbers.insert(0,answer)

    answer = numbers.pop()
   
    return answer
