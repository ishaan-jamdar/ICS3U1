print ("Please use this program to determine the total cost for your visit to the Ontario Science Centre." + '\n')

age=int(input("How old are you? "))
sid=input("Do you have a student ID? Yes/No? ").capitalize()
member=input("Do you have a membership to the Science Centre? Yes/No? ").capitalize()
sci=input("Are you going to enter the Science Centre? Yes/No? ").capitalize()
imax=input("Are you going to watch the IMAX film? Yes/No? ").capitalize()
prk=int(input("How many vehicles are you going to be parking? "))
prkp=prk*10
lock=int(input("How many lockers will you be renting? "))

if age <= 3 or member == 'Yes' and imax == 'No':
    price = 0

elif imax == 'Yes' and sci == 'No' or member == 'Yes' and imax == 'Yes':
    price = 9

elif age <=12:
    if sci == 'Yes':
        price = 13
        if imax == 'Yes':
            price = 19

elif age <= 17 or age >= 65 or sid == 'Yes':
    if sci == 'Yes':
        price = 16
        if imax == 'Yes':
            price = 22

elif age <= 64:
    if sci == 'Yes':
        price = 22
        if imax == 'Yes':
            price = 28

finalp = str(price + prkp + lock)

print ('\n' + "Your total cost will be $" + finalp + " Canadian dollars! (HST included)")
