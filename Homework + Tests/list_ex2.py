#intialize the list with 8 integers
intlist1 = [2, 4, 6, 8, 10, 12, 14, 16]

#multiplies each integer in the original list by 2 while creating a new list with these integers
intlist2 = [i * 2 for i in intlist1]

#prints each integer from the new list on one line
for i in intlist2:
    print (i, end = ' ')

#EXTENSION A
#gets the average of the first list and uses float incase it is a decimal number
avglist1 = float(sum(intlist1)/len(intlist1))

#prints the average of the list on a new line
print ('\n' + 'The average of the 8 original integers is', avglist1)

#EXTENSION B
#gets the average of the second list using the first average
avglist2 = float(avglist1 * 2)

#prints the average of the second list on a new line
print ('The average of the 8 integers multiplied by 2 is', avglist2)
