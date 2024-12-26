"""WAP to create a pyramid of "*" and it's reverse pyramid"""
def pyramid(height):
    for i in range(1, height + 1):
        print(' ' * (height - i) + '*' * (2 * i - 1))

def reverse_pyramid(height):
    for i in range(height, 0, -1):
        print(' ' * (height - i) + '*' * (2 * i - 1))

height = int(input("Enter the height of the pyramid: "))
pyramid(height)
reverse_pyramid(height)
