"""WAP to swap the first n characters of two strings"""
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
n = int(input("Enter the number of characters to swap: "))

s1, s2 = s2[:n] + s1[n:], s1[:n] + s2[n:]
print("First string:", s1)
print("Second string:", s2)
