header = 'First Name,Count\n'
docs = ['2000_BoysNames.txt','2000_GirlsNames.txt']
x = 1
for doc in docs:
    opFile = open(doc)
    if(x==1):
        newCsv = open('2000_BoysNames.csv','w')
    else:
        newCsv = open('2000_GirlsNames.csv','w')
    newCsv.write(header)
    for line in opFile:
        lineStr = line.split()
        lineStr = lineStr[0]+','+lineStr[1]+'\n'
        newCsv.write(lineStr)
    opFile.close()
    newCsv.close()
    x += 1
