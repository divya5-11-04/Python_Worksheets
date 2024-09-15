#Writing Python programs that define and use functions and classes to solve problems. 
#1. Write a Python program to calculate the difference between a given number and 17  with the help of function. If the number is greater than 17, return twice the absolute difference. 

def calc(n):
    if n > 17:
        print(2 * (n - 17))
    else:
        print(n - 17)

#2. Write a Python program for a function. to test whether a number is within 100 to 1000 or 2000. 

def check(n):
    if n >= 100 and n <= 1000:
        print("Number is within 100 to 1000")
    elif n > 1000 and n <= 2000:
         print("Number is within 100 to 2000")
        
#3. Write a Python program to reverse a string. 

def rev(str):
    print(str.reversed())

#4. Write a Python function that accepts a string and counts the number of upper and lower case letters. 
def count(str):
    upper = 0
    lower = 0
    for i in str:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
    print("Upper case letters :",upper)
    print("Lower case letters :",lower)

            

#5. Write a Python function that takes a list and returns a new list with distinct elements from the first list. 
def unique_list(l1):
    l2 = []
    for i in l1:
        if i  not in l2:
            l2.append(i)
    print(l2)

#6. Write a Python program to print the even numbers from a given list. Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9] Expected Result : [2, 4, 6, 8] 
def ret_even(l1):
    l2 = []
    for i in l1:
        if i % 2 == 0:
            l2.append(i)
#7. Write a Python program to access a function inside a function.
    unique_list(l2)

#8. Define a Python function student(). Using function attributes display the names of all arguments. 
def student(student_name , roll_no , marks):
    print(f'Student id = {student_name} \n Roll number : {roll_no} \n Marks : {marks}')

#9. Write a Python class named Student with two attributes: student_id, student_name. Add  a new attribute: student_class. Create a function to display all attributes and their values in the Student class. 
class Student:
    def __init__(self, student_id, student_name, student_class):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class

    
    def display_attributes(self):
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.student_name}")
        print(f"Student Class: {self.student_class}")



#10. Write a Python class named Student with two instances student1, student2 and assign values to the instances' attributes. Print all the attributes of the student1, student2 instances with their values in the given format. 


student1 = Student(104, "RAM", "5th Grade")
student2 = Student(110, "SHAM", "12th Grade")

# Displaying attributes for both students
print(f"Student 1: ID = {student1.student_id}, Name = {student1.student_name}, Class = {student1.student_class}")
print(f"Student 2: ID = {student2.student_id}, Name = {student2.student_name}, Class = {student2.student_class}")

#11. Write a Python class named Circle constructed from a radius and two methods that will compute the area and the perimeter of a circle. 

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

#12. Write a Python class that has two methods: get_String and print_String , get_String accept a string from the user and print_String prints the string in upper case.
class Str:
    def __init__(self):
        self.string = ""

    def get_String(self):
        self.string = input("Enter a string: ")

    def print_String(self):
        print(self.string.upper())