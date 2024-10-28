#ques-1
'''.Write a program to create a new string made of an input string’s first, middle, and last character.
Input: James
Output: Jms'''
'''
name = input("Enter name : ")
first_chr = name[0]

middle_index = len(name)//2
middle_chr = name[middle_index]

last_chr = name[-1]

output = first_chr + middle_chr + last_chr
print("Combined name: "+output)'''

#ques-2
''' Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the 
middle of s1.
Input: s1 = Python s2 = ABC
Output: s3 = PytABChon'''
'''
str1 = input("Enter first name : ")
str2 =input("Enter second name: ")

mid = len(str1)//2

x = str1[:mid]+str2+str1[mid:]
print("Append name : "+x)
'''
#ques-3
'''Write a python program to arrange string characters such that lowercase letters should come 
first.
Input: LaNguAGe
Output: agueLNAG'''
'''
input_string = input("Enter a name : ")
lower_letter = []
upper_letter = []

for char in input_string:
    if char.islower():
        lower_letter.append(char)
    elif char.isupper():
        upper_letter.append(char)

result =''.join (lower_letter + upper_letter)

print("After rearrange : "+result)'''

#ques-4
'''Write a python program to count all letters, digits, and special symbols from a given string.
Input: P@#yn26at^&i5ve
Output:
Total counts of chars, digits, and symbols
Chars = 8 
Digits = 3 
Symbol = 4'''

'''
input_string = input("Enter a name : ")
chars = []
digits = []
symbols = []

for char in input_string:
    if char.isalpha():
        chars.append(char)
    elif char.isdigit():
        digits.append(char)
    else:
        symbols.append(char)

print(f"total count of character: {len(chars)}")
print(f"total count of digit : {len(digits)}")
print(f"total count of symbol : {len(symbols)}")'''

#ques-5
'''Write a program to find all occurrences of a substring in a given string by ignoring the case.
Input: str1 = "Welcome to USA. usa is awesome, isn't it?"
Output: The USA count is: 2'''
'''
str1 =input("Enter given string : ")
words = str1.split()
substring = 'USA'
str1_lower = str1.lower()
substring_lower = substring.lower()

count = str1_lower.count(substring_lower)
print(f"The {substring} count is : {count}")
'''
#ques-6
'''WWrite a program to count occurrences of all characters within a string.
Input: str1 = "Apple"
Output: 'A': 1, 'p': 2, 'l': 1, 'e': 1'''
# Sample input string
str1 = "Apple"

# Convert the string to lowercase or uppercase if case-insensitive count is desired
str1 = str1.lower()  # Remove this line if case sensitivity is required

# Creating a dictionary to store character counts
char_count = {}
for char in str1:
    char_count[char] = char_count.get(char, 0) + 1

# Displaying the result
for char, count in char_count.items():
    print(f"'{char}': {count}", end=", ")


#ques-7
'''Write a program to find the last position of a substring “Emma” in a given string.
Input: str1 = "Emma is a data scientist who knows Python. Emma works at google."
Output: Last occurrence of Emma starts at index 43'''

# Sample input string
str1 = "Emma is a data scientist who knows Python. Emma works at google."

# Finding the last position of "Emma"
last_position = str1.rfind("Emma")

# Displaying the result
print("Last occurrence of 'Emma' starts at index", last_position)



#ques-8
'''Write a program to remove special symbols / punctuation from a string
Input: str1 = "/*Jon is @developer & musician"
Output: "Jon is developer musician"
'''

import re

# Sample input string
str1 = "/*Jon is @developer & musician"

# Removing special symbols/punctuation using regex
cleaned_str = re.sub(r'[^A-Za-z0-9\s]', '', str1)

# Displaying the result
print(cleaned_str)


#ques-9
'''Write a program to find words with both alphabets and numbers from an input string.
Input: str1 = "Emma25 is Data scientist50 and AI Expert"
Output: Emma25
scientist50'''

import re

# Sample input string
str1 = "Emma25 is Data scientist50 and AI Expert"

# Finding words with both alphabets and numbers using regex
words_with_alphabets_and_numbers = re.findall(r'\b\w*[a-zA-Z]+\w*[0-9]+\w*|\w*[0-9]+\w*[a-zA-Z]+\w*\b', str1)

