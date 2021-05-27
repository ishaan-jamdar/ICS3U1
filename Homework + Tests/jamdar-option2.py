#OPTION 2
#variables list empty list, list count and mark total
marklist = []
listcount = 0
marktotal = 0
m49 = 0
m59 = 0
m69 = 0
m79 = 0
m100 = 0

#function that takes a mark and sorts it into a group depending on what the mark is
def marksorter(i):
    """marksorter (i) - returns parameter i sorted into a mark based group"""
    if i <= 49:
        return(49)
    elif i <= 59:
        return(59)
    elif i <= 69:
        return(69)
    elif i <= 79:
        return(79)
    elif i <= 100:
        return(100)

#conditional loop used to get mark inputs
while True:
    markinput = float(input('enter a mark(-1 to exit): '))
    #if -1 entered breaks loop
    if markinput == -1:
        break
    #if a number out of marks range is entered does not count
    elif markinput >= 101 or markinput <= -2:
        print('invalid input')
    #adds new value to the list
    else:
        marklist.append(markinput)

#counted loop used to find the average of the list
for i in marklist:
    listcount += 1
    marktotal += float(i)
markmedian = (float(marktotal/listcount))

#counted loop to count how many of each number goes into each group
for i in marklist:
    marksort = marksorter(i)
    if marksort == 49:
        m49 += 1
    if marksort == 59:
        m59 += 1
    if marksort == 69:
        m69 += 1
    if marksort == 79:
        m79 += 1
    if marksort == 100:
        m100 += 1

#prints the graph displaying each mark and how many there are in each also prints median
print('\n0-49   :' + '*' * m49 + '\n50-59  :' + '*' * m59 + '\n60-69  :' + '*' * m69 + '\n70-79  :' + '*' * m79 + '\n80-100 :' + '*' * m100)
print("Average (Mean) " + str(markmedian))
