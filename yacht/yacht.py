# Score categories.
# Change the values as you see fit.
YACHT = 1
ONES = 2
TWOS = 3
THREES = 4
FOURS = 5
FIVES = 6
SIXES = 7
FULL_HOUSE = 8
FOUR_OF_A_KIND = 9
LITTLE_STRAIGHT = 10
BIG_STRAIGHT = 11
CHOICE = 12


def score(dice, category):
    total = 0
    if category == YACHT:
        if len(set(dice)) == 1:
            return 50
        return 0
    if category == ONES:
        return sum([ x if x == 1 else 0 for x in dice])
    if category == TWOS:
        return sum([ x if x == 2 else 0 for x in dice])
        
    if category == THREES:
        return sum([ x if x == 3 else 0 for x in dice])
        
    if category == FOURS:
        return sum([ x if x == 4 else 0 for x in dice])
        
    if category == FIVES:
        return sum([ x if x == 5 else 0 for x in dice])
        
    if category == SIXES:
        return sum([ x if x == 6 else 0 for x in dice])
        
    if category == FULL_HOUSE:
        count_dice = [ dice.count(x) for x in dice]
        if 3 in count_dice and 2 in count_dice:
            for i in range(0,5):
                if count_dice[i] == 3 or count_dice[i] == 2:
                    total += dice[i]
        return total
    if category == FOUR_OF_A_KIND:
        count_dice = [ dice.count(x) for x in dice]
        if 4 in count_dice:
            for i in range(0,5):
                if count_dice[i] == 4:
                    total += dice[i]
        if 5 in count_dice:
            for i in range(0,4):
                total += dice[i]
        return total
    if category == LITTLE_STRAIGHT:
        if set((1,2,3,4,5)).issubset(set(dice)):
            return 30
        return 0
    if category == BIG_STRAIGHT:
        if set((2,3,4,5,6)).issubset(set(dice)):
            return 30
        return 0
    if category == CHOICE:
        return sum([ x for x in dice])

    return 0

