#1no ques:
''' WWrite a program that prompts the user to enter the minutes (1 billion) and displays the number
of years and days for the minutes. For simplicity, assume a year has 365 days.'''
'''
def convert_minutes(minutes):
    # Constants
    minutes_in_a_day = 24 * 60
    days_in_a_year = 365

    # Calculate total days
    total_days = minutes // minutes_in_a_day
    print(total_days)

    # Calculate years and remaining days
    years = total_days // days_in_a_year
    remaining_days = total_days % days_in_a_year

    return years, remaining_days

# Prompt the user to enter the number of minutes
minutes = int(input("Enter the number of minutes: "))

# Get the number of years and days
years, days = convert_minutes(minutes)

# Display the results
print(f"{minutes} minutes is approximately {years} years and {days} days.")

'''

#2no ques:
''' Write a program that prompts the user to enter the three points (x1, y1), (x2, y2), and (x3, y3) 
of a triangle and display its area'''
'''
def example():
   x1 = float(input("Enter value of X1: "))
   y1 = float(input("Enter value of Y1: "))
   x2 = float(input("Enter value of X2: "))
   y2 = float(input("Enter value of Y2: "))
   x3 = float(input("Enter value of X3: "))
   y3 = float(input("Enter value of Y3: "))


   area = abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2)
   print("are of triangle is : " + str(area))

example()
'''

#3no ques:
'''Write a program that prompts the user to enter weight in pounds and height in inches and then 
displays the BMI. Note that one pound is 0.45359237 kgs and one inch is 0.0254 meters. The 
interpretations of BMI for people 16 years and older is followed:'''
'''
def bmmi():
    x = float(input("Enter weight in pounds : "))
    weight = x * 0.45359237
    y = float(input("Enter height in inches : "))
    height = y * 0.0254
    bmi = float(weight/(height**2))
    print("BMI is : " +str(bmi))

    a = int(input("Enter age : "))
    if a >= 16:
        if bmi < 18.5:
            print("Underweight")
        elif 18.5 <= bmi < 24.9:
            print("Normal")
        elif 25.0 <= bmi < 29.9:
            print("Overweight")
        else:
            print("obese")

bmmi()
'''
#4no ques:
'''Write a program that lets the user enter a year and then determine whether it is a leap year or 
not'''
'''
g_year =int(input("Enter given year : "))
if(g_year%4==0):
    print("This year is a leap year")
elif(g_year%100 ==0 and g_year&400 !=0):
    print("This year is a leap year")
else:
    print("This year is a not leap year")
'''
#5no ques:
'''Write a program to find the smallest factor other than 1 for an integer n (assume n >= 2).'''
'''
n = int(input("Enter an integer greater than or equal to 2: "))
i = 2
while i <= n:
     while n % i == 0:
        print(f"The smallest factor of {n} other than 1 is: {i}")
        break
     i = i + 1

print(n)
'''
#6no ques:
'''Write a Python program that accepts the user's first and last name and prints them in reverse
order with a space between them'''
'''
f_name =input("Enter first name : ")[::-1]
l_name =input("Enter last name : ")[::-1]

print(l_name,f_name)
'''

#7no ques:
'''Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current 
and previous number'''
'''
previous_num = 0
for current_num in range(10):
    sum = current_num + previous_num
    print(f"Current Number: {current_num}, Previous Number: {previous_num}, Sum: {sum}")
    previous_num = current_num
'''

#8no ques:
'''Write a Python program to calculate the difference between a given number and 17. If the 
number is greater than 17, return twice the absolute difference'''
'''
g_num =int(input("Enter given num: "))
f_num = 17

if(g_num > f_num):
    difference = 2 * abs( g_num - f_num)
    print("Difference is ", difference)
else:
    difference = f_num - g_num
    print("Given number is smallest than the fixed number", difference)
'''