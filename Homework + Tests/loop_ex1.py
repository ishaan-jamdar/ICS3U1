import random
numb=random.randint(0,101)

print ("Can you guess the number between 0 and 100?" + '\n')

while True:
    guess=int(input("Enter your guess: "))
    
    if guess > 100 or guess < 0:
        print ("This number is not between 0 and 100!")
    elif guess > numb:
        print ("Your guess is too high!")
    elif guess < numb:
        print ("Your guess is too low!")
    else:
        print ("Nice, you guessed the number right!")
        break
