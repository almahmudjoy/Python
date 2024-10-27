#ques-1
'''1. Write a Python script to sort (ascending and descending) a dictionary by value.
dictionary = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
Ascending order = [(0,0), (2, 1), (1, 2), (4,3). (3.4)]'''

dictionary = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
ascending_order = sorted(dictionary.items(), key=lambda x: x[1])
descending_order = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)

print("Ascending order:", ascending_order)
print("Descending order:", descending_order)

#ques-2
'''. Write a Python program to count number of items in a dictionary value that is a list. Sample Output
Dict['M1': [67,79,90,73,36], M2: [89.67,84], M3': [82.57])
Number of ltems in a Dictionary: 10'''

Dict = {'M1': [67, 79, 90, 73, 36], 'M2': [89, 67, 84], 'M3': [82, 57]}
count = sum(len(value) for value in Dict.values() if isinstance(value, list))

print("Number of Items in a Dictionary:", count)




#ques-3
'''. Write a Python program to remove the characters which have odd index values of a given string. Sample Output 
String Computer Education 
Remove Odd Index Char = Cmue dcto'''

string = "Computer Education"
result = ''.join([string[i] for i in range(len(string)) if i % 2 == 0])

print("Remove Odd Index Char =", result)


#ques-4
'''. Write a Python program to count the occurrences of each word in a given sentence Sample Output string To change the overall look your document. To change the look available in the gallery
 To: 2 change: 2. the 3, overall': 1, 'look': 2, 'your 1, document. 1, available: 1, in 1, gallery: 1)'''

string = "To change the overall look your document. To change the look available in the gallery"
words = string.split()
word_count = {word: words.count(word) for word in set(words)}

print("Word Occurrences:", word_count)

#ques-5
'''. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters. 
Sample Output
Enter the String = ComPuTeR
Check if there are at least 2 uppercase letters in the first 4 characters = COMPUTER 
Enter the String = Computer
Check if does not contain at least 2 uppercase letters in the first 4 characters Computer'''

string = input("Enter the String = ")
if sum(1 for char in string[:4] if char.isupper()) >= 2:
    result = string.upper()
else:
    result = string

print("Converted String:", result)

#ques-6
'''. Write a Python program to compute sum of digits of a given string
 Sample Output 
 String = Hello World 2345
 Sum of Digits of a Given String 14 '''

string = "Hello World 2345"
sum_digits = sum(int(char) for char in string if char.isdigit())

print("Sum of Digits in a Given String =", sum_digits)


#ques-7
'''. Write a Python program to count the number of strings from a given list of strings if the string length is 2 or more and the first and last characters are the same.
 Sample List: ['abc', 'xyz', 'aba, 1221] 
 Expected Result: 2'''

strings = ['abc', 'xyz', 'aba', '1221']
count = sum(1 for s in strings if len(s) >= 2 and s[0] == s[-1])

print("Expected Result =", count)
