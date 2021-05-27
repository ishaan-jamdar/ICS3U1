def hyp (a,b):
    'hyp (a,b) - returns the hypotenuse of a right angled triangle using sides A and B'
    c = (((a ** 2) + (b ** 2)) ** 0.5)
    return (c)

a = float(input('what is the length of side A: '))
b = float(input('what is the length of side B: '))

print (hyp(a,b))
