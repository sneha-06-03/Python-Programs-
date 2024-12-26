""" WAP to create a list of the cubes of only the even integers appearing in the input list (may have elements of other types also) using the following:(a) 'for' loop. """

input_list = [1, 2, 'hello', 4, 5, 6, 8, 9.5, 10]
even_cubes = []

for element in input_list:
    if isinstance(element, int) and element % 2 == 0:
        even_cubes.append(element ** 3)

print(even_cubes)
