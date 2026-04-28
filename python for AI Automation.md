# Python for AI Automation

## 1. Variables

- Variables store values under a name.
- Python is dynamically typed, so you do not declare variable types explicitly.

Example:
```python
name = "Alice"
age = 30
price = 19.99
is_active = True
```

Key points:
- Use `=` to assign values.
- Variable names can contain letters, numbers, and underscores.
- Variable names cannot start with a number.
- Variable names are case-sensitive.

Example with math operations:
```python
a = 10
b = 3
sum_value = a + b
product = a * b
division = a / b      # float result
integer_div = a // b  # integer division
remainder = a % b
power = a ** b
```

## 2. Loops

Python has two main loop types: `for` and `while`.

### `for` loop
Used to iterate over items in a sequence such as a list, tuple, or string.

Example:
```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
	print(fruit)
```

Iterating over a range:
```python
for i in range(5):
	print(i)   # prints 0, 1, 2, 3, 4
```

`range(start, stop[, step])` examples:
- `range(1, 6)` → 1..5
- `range(0, 10, 2)` → 0, 2, 4, 6, 8

### `while` loop
Runs until a condition becomes false.

Example:
```python
count = 0
while count < 5:
	print(count)
	count += 1
```

Example with countdown:
```python
n = 10
while n > 0:
	print(n)
	n -= 1
```

### Loop control statements
- `break` exits the loop early.
- `continue` skips the current iteration.

Example:
```python
for number in range(1, 10):
	if number == 5:
		break
	if number % 2 == 0:
		continue
	print(number)
```

## 3. Functions

Functions package reusable code and help organize logic.

### Defining a function
Use `def` to define a function, then use `return` to provide a result.

Example:
```python
def greet(name):
	return f"Hello, {name}!"

message = greet("Alice")
print(message)
```

### Function with multiple parameters
```python
def add(a, b):
	return a + b

result = add(4, 7)
print(result)
```

### Default parameters
```python
def greet(name="Guest"):
	print(f"Hello, {name}!")

greet()          # Hello, Guest!
greet("Maria")   # Hello, Maria!
```

### Functions without a return value
If no `return` statement is present, the function returns `None`.

Example:
```python
def show_message(text):
	print(text)

result = show_message("Hi")
print(result)   # prints None
```

### Combined example: variables, loops, and functions
```python
def square_numbers(numbers):
	squared = []
	for value in numbers:
		squared.append(value ** 2)
	return squared

data = [1, 2, 3, 4]
squares = square_numbers(data)

for value, square in zip(data, squares):
	print(value, "->", square)
```

## 4. Practical tips
- Use descriptive names: `total_price`, `user_count`, `is_valid`.
- Keep functions short and focused.
- Use loops to process lists, strings, or other collections.
- Test functions with different inputs.

## 5. Suggested next practice steps
1. Write a script that uses variables to store user data.
2. Loop over a list of items and print each item with a message.
3. Create functions to calculate totals, averages, or transformed values.
4. Combine all three concepts into a single small program.

## Exercises
1. Create a variable for a user's name, age, and favorite language. Print a sentence using all three.
2. Use a `for` loop to iterate over a list of five programming languages and print each one with its index.
3. Write a `while` loop that counts down from 5 to 1 and prints `Blast off!` after the loop ends.
4. Build a function named `calculate_area(width, height)` that returns the area of a rectangle, then call it with sample values.
5. Create a function that takes a list of numbers and returns a new list with each number doubled. Print the result.
