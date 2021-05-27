#the variable "fruits" represents the 5 fruits I chose in a list format
fruits = ['Apples','Bananas','Oranges','Plums','Mangoes']

#this uses a counted loop in order to print each of the fruits in the list
for i in fruits:
    print (i)

#EXTENSION A
print ('\n')

#this replaces the second fruit in the list (Bananas) with "Watermelons"
#the reason it replaces index position 1 instead of 2 is because the first index position is considered as 0
fruits[1] = 'Watermelons'

for i in fruits:
    print (i)
