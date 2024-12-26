"""Write a function that accepts two strings and returns the indices of all the occurences of the second string in the first string as a list. If the second string is not present in the first then it should return -1"""
def find_substring_indices(main_string, substring):
    indices = []
    start = 0

    while True:
        start = main_string.find(substring, start)
        if start == -1:
            break

        indices.append(start)
        start += 1  
    
    return indices if indices else -1

# Example
main_string = "hello world"
substring = "hello python"
result = find_substring_indices(main_string, substring)
print(result)

 