# 1) A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount.

salary = int(input("Enter your salary: "))
years = int(input("Enter the number of years you worked in this company: "))

if years >= 5:
    salary = salary * 12
    bonus = (years * salary) / 100 * 5
    print("Your net bonus is: " + str(bonus)) 
else:
    print("You not eligible for the bonus")

# 2) Write a program to check whether a person is eligible for voting or not. (accept age from user) if age is greater than 17 eligible otherwise not eligible

age = int(input("Enter your age: "));

if age >= 18:
    print("You are eligible for voting")
else:
    print("You are not eligible for voting")

# 3) Write a program to check whether a number entered by user is even or odd.
    
num = int(input("Enter any number: "))

if num % 2 == 0:
    print("Your number is even")
else:
    print("Your number is odd")

# 4) Write a program to check whether a number is divisible by 7 or not. Show Answer

num = int(input("Enter any number: "))

if num % 7 == 0:
    print("Your number is divisible by seven")
else:
    print("Your number is not divisible by seven")

# 5) Write a program to display "Hello" if a number entered by user is a multiple of five , otherwise print "Bye"
    
num = int(input("Enter any number: "))

if num % 5 == 0:
    print("Hello")
else:
    print("Bye")
    
# 7) Write a program to display the last digit of a number
    
num = int(input("Enter any number: "))

print(num % 10)

# Q8. Write a program to check whether the last digit of a number( entered by user ) is divisible by 3 or not.

num = int(input("Enter any number: "))

if (num % 10) % 3 == 0:
    print("Your number is divisible by three")
else:
    print("Your number is not divisible by three")

# 9) Take values of length and breadth of a rectangle from user and print if it is square or rectangle.

length = int(input("Enter the length of a rectangle: "))
breadth = int(input("Enter the breadth of a rectangle: "))

if length == breadth:
    print("It is a square")
else:
    print("It is a rectangle")

# 10) Take two int values from user and print greatest among them.

num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))

if num1 > num2:
    print("Number1 (" + str(num1) + ") is greater than Number2 (" + str(num2) + ")")
elif num1 == num2:
    print("Both numbers are equal")
else:
    print("Number2 (" + str(num2) + ") is greater than Number1 (" + str(num1) + ")")

# 11) A shop will give discount of 10% if the cost of purchased quantity is more than 1000. Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user.
    
quantity = int(input("Enter the quantity of units you purchased: "))
total = quantity * 100

if quantity >= 10:
    total = total - total / 10

print("This is the total cost of your purchase: " + str(total))

# 12) A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.

marks = int(input("Enter your marks: "))

if marks < 25:
    print("Your Grade is F")
elif marks >= 25 and marks < 45:
    print("Your Grade is E")
elif marks >= 45 and marks < 50:
    print("Your Grade is D")
elif marks >= 50 and marks < 60:
    print("Your Grade is C")
elif marks >= 60 and marks < 80:
    print("Your Grade is B")
else:
    print("Your Grade is A")

# 