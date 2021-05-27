#creates an empty list where the inputs will be stored
gradelist = []

#creates a counted loop to get 10 of the grade inputs(in float incase of decimals) and adds them in to the empty list
for i in range(10):
    gradeinput = float(input('Enter each grade: '))
    gradelist.append(gradeinput)

#prints the list
print ('this is your list of grades', gradelist)

#EXTENSION A
#sorts list in ascending order
gradelist.sort()

#prints the list on a new line
print ('\nthis is your list of grades in ascending order', gradelist)

#EXTENSION B
#sorts list in descending order, can use reverse since already in ascending order
gradelist.reverse

#prints the list on a new line
print ('\nthis is your list of grades in descending order', gradelist)

#EXTENSION C
#creates a variable for the total sum of all the integers
avg = 0

#uses a counted loop to add each integer from the list together
for i in gradelist:
    avg += i

#prints the average of the list
print ('\nthis is the average of your list', (avg/10))

#EXTENSION D
#creates the empty lists where grades and courses will be stored
gradelist2 = []
courselist = []

#uses a counted loop to get the 10 grades and courses and input them in the list
for i in range(10):
    courseinput = input('Enter your course: ')
    courselist.append(courseinput)
    gradeinput2 = float(input('Enter the grade: '))
    gradelist2.append(gradeinput2)

#prints each course in the list along with the mark of that course
for i in range(10):
    print (courselist[i], '=', gradelist2[i])

#prints the average of the newly inputted marks
print ('The average of your grades is ', (sum(gradelist2))/10)

    
    
