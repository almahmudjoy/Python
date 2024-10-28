#ques-1
'''Write a Python program to sort (ascending and descending) a dictionary by value.'''

# Sample dictionary
sample_dict = {'apple': 10, 'banana': 5, 'cherry': 20, 'date': 15}

# Sorting in ascending order by value
ascending = dict(sorted(sample_dict.items(), key=lambda item: item[1]))
print("Ascending order:", ascending)

# Sorting in descending order by value
descending = dict(sorted(sample_dict.items(), key=lambda item: item[1], reverse=True))
print("Descending order:", descending)


#ques-2
'''Write a Python script to generate and print a dictionary that contains a number (between 1 
and n) in the form (x, x*x).
 Sample Dictionary (n = 5) :
 Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}'''

# Input for the maximum number n
n = 5  # You can change this value as needed

# Generating the dictionary
squared_dict = {x: x * x for x in range(1, n + 1)}

# Printing the dictionary
print(squared_dict)


#ques-3
'''Write a Python program to combine two dictionary by adding values for common keys.
 d1 = {'a': 100, 'b': 200, 'c':300}
 d2 = {'a': 300, 'b': 200, 'd':400}
 Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})'''

from collections import Counter

# Sample dictionaries
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

# Combine the dictionaries using Counter
result = Counter(d1) + Counter(d2)

# Display the result
print(result)



#ques-4
'''Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string : 'Intelligence'
Expected output: {'I': 1, 'n': 2, 't': 1, 'e': 3, 'l': 2, 'g': 1, 'c': 1}'''

# Sample string
sample_string = 'Intelligence'

# Creating a dictionary to count each letter's occurrences
letter_count = {}
for letter in sample_string:
    letter_count[letter] = letter_count.get(letter, 0) + 1

# Displaying the result
print(letter_count)



#ques-5
'''Write a Python program to get the top three items in a shop.
Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
Expected Output:
item4 55
item1 45.5
item3 41.3'''


# Sample data
shop_items = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}

# Sorting items by value in descending order and getting the top three
top_three = dict(sorted(shop_items.items(), key=lambda item: item[1], reverse=True)[:3])

# Displaying the result
for item, price in top_three.items():
    print(f"{item} {price}")



