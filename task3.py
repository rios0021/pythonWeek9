import rios0021Library
# Function that creates a dictionary from file font3.txt
# Input: none
# Output: returns a dictionary
def generateDictionary():
    try:
        opFile = open('font3.txt','r')
        valuesDictionary = dict()
        # Loop through each line in the file
        for line in opFile:
            binList=[]
            # Separate values from each line with the comma
            auxList = line.split(',')
            # Assign values to descriptive variables
            baseNo = auxList[0][2:]
            keyChar = auxList[1].rstrip()
            # Transform hex to bin and fill the zeroes at the start if removed
            binNumber = bin(int(baseNo,16))[2:].zfill(64)
            # Loop 8 times to split the bin number and create the list of lists
            for i in range(1,9):
                aux = (i*8)
                binList.append(list(binNumber[aux-8:aux]))
            # Assign the key and list of lists to the dictionary
            valuesDictionary[keyChar] = binList
        opFile.close()
        return valuesDictionary
    except:
        print('Function generateDictionary failed')
newDictionary = generateDictionary()
askChar = input('Please enter a character to display in the gfxhat: ')
try:
    rios0021Library.clearScreen()
    rios0021Library.clearBacklight()
    rios0021Library.randomLedColor()
    rios0021Library.displayObject(newDictionary[askChar], 60,30)
except:
    print('Something went wrong with displayObject')