# Displaying the result
print(words_with_alphabets_and_numbers)


#ques-10
'''Write a program to replace each special symbol with # in the following string.
Input: str1 = '/*Jon is @developer & musician!!'
Output: ##Jon is #developer # musician##'''


import re

# Sample input string
str1 = '/*Jon is @developer & musician!!'

# Replacing special symbols with #
replaced_str = re.sub(r'[^A-Za-z0-9\s]', '#', str1)

# Displaying the result
print(replaced_str)



##List

#ques-11
'''Write a program to reverse a list in Python
Input: list1 = [100, 200, 300, 400, 500]
Output: [500, 400, 300, 200, 100]
'''

# Sample input list
list1 = [100, 200, 300, 400, 500]

# Reversing the list
reversed_list = list1[::-1]

# Displaying the result
print(reversed_list)


#ques-12
'''Write a program to add two lists index-wise. Create a new list that contains the 0th index 
item from both the list, then the 1st index item, and so on till the last element. any leftover items 
will get added at the end of the new list.
Input: list1 = ["M", "na", "i", "Ka"]
 list2 = ["y", "me", "s", "rim"]
Output: ['My', 'name', 'is', 'Karim']
'''

# Sample input lists
list1 = ["M", "na", "i", "Ka"]
list2 = ["y", "me", "s", "rim"]

# Creating a new list to store the result
result = []

# Get the length of the longest list
max_length = max(len(list1), len(list2))

# Iterate over the indices of the longest list
for i in range(max_length):
    # Add the index-wise items from both lists if they exist
    if i < len(list1):
        result.append(list1[i])
    if i < len(list2):
        result.append(list2[i])

# Joining the result list to form words
output = [''.join(result[i:i + 2]) for i in range(0, len(result), 2)]

# Displaying the result
print(output)


#ques-13
'''Given a list of numbers. write a program to turn every item of a list into its square.
Given: numbers = [1, 2, 3, 4, 5, 6, 7]
Expected output: [1, 4, 9, 16, 25, 36, 49]
'''

# Given list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7]

# Squaring each item in the list using a list comprehension
squared_numbers = [num ** 2 for num in numbers]

# Displaying the result
print(squared_numbers)


#ques-14
'''Write a program to remove empty strings from the list of strings
list1 = ["Mango", "", "Orange", "Grape", "", "Dragon"]
Expected output: ["Mango", "Orange", "Grape", "Dragon"]
'''

# Given list of strings
list1 = ["Mango", "", "Orange", "Grape", "", "Dragon"]

# Removing empty strings using list comprehension
filtered_list = [fruit for fruit in list1 if fruit]

# Displaying the result
print(filtered_list)


#ques-15
'''You have given a Python list. Write a program to find value 20 in the list, and if it is present, 
replace it with 200. Only update the first occurrence of an item.
Input: list1 = [5, 10, 15, 20, 25, 50, 20]
Expected output: [5, 10, 15, 200, 25, 50, 20]
'''
# Given list
list1 = [5, 10, 15, 20, 25, 50, 20]

# Finding the index of the first occurrence of 20
if 20 in list1:
    index = list1.index(20)  # Get the index of the first occurrence
    list1[index] = 200       # Replace it with 200

# Displaying the result
print(list1)


#ques-16
'''Given a Python list, write a program to remove all occurrences of item 20.
Given: list1 = [5, 20, 15, 20, 25, 50, 20]
Expected output: [5, 15, 25, 50]'''

# Given list
list1 = [5, 20, 15, 20, 25, 50, 20]

# Removing all occurrences of 20 using list comprehension
filtered_list = [item for item in list1 if item != 20]

# Displaying the result
print(filtered_list)


#ques-17
'''WWrite a Python program to remove duplicates from a list'''

# Given list with duplicates
list_with_duplicates = [1, 2, 3, 2, 4, 5, 1, 6, 4]

# Removing duplicates while preserving order
unique_list = []
for item in list_with_duplicates:
    if item not in unique_list:
        unique_list.append(item)

# Displaying the result
print(unique_list)


