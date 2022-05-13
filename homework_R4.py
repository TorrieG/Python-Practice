"""
TASK-1
Create a method called noSpace()
This method will take one String argument and it will return a new String with all spaces removed from the original String
"""
from tkinter import Y


def no_space(word):  
    return (word.replace(" ", ""))


"""
TASK-2
Create a method called replaceFirstLast()
-This method will take one String argument and it will return a new String with first and last characters replaced

NOTE: if the length is less than 2, then return empty String
NOTE: Ignore all before and after spaces (get actual String only)
"""
def replace_first_last(word):    
    word = word.strip()
    if len(word) < 2:
        return (word)
    else:
        return (word[-1]+word[1:-1]+word[0])

"""
TASK-3
Create a method called hasVowel()
This method will take one String argument and it will return a boolean 
checking if String has any vowel or not

NOTE: Vowels are = a, e, o, u, I
NOTE: Ignore cases
"""
def has_vowel(word):
    for i in word:
        if i == "A" or i == "a" or i == "E" or i == "e" or i == "I" or i == "i" or \
        i == "O" or i == "o" or i == "U" or i == "u":
            vowel = True
        else:
            vowel = False
    print (vowel)

"""
TASK-4
Create a method called checkAge()
This method will take an int yearOfBirth as  
argument and it will print message below based on the entry
If the age is less than 16, then print “AGE IS NOT ALLOWED”
If the age is 16 or more, then print “AGE IS ALLOWED”
If the age is more than 100 or a future year entered, print “AGE IS NOT VALID”
NOTE: Calculate the age taking base year as current year in a dynamic way. You can use Date class.
"""
def check_age(year_of_birth):
    current_year = 2022
    if year_of_birth > current_year or current_year - year_of_birth > 100:
        print("AGE IS NOT VALID") 
    elif current_year - year_of_birth < 16:
        print("AGE IS NOT ALLOWED")
    elif current_year - year_of_birth >= 16:
        print("AGE IS ALLOWED")

"""
TASK-5
Create a method called averageOfEdges()
This method will take three int arguments and it will return average of min
and max numbers
"""
def average_of_edges(num1, num2, num3):
    edges = [num1, num2, num3]
    edges.sort()
    print ((edges[0] +edges[-1]) // 2)

'''
TASK-6
Create a method called noA()
This method will take a String array argument and it will return a 
new array with all elements starting with A or a replaced with “###”

NOTE: Assume length will always be more than zero
NOTE: Ignore cases
'''
def no_a(wordlist):
    for i in range(len(wordlist)):
        if wordlist[i].lower().startswith('a'):
            wordlist[i] = '###'
    print(wordlist)

"""
TASK-6
Create a method called no3or5()
This method will take an int array argument and it will return a new array with some elements replaced as below
If element can be divided by 5, replace it with 99
If element can be divided by 3, replace it with 100
If element can be divided by both 3 and 5, replace it with 101

NOTE: Assume length will always be more than zero
"""
def no_3_or_5(numlist):
    for i in range(len(numlist)):
        if numlist[i] % 15 == 0:
            numlist[i] = 101
        elif numlist[i] % 3 == 0:
            numlist[i] = 100
        elif numlist[i] % 5 == 0:
            numlist[i] = 99
    return numlist

"""
TASK-8
Create a method called countPrimes()
This method will take an int array argument and it will return how many
elements in the array are prime numbers

NOTE: Prime number is a number that can be divided only by 1 and itself
NOTE: Negative numbers cannot be prime
Examples: 2,3,5,7,11,13,17,19,23,29,31,37 etc.
NOTE: Smallest prime number is 2
"""
def count_primes(arraylist):
    prime = []

    for num in arraylist:
        if num == 2:
            prime.append(i)
        elif num > 2:
            is_prime = True
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                prime.append(num)
    print(len(prime))










print (no_space("    Hello    "))
print (replace_first_last("    Hello   "))
has_vowel("ESDE")
check_age(1800)
average_of_edges(-2,-2,10)

stuff = ["appium", "123", "ABC", "java"]
no_a(stuff)

task7 = [10, 11, 12, 13, 14, 15]
print(no_3_or_5(task7))

task8 = [41, 53, 19, 47, 67, 3]
count_primes(task8)
