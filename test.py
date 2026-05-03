# Script to store user data in variables

user_name = "John Doe"
user_age = 28
user_email = "john.doe@example.com"

print("User Information:")
print("Name:", user_name)
print("Age:", user_age)
print("Email:", user_email)

# Loop over a list of items and print each one with a message
items = ["apple", "banana", "cherry"]

for item in items:
	print(f"Item found: {item}")

# Functions to calculate totals, averages, or transformed values

def calculate_total(numbers):
	total = 0
	for num in numbers:
		total += num
	return total

def calculate_average(numbers):
	if len(numbers) == 0:
		return 0
	total = calculate_total(numbers)
	return total / len(numbers)

def transform_values(numbers):
	transformed = []
	for num in numbers:
		transformed.append(num ** 2)  # Square each number
	return transformed

# Example usage
data = [1, 2, 3, 4, 5]
print("Total:", calculate_total(data))
print("Average:", calculate_average(data))
print("Transformed:", transform_values(data))


calculate_average(data)

def square(number):
    return number * number

square(125)

# Real-world application example of lists & dictionaries (sorting a list of fruits into bins based on type)✅
fruit_basket = ['apple', 'banana', 'cherry', 'date', 'eggplant']  
type_to_bin = {'fruit': [], 'vegetable': []}  
for fruit in my_list: 
    if fruit in type_to_bin.keys(): # Checking dictionary keys for item placement (avoid KeyError)
        type_to_bin[fruit].append(fruit)
print("Fruits are placed into 'fruit' bin.")  
for veggie in my_list: 
    if veggie in type_to_bin.keys(): # Same key-check for vegetable placement (avoid KeyError again)
        type_to_bin[veggie].append(veggie)
print("Vegetables are placed into 'vegetable' bin.")  

