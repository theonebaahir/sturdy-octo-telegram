input_number = 10

# Create a list of odd numbers up to input_number
odd_numbers1 = [num for num in range(1, input_number + 1) if num % 2 != 0]

# Create another list of odd numbers (same as above for simplicity)
odd_numbers2 = odd_numbers1.copy()

# Create a list of fruits
fruits = ["apple", "banana", "orange", "grape", "mango"]

# Create a new list with the first letter of each fruit capitalized
capitalized_fruits = [fruit.capitalize() for fruit in fruits]

# Print results
print("List of odd numbers up to", input_number, ":", odd_numbers1)
print("Another list of odd numbers:", odd_numbers2)
print("Original fruit list:", fruits)
print("Capitalized fruit list:", capitalized_fruits)