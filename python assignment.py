# 1) Write a Python program that simulates a basic calculator, performing addition, subtraction,multiplication, and division.
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

if b != 0:
    print("Division:", a / b)
else:
    print("Cannot divide by zero")

# 2) Write a Python program that converts a given decimal number to its binary equivalent.
num = int(input("Enter a decimal number: "))
print("Binary equivalent:", bin(num)[2:])

# 3) Write a Python program that asks for the user's age and then prints a message stating whether
# the user is a minor, an adult, or a senior.
age = int(input("Enter your age: "))

if age < 18:
    print("You are a minor")
elif age < 60:
    print("You are an adult")
else:
    print("You are a senior")


# 4) Write a Python program to swap the values of two variables without using a third variable.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a, b = b, a

print("After swap, a =", a, "b =", b)

# 5) Write a Python program to print the first 10 numbers of the Fibonacci series.
a, b = 0, 1
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b
print()

# 6) Write a Python program to check if a given number is prime or not.
num = int(input("Enter number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")

# 7) Write a Python program that takes three numbers as input and checks if the third number is the
# sum of the first two numbers using logical operators.
a = int(input("First number: "))
b = int(input("Second number: "))
c = int(input("Third number: "))

if c == a + b:
    print("Third number is sum of first two")
else:
    print("It is not")

# 8) Write a Python program that imports a custom module you created with a function that returns
# the factorial of a number.

import factorial_module

num = int(input("Enter number: "))
print("Factorial:", factorial_module.factorial(num))

# 9) Write a Python program that takes two numbers as input and performs division, handling the
# case where the divisor is zero.
a = float(input("Enter numerator: "))
b = float(input("Enter denominator: "))

if b != 0:
    print("Result:", a / b)
else:
    print("Cannot divide by zero")

# 10) Write a Python function that takes a list of numbers and returns the maximum value in the list.
def find_max(nums):
    return max(nums)

print(find_max([3, 7, 2, 9, 1]))

# 11) Write a Python function that takes a name and an optional age parameter and prints a greeting.
# If the age is not provided, it should default to 25.
def greet(name, age=25):
    print(f"Hello {name}, you are {age} years old")

greet("Alice")
greet("Bob", 30)

# 12) Write a Python program to count the number of vowels in a given string.
s = input("Enter a string: ").lower()
vowels = "aeiou"
count = sum(1 for char in s if char in vowels)
print("Number of vowels:", count)


# 13) Write a Python program that prints a multiplication table up to (numberx10).
num = int(input("Enter number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# 14) Write a Python program to print a right-angled triangle of '*' with a given number of rows.
rows = int(input("Enter rows: "))
for i in range(1, rows + 1):
    print('*' * i)

# 15) Write a Python program to print a pyramid of '*' with a given number of rows.
rows = int(input("Enter rows: "))
for i in range(rows):
    print(' ' * (rows - i - 1) + '*' * (2 * i + 1))

#set B
    
# 1) Given an integer x, return true if x is a palindrome, and false otherwise. (LeetCode: Palindrome Number)
x = int(input("Enter number: "))
if str(x) == str(x)[::-1]:
    print(True)
else:
    print(False)

# 2) Given a non-empty array of integers nums, every element appears twice except for one. Find that single one. (LeetCode: Single Number)
nums = [4, 1, 2, 1, 2]
result = 0
for num in nums:
    result ^= num
print("Single Number:", result)

# 3) Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. (LeetCode: Two Sum)
nums = [2, 7, 11, 15]
target = 9
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print([i, j])

# 4) Write an algorithm to determine if a number n is happy. (LeetCode: Happy Number)
def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(ch) ** 2 for ch in str(n))
    return n == 1

print(is_happy(19))

# 5) Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct. (LeetCode: Contains Duplicate)
nums = [1, 2, 3, 1]
if len(nums) != len(set(nums)):
    print(True)
else:
    print(False)