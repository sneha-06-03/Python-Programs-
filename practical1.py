"""WAP to find the roots of a quadratic equation"""
a,b,c = eval(input("Enter Value(seperated by commas):"))
d= b**2-4*a*c
r1 = (-b+(d)**0.5)/2*a
r2 = (-b-(d)**0.5)/2*a
if d >= 0:
    print("Roots are real:", r1,r2)
else:
    print("Roots are not real")
