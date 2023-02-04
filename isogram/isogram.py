def is_isogram(string):
    
    for i in range(len(string)):
        if string.lower().count(string[i].lower()) > 1 and string[i].isalpha():
            return False
    
    return True

