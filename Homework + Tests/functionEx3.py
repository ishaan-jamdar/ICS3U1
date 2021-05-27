def persistance(num,pers=0):
    """persistance(num) - returns the persistance of parameter num"""
    
    Npers = 1
    if num < 10 and num > -10:
        #we return 0 since the number would already be in a single digit meaning it takes 0 steps
        return pers
    
    #this loop continues until the number is 0
    while num > 0 or num < 0:
        
        #gives the digit in the ones column
        ones = num % 10
        
        #the multiplication of the numbers occurs here
        Npers = Npers * ones
        
        #uses integer division to divide the number by 10(getting rid of the ones digit) and still be left with a whole number
        num = num // 10
        
    #this is when the funtion is finally complete and can print the final persistance number
    if Npers < 10 and Npers > -10:
        return pers + 1
    
    #however if the number is still not at a single digit form we will use recursion to go through the function again while adding to our persistance count, this will occur as many times as needed
    else:
        num = Npers
        return persistance(num,pers+1)

number = int(input('Enter a number: '))
print ('The persistance is ', str(persistance(number)))
        

    
        
