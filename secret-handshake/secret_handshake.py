def commands(binary_str):
    hand_shake = []
    actions = ['wink', 'double blink', 'close your eyes', 'jump']
    
    for i in range(len(binary_str)-1,0,-1):
        if binary_str[i] == '1':
            hand_shake.append(actions[(len(binary_str)-1) - i])

    if binary_str[0] == '1':
        hand_shake.reverse()

    return hand_shake

    
