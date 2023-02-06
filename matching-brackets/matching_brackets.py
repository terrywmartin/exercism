def is_paired(input_string):
    bracket_check = []

    for i, char in enumerate(input_string):
        if char in "[{(":
            bracket_check.append(char)
        if char in "]})":
            if len(bracket_check) == 0:
                return False
            if char == ']' and bracket_check[-1] != '[':
                return False
            if char == ')' and bracket_check[-1] != '(':
                return False
            if char == '}' and bracket_check[-1] != '{':
                return False
            bracket_check.pop()
    if len(bracket_check) == 0:
        return True
    return False

