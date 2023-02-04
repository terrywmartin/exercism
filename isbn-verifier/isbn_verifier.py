def is_valid(isbn):
    
    if isbn == "":
        return False

    if not isbn[-1].isnumeric() and isbn[-1].upper() != 'X':
        return False

    txt = isbn.replace('-','')
    for i in range(len(txt)-1):
        if not txt[i].isnumeric():
            return False
    if len(txt) != 10:
        return False

    total = 0
    for i in range(len(txt)):
        if txt[i].upper() == 'X':
            total += 10 * (10 - i)
        else:
            total += int(txt[i]) * (10 - i)

    if total % 11 == 0:
        return True
    return False

print(is_valid("3-598-2X507-9"))