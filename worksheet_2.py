#Writing Python programs that manipulate numbers, booleans, strings, lists, dictionaries, sets, and tuples. 
#1. L is a list defined as L= [11, 12, 13, 14]. 
#(i) WAP to add 50 and 60 to L. 
L = [11 , 12 , 13 , 14]
L.append(50)
L.append(60)
print(L)
#(ii) WAP to remove 11 and 13 from L. 
L.remove(11)
L.remove(13)
print(L)
#(iii) WAP to sort L in ascending order. 
L.sort()
print(L)
#(iv) WAP to sort L in descending order. 
L.reverse()
print(L)
#(v) WAP to search for 13 in L. 

for i in L:
    if i == 13:
        print('Found')
    else:
        print('Not Found')

#(vi) WAP to count the number of elements present in L. 

print(len(L))

#(vii) WAP to sum all the elements in L. 
print(sum(L))

#(viii) WAP to sum all ODD numbers in L. 
odd_sum = 0
for i in L:
    if i % 2 != 0:
        odd_sum = odd_sum + i
print(odd_sum)

#(ix) WAP to sum all EVEN numbers in L. 
even_sum = 0
for i in L:
    if i % 2 == 0:
        even_sum = even_sum + i
print(even_sum)

#(x) WAP to sum all PRIME numbers in L. 
sum = 0
for i in L:
    if i.isprime():
        sum = sum + i
print(sum)
#(xi) WAP to clear all the elements in L. 
L.clear()
#(xii) WAP to delete L. 
del(L)
#2. Write a Python program to sum all the items in a list without using any inbuilt function. 
sum = 0
for i in L:
    sum = sum + i
#3. Write a Python program to multiply all the items in a list without using any inbuilt function. 
product = 1
for i in L:
    product = product * i
#4. Write a Python program to generate a 3*4*6 3D array whose each element is *. 
array = [[['*' for _ in range(6)] for _ in range(4)] for _ in range(3)]

for i in array:
    for j in i:
        print(j)
    print()  

#5. D is a dictionary defined as D= {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}. 

#(i) WAP to add new entry in D; key=8 and value is 8.8 
D = {1: 5.6, 2: 7.8, 3: 6.6, 4: 8.7, 5: 7.7}

# (i) Add new entry in D; key=8, value=8.8
D[8] = 8.8

# (ii) Remove key=2
D.pop(2, None)

# (iii) Check if key=6 is present in D
key_present = 6 in D
print(f"Is key 6 present? {key_present}")

# (iv) Count the number of elements in D
count_elements = len(D)
print(f"Number of elements in D: {count_elements}")

# (v) Add all values present in D
sum_values = sum(D.values())
print(f"Sum of all values: {sum_values}")

# (vi) Update value of key=3 to 7.1
D[3] = 7.1

# (vii) Clear the dictionary
D.clear()

#6. S1 is a set defined as S1= [10, 20, 30, 40, 50, 60]. S2 is a set defined as S2= [40, 50, 60, 70, 80, 90]. 
S1 = {10, 20, 30, 40, 50, 60}
S2 = {40, 50, 60, 70, 80, 90}

# (i) Add 55 and 66 to Set S1
S1.update([55, 66])

# (ii) Remove 10 and 30 from Set S1
S1.discard(10)
S1.discard(30)

# (iii) Check whether 40 is present in S1
is_40_present = 40 in S1
print(f"Is 40 present in S1? {is_40_present}")

# (iv) Find the union between S1 and S2
union_set = S1.union(S2)
print(f"Union of S1 and S2: {union_set}")

# (v) Find the intersection between S1 and S2
intersection_set = S1.intersection(S2)
print(f"Intersection of S1 and S2: {intersection_set}")

# (vi) Find the difference S1 - S2
difference_set = S1.difference(S2)
print(f"S1 - S2: {difference_set}") 
#7. Write the following program. 
#(i) WAP to print 100 random strings whose length between 6 and 8. 

import random
import string

def random_string(length):
    return ''.join(random.choices(string.ascii_letters, k=length))

random_strings = [random_string(random.randint(6, 8)) for _ in range(100)]
for s in random_strings:
    print(s) 

#(ii) WAP to print all prime numbers between 600 and 800. 

for i in range(600,801):
    flag = 0
    for j in range(2,i):
        if i % j == 0:
            flag = 1
    if flag == 0:
        print(i)

#(iii) WAP to print all numbers between 100 and 1000 that are divisible by 7 and 9.

for i in range(100,1001):
    if i % 7 == 0 and i % 9 == 0:
        print(i)


#8. Write a Python program to display the examination schedule. (extract the date from exam_st_date). exam_st_date = (11, 12, 2014) 
exam_st_date = (11, 12, 2014)
print(f"The examination will start from: {exam_st_date[0]}/{exam_st_date[1]}/{exam_st_date[2]}")

#9. Iterate the given list of numbers and print only those numbers which are divisible by 5. 
numbers = [12, 15, 25, 36, 50, 60, 75, 81]
divisible_by_5 = [n for n in numbers if n % 5 == 0]
print("Numbers divisible by 5:", divisible_by_5)


#10. Write a Python program to check if a given number is even or odd using boolean variables. 
n = int(input("Enter a number to check for even :"))
if n % 2 == 0:
    print(True)
else :
    print(False)

#11. Write a program to find how many times substring “Emma” appears in the given string. 
str = input("ENter the lines:")
count_emma = str.count("Emma")
print(f"The substring 'Emma' appears {count_emma} times.")
#12. Create a new list from two list using the following condition, Given two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [11, 12, 13, 14, 15, 16, 17, 18, 19]

new_list = [x for x in list1 if x % 2 != 0] + [x for x in list2 if x % 2 == 0]
print("New list with odd numbers from list1 and even numbers from list2:", new_list)