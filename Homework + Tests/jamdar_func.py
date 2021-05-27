import random

#defines the boo function along with documentation
def boo(a,b,c):
    '''boo(a,b,c) - sorts parameters a, b, and c by ascending integer value, and returns the middle value'''

    #changes each value to an integer, in the case that they may be a string or a float value
    a = int(a)
    b = int(b)
    c = int(c)

    #using min and max we can make minI become the lowest value and maxI become the largest value
    minI = min(a,b,c)
    maxI = max(a,b,c)

    #subtracting the lowest number and the highest number from the sum of the three will leave us with the middle value as a integer
    return((a + b + c) - minI - maxI)

for i in range (10):
    #randomizes each number
    a = random.randint(1, 101)
    b = random.randint(1, 101)
    c = random.randint(1, 101)

    #prints the middle value from the randomized set
    print ('The middle value is ' + str(boo(a,b,c)))
