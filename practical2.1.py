"""Wap to accept a number 'n' and check if 'n' is prime"""
n = eval(input("Enter value:"))
if n>1:
    for i in range(2,n):
      if n%i == 0:
        print(n,"not a prime number")
        break
    else:
       print(n, "prime number")
else:
   print(n,"not a prime number")

