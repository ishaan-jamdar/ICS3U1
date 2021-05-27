#OPTION 3
marklist = []

def markAvgMean(numlist, listcount = 0, marktotal = 0, newlist = []):
    """markAvgMean (numlist) - returns average as a floating point value of prameter numlist"""
    for i in range(6):
        newlist.append(max(numlist))
        marklist.remove(max(numlist))
    for i in newlist:
        listcount += 1
        marktotal += float(i)
    return(float(marktotal/listcount))

while True:
    markinput = float(input('enter a mark(-1 to exit): '))
    if markinput == -1:
        break
    elif markinput >= 101 or markinput <= -2:
        print('invalid input')
    else:
        marklist.append(markinput)

print (markAvgMean(marklist))
