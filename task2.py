fileName = input('Please enter the name of the .csv file: ')
try:
    opFile = open(fileName + '.csv')
    for line in opFile:
        print(line)
except:
    print('Something went wrong!')