#Task 1
#The greatest number
#Write a Python program to get the largest number from a list of random numbers with the length of 10
#Constraints: use only while loop and random module to generate numbers

import random

my_list = []
i = 1

while i <= 10:
    my_list.append(random.randint((10 ** 9), (10 ** 10) - 1))
    i+=1
print(my_list)
x = (max(my_list))
print("Max value in my list = " +str(x) )

