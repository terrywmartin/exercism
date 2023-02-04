
color_bands = [ 'black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white' ]

def label(colors):
    multiplier = color_bands.index(colors[2])
    suffix = [ ' ohms', ' kiloohms', ' megaohms', ' gigaohms']

    bands = str(color_bands.index(colors[0])) + str(color_bands.index(colors[1]))

    resistance = int(bands) * ( 10 ** multiplier)

    if resistance > 1000000000:
        resistance = resistance / (10  ** 9)
        return str(int(resistance)) + " gigaohms"
    
    if resistance > 1000000:
        resistance = resistance / (10  ** 6)
        return str(int(resistance)) + " megaohms"

    if resistance > 1000:
        resistance = resistance / (10  ** 3)
        return str(int(resistance)) + " kiloohms"

    return str(int(resistance)) + " ohms"
