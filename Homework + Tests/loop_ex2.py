numb=int(input("Enter a number: "))

fib1=0
fib2=1

for i in range(numb):
    print (fib1, end=' ')

    fib3 = fib1 + fib2
    fib1 = fib2
    fib2 = fib3


