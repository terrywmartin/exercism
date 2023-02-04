color_bands = [ 'black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white' ]

def value(colors):

    resistance = str(color_bands.index(colors[0])) + str(color_bands.index(colors[1]))

    return int(resistance)
