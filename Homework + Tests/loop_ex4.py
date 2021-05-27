psword = input('Enter a new password (Password requires 1 capital letter, 1 number, and no characters but letters, numbers, and underscores): ')
up = 0
no = 0
usco = 0
usc = '_'

for i in psword:
    if i.isupper():
        up = 1

    elif i.isdigit():
        no = 1

    elif i in usc:
        usco = 1

        if up == 1 and no == 1 or up == 1 and no == 1 and usco == 1:
            continue

        else:

       
print ('your password is compatible')

