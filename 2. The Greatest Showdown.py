# Objective:
# Harness the power of conditional statements to compare and determine values.

# Task 1: Identify the Greatest
# Write a Python program that prompts the user to enter three numbers. The program should then identify and print out the largest number among the three.
number_1=input("Enter your number")
number_2=input("Enter your number")
number_3=input("Enter your number")
print(max(number_1,number_2,number_3));
# Task 2: Identify the Smallest
# Extend your program from Task 1 to also determine the smallest number among the three and print it out.
number_1=input("Enter your number")
number_2=input("Enter your number")
number_3=input("Enter your number")
print(min(number_1,number_2,number_3));
# Task 3: Equality Check
# Enhance your program to handle cases where two or all of the numbers are equal. The program should display appropriate messages like "Two numbers are equal and the largest" or "All numbers are equal".

# Expected Outcome: If we provide the numbers 3, 3, and 4, it should print out that "The smallest number is 3. The largest number is 4. There are two numbers equal to each other." Printing out which numbers are equal would be a great added bonus.

number_1=input("Enter your number")
number_2=input("Enter your number")
number_3=input("Enter your number")
smallest=min(number_1,number_2,number_3)
largest= max(number_1,number_2,number_3)

if number_1==number_2==number_3:
    print("All numbers are equal")
elif number_1==number_2:
    print(f"The smallest number is {smallest}. The largest number is {largest}. There are two numbers equal to each other: {number_1}")
elif number_2==number_3:
    print(f"The smallest number is {smallest}. The largest number is {largest}. There are two numbers equal to each other: {number_2}")
elif number_1==number_3:
    print(f"The smallest number is {smallest}. The largest number is {largest}. There are two numbers equal to each other: {number_3}")
else:
    print(f"The smallest number is {smallest}. The largest number is {largest}. No Numbers are equal")