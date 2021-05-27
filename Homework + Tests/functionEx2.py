def knightMove(row,col):
    """knightMove(row,col) - returns all potential moves of a knight in chess from parameters row and col"""
    #creates a new list where the potential moves will be stored
    moveList = []
    
    #creates 2 tuples with every number corresponding to every possible move a knight can make
    rowM = (1, 1, 2, 2, -1, -1, -2, -2)
    colM = (2, -2, 1, -1, 2, -2, 1, -1)
    
    #creates a list of the letters that will be used when getting final position
    letters = ['r','r','A','B','C','D','E','F','G','H','r','r']
    
    #capitalizes the inputted column letter and assigns it a number based on the index position in the list
    col = col.capitalize()
    col = letters.index(col)
    
    #rci is the variable used to increase the index position in our loop allowing us to go through each calculation
    rci = 0
    
    #we use a counted loop in a range of 8 as that is the total number of moves we will be calculating
    for i in range(8):
        
        #calculates the row and column position after each move occurs
        rowN = row + rowM[rci]
        colN = col + colM[rci]
        
        #checks to see if the final calculations are within the board range and do not go off the board
        if 0 < rowN < 9 and 1 < colN < 10:
            
            #converts the column number to the corresponding letter in the list and puts both row and column in a tuple which is then appended in to our final list
            pos = (rowN, letters[colN])
            moveList.append(pos)
            
        #increases the counted index by 1 for the next calculation
        rci += 1
        
    return moveList
        
row = int(input('What row is the knight in? '))
col = input('What column is the knight in?(A - H) ')

print (knightMove(row,col))
