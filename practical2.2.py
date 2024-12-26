"""WAP to generate all the prime numbers upto n"""
n =int(input("Enter upper value  to print prime numbers n : "))
for a in range(2,n +1):
    k=0
    for i in range(2,a//2+1):
        if(a%i==0):
            k=k+1
    if(k<=0):
        print(a)