numb = int(input('Enter a number: '))
numbdiv = 1

print ('The divisors are: ')

for i in range(numb):
    if numb % numbdiv == 0:
           print (numbdiv, end = ' ')
    numbdiv += 1
