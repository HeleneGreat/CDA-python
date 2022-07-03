from inspect import _void

"""
EN This script displays some song's lyrics according to the number chosen by the user
"""
def main()->_void:
    nb = input("Nombre de bolées désirées :")
    isInt:bool = check_user_input(nb)
    if isInt:
        song:tuple = getSong(int(nb))
        partOne:str = song[0]
        partTwo:str = song[1]
        print(partOne)
        print(partTwo)


"""
EN Checks if the user entered a valid parameter : if it can be typed as an int between 0 and 99, it is valid
@param str
@return bool
"""
def check_user_input(nb:str):
    # In case no number is entered
    if nb == "":
        print("Si tu ne renseigne pas de quantité, je ne peux pas chanter !")
        return False
    else:
        # It is an int
        try:
            value = int(nb)
            # If the number is within 0 and 99
            if value >= 0 and value <= 99:
                return True
            else:
                print("La quantité doit être comprise entre 0 et 99.")
                return False
        # It is not an int
        except ValueError:
            print("La quantité doit être un entier compris entre 0 et 99")
            return False

 
"""
EN Gets the lyrics of the song
@param int
@return tuple[str]
"""
def getSong(nb:int)->str:
    # If the number entered is between 1 and 99 included
    if nb > 0 and nb <= 99:
        partOne:str = songPartOne(nb)
        partTwo:str = songPartTwo(nb - 1)
    # If the number if zero, the song is different
    elif nb == 0:
        partOne:str = "Plus de bolées de cidre sur le mur, plus de bolées sans alcool."
        partTwo:str = "Vas au supermarché pour en acheter, 99 bolées de cidre sur le mur."
    return partOne, partTwo


"""
EN Gets the first line of the song
@param int
@return str
"""
def songPartOne(nb:int)->str:
    accord:str = plural(nb)
    if(nb == 0):
        nb:str = "plus de"
    return str(nb) + " bolée" + accord + " de cidre sur le mur, " + str(nb) + " bolée" + accord + " sans alcool."


"""
EN Gets the second line of the song
@param int
@return str
"""
def songPartTwo(newNb:int)->str:
    accord:str = plural(newNb)
    if(newNb == 0):
        newNb:str = "Plus de"
    return "Bois en un et au suivant ! " + str(newNb) + " bolée" + accord + " de cidre sur le mur."


"""
EN Gets whether the word "bolée" is plural or singular
@param int
@return str
"""
def plural(number:int):
    accord:str = ""
    if(number > 1 or number == 0):
        accord = "s"
    return accord




main()