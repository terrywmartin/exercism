import math
def score(x, y):
    
    d = math.sqrt((((0 - x) ** 2) + (0 - y) ** 2))
    print(d)
    if d > 10:
        return 0
    if 5 < d <= 10:
        return 1
    if 1 < d <= 5:
        return 5
    else:
        return 10



