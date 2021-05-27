#OPTION 3
#empty list to hold 
marklist = []

#function to find avg of list
def markAvgMean(numlist, listcount = 0, marktotal = 0, newlist = []):
    """markAvgMean (numlist) - returns average as a floating point value of prameter numlist"""
    #adds only the top 6 marks to the new list
    for i in range(6):
        newlist.append(max(numlist))
        marklist.remove(max(numlist))
    #finds the total value and number of variables in list
    for i in newlist:
        listcount += 1
        marktotal += float(i)
    return(float(marktotal/listcount))

#conditional loop used to take input of the marks, you can enter as many as you want until -1 is entered, if it above 100 or less than -2 the input will not be counted
while True:
    markinput = float(input('enter a mark(-1 to exit): '))
    if markinput == -1:
        break
    elif markinput >= 101 or markinput <= -2:
        print('invalid input')
    else:
        #appends this new value to the list
        marklist.append(markinput)

#prints the average of the top 6 marks using function
print ('The average of your top 6 marks is' + str(markAvgMean(marklist)))
