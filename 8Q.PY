# Program to create a dictionary of odd numbers and their cubes

# Input list
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Dictionary comprehension for odd numbers and their cubes
odd_cubes = {num: num**3 for num in numbers if num % 2 != 0}

# Output
print("Output Dictionary:", odd_cubes)
