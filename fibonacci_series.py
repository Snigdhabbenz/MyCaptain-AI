#Fibonacci Series

n=int(input("Enter the no of values"))
a = 0
b = 1
i = 0
if n < 0:
    print("Enter a valid number")
else:
    while i <= n:
        c = a + b
        a = b 
        b = c
       
        print(a)
        i += 1
