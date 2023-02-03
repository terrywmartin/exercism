def valid_triangle(sides):
    if 0 in sides:
        return False

    if sides[0] + sides[1] < sides[2]:
        return False
    if sides[1] + sides[2] < sides[0]:
        return False
    if sides[0] + sides[2] < sides[1]:
        return False
    return True

def equilateral(sides):
    if not valid_triangle(sides):
        return False
    
    if sides[0] == sides[1] == sides[2]:
        return True
    return False


def isosceles(sides):
    if not valid_triangle(sides):
        return False
    
    if 0 in sides:
        return False
    return bool(len(sides) != len(set(sides)))


def scalene(sides):
    if not valid_triangle(sides):
        return False
    
    if 0 in sides:
        return False
    return bool(len(sides) == len(set(sides))) 

