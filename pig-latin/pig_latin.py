def translate(text):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    consonant_sound = ['sh', 'gl', 'ch', 'ph', 'tr', 'br', 'fr', 'bl', 'gr', 'st', 'sl', 'cl', 'pl', 'fl']

    words = text.split(' ')
    print(words)
    pig_latin = []
    for i in range(len(words)):
        if words[i][0] in vowels or words[i][0:2] == 'xr' or words[i][0:2] == 'yt':
            pig_latin.append(words[i] + 'ay')
        elif words[i][0:2] == 'qu':
            pig_latin.append(words[i][2:] + words[i][0:2] + 'ay')
        elif words[i][0:2] in consonant_sound:
            if words[i][2] == 'y':
                pig_latin.append(words[i][2:] + words[i][0:2] + 'ay')
            elif words[i][0:2] == 'qu':
                pig_latin.append(words[i][4:] + words[i][0:4] + 'ay')
            else:
                pig_latin.append(words[i][2:] + words[i][0:2] + 'ay')
        else:
            consonant_count = 0
            while words[i][consonant_count] in consonants and words[i][consonant_count] != 'y' and consonant_count < len(words[i])-1:
                consonant_count += 1
            
            print(consonant_count)
            print(words[i][consonant_count])
            if words[i][consonant_count-1:consonant_count+1] == 'qu':
                pig_latin.append(words[i][consonant_count+1:] + words[i][0:consonant_count+1] + 'ay')
            elif words[i][consonant_count] == 'y':
                if consonant_count == 0:
                    pig_latin.append(words[i][consonant_count+1:] + words[i][0:consonant_count+1] + 'ay')
                else:
                    pig_latin.append(words[i][consonant_count:] + words[i][0:consonant_count] + 'ay')
            else:
                pig_latin.append(words[i][consonant_count:] + words[i][0:consonant_count] + 'ay')

    print(pig_latin)
    if len(pig_latin) > 1:
        resp = " ".join(pig_latin)
    else:
        resp = pig_latin[0]
    return resp


#print(translate("thrush"))

print(translate("yellow"))
print(translate("may"))
print(translate("rhythm"))
