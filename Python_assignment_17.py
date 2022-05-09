#Q-1 Python program to find difference between current time and given time
# Python program to find the
# difference between two times
  
  
# function to obtain the time
# in minutes form
def difference(h1, m1, h2, m2):
      
    # convert h1 : m1 into
    # minutes
    t1 = h1 * 60 + m1
      
    # convert h2 : m2 into
    # minutes 
    t2 = h2 * 60 + m2
      
    if (t1 == t2): 
        print("Both are same times")
        return 
    else:
          
        # calculating the difference
        diff = t2-t1
          
    # calculating hours from
    # difference
    h = (int(diff / 60)) % 24
      
    # calculating minutes from 
    # difference
    m = diff % 60
  
    print(h, ":", m)
  
# Driver's code
if __name__ == "__main__":
      
    difference(7, 20, 9, 45)
    difference(15, 23, 18, 54)
    difference(16, 20, 16, 20)

#Q-2 Python Program to Create a Lap Timer

# importing libraries
import time
  
  
# Timer starts
starttime=time.time()
lasttime=starttime
lapnum=1
  
print("Press ENTER to count laps.\nPress CTRL+C to stop")
  
try:
     while True:
              
          # Input for the ENTER key press
          input()
  
          # The current lap-time
          laptime=round((time.time() - lasttime), 2)
  
          # Total time elapsed 
          # since the timer started
          totaltime=round((time.time() - starttime), 2)
  
          # Printing the lap number,
          # lap-time and total time
          print("Lap No. "+str(lapnum)) 
          print("Total Time: "+str(totaltime))
          print("Lap Time: "+str(laptime))
            
          print("*"*20)
  
          # Updating the previous total time
          # and lap number
          lasttime=time.time()
          lapnum+=1
  
# Stopping when CTRL+C is pressed
except KeyboardInterrupt:
     print("Done")

#Q-3 Convert date string to timestamp in Python

# Python program to convert 
# date to timestamp
  
  
import time
import datetime
  
  
string = "20/01/2020"
print(time.mktime(datetime.datetime.strptime(string,
                                             "%d/%m/%Y").timetuple()))


#Q-4 How to convert timestamp string to datetime object in Python?

from datetime import datetime
  
  
timestamp = 1545730073
dt_obj = datetime.fromtimestamp(1140825600)
  
print("date_time:",dt_obj)
print("type of dt:",type(dt_obj))

#Q-5 Find number of times every day occurs in a Year

# python program Find number of
# times every day occurs in a Year
  
 
import datetime
import calendar
  
def day_occur_time(year):
     
    # stores days in a week
    days = [ "Monday", "Tuesday", "Wednesday", 
           "Thursday",  "Friday", "Saturday",
           "Sunday" ]
     
    # Initialize all counts as 52
    L = [52 for i in range(7)]
     
    # Find the index of the first day
    # of the year
    pos = -1
    day = datetime.datetime(year, month = 1, day = 1).strftime("%A")
    for i in range(7):
        if day == days[i]:
            pos = i
             
    # mark the occurrence to be 53 of 1st day
    # and 2nd day if the year is leap year
    if calendar.isleap(year):
        L[pos] += 1
        L[(pos+1)%7] += 1
         
    else:
        L[pos] += 1
         
     
    # Print the days
    for i in range(7):
        print(days[i], L[i])
      
  
# Driver Code
year = 2019
day_occur_time(year)

#Q-6 Python Program to Check if String Contain Only Defined Characters using Regex

# _importing module
import re
  
  
def check(str, pattern):
    
    # _matching the strings
    if re.search(pattern, str):
        print("Valid String")
    else:
        print("Invalid String")
  
# _driver code
pattern = re.compile('^[1234]+$')
check('2134', pattern)
check('349', pattern)

#Q-7 Python program to Count Uppercase, Lowercase, special character and numeric values using Regex
import re
 
 
string = "ThisIsGeeksforGeeks !, 123"
 
# Creating separate lists using
# the re.findall() method.
uppercase_characters = re.findall(r"[A-Z]", string)
lowercase_characters = re.findall(r"[a-z]", string)
numerical_characters = re.findall(r"[0-9]", string)
special_characters = re.findall(r"[, .!?]", string)
 
print("The no. of uppercase characters is", len(uppercase_characters))
print("The no. of lowercase characters is", len(lowercase_characters))
print("The no. of numerical characters is", len(numerical_characters))
print("The no. of special characters is", len(special_characters))

#Q-8 Python Program to find the most occurring number in a string using Regex

# your code goes here# Python program to 
# find the most occurring element 
import re 
from collections import Counter 
  
def most_occr_element(word):
      
    # re.findall will extract all the elements 
    # from the string and make a list
    arr = re.findall(r'[0-9]+', word)    
      
    # to store maxm frequency
    maxm = 0  
  
    # to store maxm element of most frequency
    max_elem = 0
      
    # counter will store all the number with 
    # their frequencies
    # c = counter((55, 2), (2, 1), (3, 1), (4, 1))    
    c = Counter(arr)
    
    # Store all the keys of counter in a list in
    # which first would we our required element    
    for x in list(c.keys()):
  
        if c[x]>= maxm:
            maxm = c[x]
            max_elem = int(x)
                  
    return max_elem
  
# Driver program 
if __name__ == "__main__": 
    word = 'geek55of55gee4ksabc3dr2x'
    print(most_occr_element(word))

#Q-9 Python Regex to extract maximum numeric value from a string

# Function to extract maximum numeric value from 
# a given string
import re
  
def extractMax(input):
  
     # get a list of all numbers separated by 
     # lower case characters 
     # \d+ is a regular expression which means
     # one or more digit
     # output will be like ['100','564','365']
     numbers = re.findall('\d+',input)
  
     # now we need to convert each number into integer
     # int(string) converts string into integer
     # we will map int() function onto all elements 
     # of numbers list
     numbers = map(int,numbers)
  
     print (numbers)
  
# Driver program
if __name__ == "__main__":
    input = '100klh564abc365bg'
    extractMax(input)

#Q-10 Python Program to put spaces between words starting with capital letters using Regex

# import module for regular expression 
import re
#input
string='HelloWorldOfPython'
#Find the words in string starting with uppercase letter. 
words = re.findall('[A-Z][a-z]*', string)
#concatenate the word with space
print(' '.join((words)))