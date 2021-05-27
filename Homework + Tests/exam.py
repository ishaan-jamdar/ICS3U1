i = 0
s = 'supercalifragilisticexpialidocious'
while i < len(s):
    if s[i] == 'a':
        print (i * s[i])
    elif s[i] == 'e':
        print ('ae' * i)
    else:
        print (s[i])