#ques-18
'''Write a Python program to print the numbers of a specified list after removing even numbers 
from it'''

# Given list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Removing even numbers using list comprehension
odd_numbers = [num for num in numbers if num % 2 != 0]

# Displaying the result
print(odd_numbers)


#ques-19
'''WWrite a Python program that prints long text, converts it to a list, and prints all the words and 
the frequency of each word.'''

from collections import Counter

# Long text input
text = """
Python is an amazing programming language. It is widely used for web development, data analysis, artificial intelligence, scientific computing, and more.
Python is known for its simplicity and readability, making it a great choice for beginners and experienced developers alike.
"""

# Converting text to a list of words
words = text.split()

# Counting the frequency of each word using Counter
word_count = Counter(words)

# Displaying each word and its frequency
for word, frequency in word_count.items():
    print(f"'{word}': {frequency}")


#ques-20
'''Write a Python program to find the heights of the top three buildings in descending order 
from eight given buildings.
Input:
0 <= height of building (integer) <= 10,000
Input the heights of eight buildings:
25
35
15
16
30
45
37
39
Output: Heights of the top three buildings:
45
39
37'''

# Input: Heights of eight buildings
building_heights = []

print("Input the heights of eight buildings:")
for i in range(8):
    height = int(input())
    building_heights.append(height)

# Sorting the heights in descending order
sorted_heights = sorted(building_heights, reverse=True)

# Getting the top three heights
top_three_heights = sorted_heights[:3]

# Displaying the result
print("Heights of the top three buildings:")
for height in top_three_heights:
    print(height)




##Tuple

#ques-21
'''The given tuple is a nested tuple. write a Python program to print the value 20.
Input: tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
output: 20'''

# Given nested tuple
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))

# Accessing and printing the value 20
value = tuple1[1][1]  # Access the second element of the second item (list)
print(value)


#ques-22
'''Write a program to Swap two tuples in Python
Input: tuple1 = (11, 22)
 tuple2 = (99, 88)
output: tuple1: (99, 88)
 tuple2: (11, 22)'''

# Given tuples
tuple1 = (11, 22)
tuple2 = (99, 88)

# Swapping the tuples
tuple1, tuple2 = tuple2, tuple1

# Displaying the output
print("tuple1:", tuple1)
print("tuple2:", tuple2)


#ques-23
'''Write a program to copy elements 44 and 55 from the following tuple into a new tuple.
Input: tuple1 = (11, 22, 33, 44, 55, 66)
output: tuple2: (44, 55)'''

# Given tuple
tuple1 = (11, 22, 33, 44, 55, 66)

# Copying elements 44 and 55 into a new tuple
tuple2 = (tuple1[3], tuple1[4])  # Accessing by index

# Displaying the output
print("tuple2:", tuple2)


#ques-24
'''Write a python program to check if all items in the tuple are the same
Input: tuple1 = (45, 45, 45, 45)
output: True'''

# Given tuple
tuple1 = (45, 45, 45, 45)

# Checking if all items in the tuple are the same
all_same = all(item == tuple1[0] for item in tuple1)

# Displaying the output
print(all_same)


#ques-25
'''Write a Python program to get the 1
st 4
th element and the last 4
th element of a tuple.
Input: WORLDISCHANGING
Output: DG
'''

# Given input string
input_string = "WORLDISCHANGING"

# Converting the string to a tuple of characters
tuple1 = tuple(input_string)

# Accessing the 1st, 4th, and last 4th elements
first_element = tuple1[0]       # 1st element (index 0)
fourth_element = tuple1[3]      # 4th element (index 3)
last_fourth_element = tuple1[-4] # Last 4th element (index -4)

# Combining the results
output = first_element + fourth_element + last_fourth_element

# Displaying the output
print("Output:", output)


#ques-26
'''Write a Python program to check whether an element (e.g: a) exists within a tuple.
Input: ‘There’, ‘is’, ‘a’, ‘rose’, ‘garden’'''

# Given tuple
my_tuple = ('There', 'is', 'a', 'rose', 'garden')

# Element to check
element_to_check = 'a'

# Checking if the element exists in the tuple
exists = element_to_check in my_tuple

