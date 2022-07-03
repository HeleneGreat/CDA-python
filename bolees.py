from inspect import _void


# TODO : ADD nb as argument of the command line
def main()->_void:
    nb = 55
    song = getSong(nb)
    partOne = song[0]
    partTwo = song[1]
    print(partOne)
    print(partTwo)

 
"""
EN 
@param str or int
@return tuple[str]
"""
def getSong(nb)->str:
    # In case no number is entered
    if nb == "":
        partOne:str = "Si tu ne renseigne pas de quantité, je ne peux pas chanter !"
        partTwo:str = ""
    # If the number entered is between 0 and 99 included
    elif nb > 0 and nb <= 99:
        partOne:str = songPartOne(nb)
        partTwo:str = songPartTwo(nb - 1)
    # If the number if zero, the song is different
    elif nb == 0:
        partOne:str = "Plus de bolées de cidre sur le mur, plus de bolées sans alcool."
        partTwo:str = "Vas au supermarché pour en acheter, 99 bolées de cidre sur le mur."
    # If the number is not within 0 and 99
    elif nb < 0 or nb > 99:
        partOne:str = "La quantité doit être comprise entre 0 et 99."
        partTwo:str = ""
    return partOne, partTwo


"""
EN 
@param int
@return str
"""
# First line of the song
def songPartOne(nb:int)->str:
    accord:str = plural(nb)
    if(nb == 0):
        nb:str = "plus de"
    return str(nb) + " bolée" + accord + " de cidre sur le mur, " + str(nb) + " bolée" + accord + " sans alcool."


"""
EN 
@param int
@return str
"""
# Second line of the song
def songPartTwo(newNb:int)->str:
    accord:str = plural(newNb)
    if(newNb == 0):
        newNb:str = "Plus de"
    return "Bois en un et au suivant ! " + str(newNb) + " bolée" + accord + " de cidre sur le mur."


"""
EN 
@param int
@return str
"""
# Decides whether the word "bolée" is plural or singular
def plural(number:int):
    accord:str = ""
    if(number > 1 or number == 0):
        accord = "s"
    return accord




main()