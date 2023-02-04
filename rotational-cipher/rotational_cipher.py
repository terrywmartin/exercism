def rotate(text, key):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    output = ""
    for i in range(len(text)):
        if text[i].isspace():
            output += text[i]
        elif text[i].isalpha():
            index = alpha.index(text[i].lower())
            if index + key > len(alpha)-1:
                index = (index + key) - len(alpha)
                char = alpha[index] if text[i].islower() else alpha[index].upper()
                output += char
            else:
                char = alpha[index + key] if text[i].islower() else alpha[index + key].upper()
                output += char
        else:
            output += text[i]
    return output

