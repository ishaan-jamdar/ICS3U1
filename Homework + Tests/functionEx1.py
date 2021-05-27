def palindrome(a):
    """palindrome(a) - checks whether parameter a is a palindrome or not"""
    
    #removes all spaces from the string so that you can check for palindrome sentences as well
    b = a.lower().replace (" ", "")
    
    #checks if the input is equivalent to the reverse input and dependant on this factor returns true or false
    if b == b[::-1]:
        
        return ("True")
    return ("False")

while True:
    pal = input("Enter a string to check if it is a palindrome: ")

    print (palindrome(pal))