# Displaying the output
print(f"Does the element '{element_to_check}' exist in the tuple? {exists}")


#ques-27
'''Write a Python program to calculate the product, multiplying all the numbers in a given 
tuple.
Original Tuple:
(4, 3, 2, 2, -1, 18)
Product - multiplying all the numbers of the said tuple: -864
Original Tuple:
(2, 4, 8, 8, 3, 2, 9)
Product - multiplying all the numbers of the said tuple: 27648'''

from functools import reduce

# Function to calculate the product of elements in a tuple
def calculate_product(tup):
    return reduce(lambda x, y: x * y, tup)

# Test with the first tuple
tuple1 = (4, 3, 2, 2, -1, 18)
product1 = calculate_product(tuple1)
print("Original Tuple:")
print(tuple1)
print("Product - multiplying all the numbers of the said tuple:", product1)

# Test with the second tuple
tuple2 = (2, 4, 8, 8, 3, 2, 9)
product2 = calculate_product(tuple2)
print("\nOriginal Tuple:")
print(tuple2)
print("Product - multiplying all the numbers of the said tuple:", product2)


#ques-28
'''Write a Python program to calculate the average value of the numbers in a given tuple of 
tuples.
Original Tuple:
((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
Average value of the numbers of the said tuple of tuples:
[30.5, 34.25, 27.0, 23.25]
Original Tuple:
((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
Average value of the numbers of the said tuple of tuples:
[25.5, -18.0, 3.75]
'''

# Function to calculate the average values of each tuple in a tuple of tuples
def calculate_averages(tup_of_tups):
    averages = []
    for tup in tup_of_tups:
        avg = sum(tup) / len(tup)  # Calculate average
        averages.append(avg)
    return averages

# Test with the first tuple of tuples
tuple1 = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
averages1 = calculate_averages(tuple1)
print("Original Tuple:")
print(tuple1)
print("Average value of the numbers of the said tuple of tuples:")
print(averages1)

# Test with the second tuple of tuples
tuple2 = ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
averages2 = calculate_averages(tuple2)
print("\nOriginal Tuple:")
print(tuple2)
print("Average value of the numbers of the said tuple of tuples:")
print(averages2)


# Test with


#ques-29
'''Write a Python program to convert a given tuple of positive integers into an integer.
Original tuple:
(1, 2, 3)
Convert the said tuple of positive integers into an integer:
123
Original tuple:
(10, 20, 40, 5, 70)
Convert the said tuple of positive integers into an integer:
102040570'''

# Function to convert a tuple of integers into a single integer
def tuple_to_integer(tup):
    # Convert each integer to a string and join them
    return int(''.join(map(str, tup)))

# Test with the first tuple
tuple1 = (1, 2, 3)
result1 = tuple_to_integer(tuple1)
print("Original tuple:")
print(tuple1)
print("Convert the said tuple of positive integers into an integer:")
print(result1)

# Test with the second tuple
tuple2 = (10, 20, 40, 5, 70)
result2 = tuple_to_integer(tuple2)
print("\nOriginal tuple:")
print(tuple2)
print("Convert the said tuple of positive integers into an integer:")
print(result2)


#ques-30
'''Write a Python program to check if a specified element appears in a tuple of tuples.
Original list:
(('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
Check if White presenet in said tuple of tuples!
True
Check if White presenet in said tuple of tuples!
True
Check if Olive presenet in said tuple of tuples!
False'''

# Function to check if an element exists in a tuple of tuples
def check_element_in_tuples(tuples, element):
    return any(element in tup for tup in tuples)

# Original tuple of tuples
tuple_of_tuples = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))

# Check for different elements
element1 = 'White'
element2 = 'Olive'

# Output results
print("Original list:")
print(tuple_of_tuples)

print(f"Check if '{element1}' present in said tuple of tuples!")
print(check_element_in_tuples(tuple_of_tuples, element1))  # Should return True

print(f"Check if '{element1}' present in said tuple of tuples!")
print(check_element_in_tuples(tuple_of_tuples, element1))  # Should return True

print(f"Check if '{element2}' present in said tuple of tuples!")
print(check_element_in_tuples(tuple_of_tuples, element2))  # Should return False















