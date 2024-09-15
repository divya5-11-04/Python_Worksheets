import math
#Write a Python program to print the following string in a specific format (see theoutput). Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are".
print("Twinkle, twinkle, little star,\n How I wonder what you are!\n Up above the world so high,\n Like a diamond in the sky.\nTwinkle, twinkle, little star,\nHow I wonder what you are")

#2. Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
first_name = input("Enter your first name : ")
last_name = input("Enter your last name : ")
print(last_name + " " + first_name) 

#3. Write a Python program that calculates the area of a circle based on the radius entered by the user.
r = float(input("Enter radius : "))
area = 3.14 * r * r 
print(area)

#4. Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]
print(color_list[0])
print(color_list[-1])

#5. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.Sample value of n is 5
n = input("Enter a number :")
sum = int(n + n*n + n*n*n)
print(sum)

#6. Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers. Sample data : 3, 5, 7, 23
l = input("Enter numbers : ")
list1= []
for i in l:
    list1.append(l.split(','))

#7. Write a program that will convert celsius value to Fahrenheit.
temp = float(input("Enter celsius temperature : "))
print("Temperature in fahrenheit :",(temp*1.8)+32)

#8. User will input (2numbers). Write a program to swap the numbers. Add incrementally in any one variable.
a = int(input("Enter first number : "))
b = int(input("Enter second number :"))
temp = a
a = b
b = temp
print(a)
print(b)
print(b+1)

#9. Write a program that will tell whether the number entered by the user is odd or even.
n = int(input("Enter number :"))
if n % 2 == 0:
    ("Even Number")
else :
    ("Odd Number")

#10. Write a program that will tell whether the given year is a leap year or not.
year = int(input("Enter year :"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not Leap Year")

#11. Write a program to find the euclidean distance between two coordinates.
x1 = int(input("Enter first x coorinate"))
x2 = int(input("Enter second x coorinate"))
y1 = int(input("Enter first y coorinate"))
y2 = int(input("Enter second y coorinate"))
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Distance between coordinates :")

#12. Write a program that take a user input of three angles and will find out whether it can form a triangle or not.
a = float(input("Enter first angle :"))
b = float(input("Enter second angle :"))
c = float(input("Enter third angle :"))
if a + b + c == 180:
    print("It forms triangle")
else:
    print("It does not forms triangle")

#13. WAP to find compound interest for given values.
principle = float(input("Enter principle amount : "))
rate = float(input("Enter a rate :"))
time = float(input("Enter time after which it will compounded : "))
n	=	int(input("Enter number of times interest applied per time period: "))
A = principle * (1 + (rate/n))^(n * time)
print("Interest : ",A - principle)
#14. Given a positive integer N, the task is to write a Python program to check if the number is Prime or not in Python.
n = int(input("Enter a number : "))
print(n.isprime())

#15. Given a positive integer N. The task is to find 12+ 22+ 32+ ..... + N2.
n = int(input("Enter a number : "))
sum = 0
for i in range(1,n):
    sum = sum + ((i * 10) + 2)
print(sum)