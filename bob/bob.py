def response(hey_bob):
    txt = hey_bob.strip()
    if txt[-1:] == '?':
        if txt.isupper():
            return "Calm down, I know what I'm doing!"
        else:
            return 'Sure.'
    if txt.isupper():
        return 'Whoa, chill out!'

    if txt == "":
        return 'Fine. Be that way!'

    return 'Whatever.'

