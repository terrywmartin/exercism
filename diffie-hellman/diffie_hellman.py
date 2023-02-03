import random
def private_key(p):
    random.seed()
    return random.randrange(2, p)


def public_key(p, g, private):
    return (g ** private) % p

def secret(p, public, private):
    return (public ** private) % p
