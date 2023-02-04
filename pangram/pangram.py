def is_pangram(sentence):
    alpha = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
    alpha_dict = {}

    for char in alpha.split():
        alpha_dict[char] = 0

    for char in sentence:
        if char.isalpha():
            alpha_dict[char.lower()] += 1
    
    return (all( alpha_dict[x] > 0 for x in alpha_dict))
