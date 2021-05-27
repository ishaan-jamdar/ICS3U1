print ('Please use this program to vote in the election.' + '\n' + '1. Donald Trump' + '\n' + '2. Justin Trudeau' + '\n' + '3. Arnold Schwarzenegger')

trump = 0
trudeau = 0
arnold = 0

while True:
    vote = int(input('Enter Vote(0 to exit):'))
    if vote == 0:
        break

    elif vote == 1:
        trump += 1

    elif vote == 2:
        trudeau += 1

    elif vote == 3:
        arnold += 1

    else:
        print ('Invalid input')

totalvote = trump + trudeau + arnold

if trump > trudeau and trump > arnold:
    print ('Donald Trump won')

elif trudeau > trump and trudeau > arnold:
    print ('Justin Trudeau won')

elif arnold > trump and arnold > trudeau:
    print ('Arnold Schwarzenegger won')

else:
    print ('There was a draw!!!')

print ('Donald Trump earned ' + str((trump/totalvote)*100) + '% of the votes')
print ('Justin Trudeau earned ' + str((trudeau/totalvote)*100) + '% of the votes')
print ('Arnold Schwarzenegger earned ' + str((arnold/totalvote)*100) + '% of the votes')
