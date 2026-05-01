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
