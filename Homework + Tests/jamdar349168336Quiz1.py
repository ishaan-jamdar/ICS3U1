size=int(input("enter size :"))
txt=input("enter text :")
txt2 = ' ' + txt + ' '
txtlen = txt2.count('')
txtblank = str(' ' * txtlen)

print ("X" * size)\n * ((size/2)-2)
print (txtlen.center(size,"X"))
print (txt2.center(size,"X"))
print (txtlen.center(size,"X"))
print ("X" * size)\n * ((size/2)-2)
