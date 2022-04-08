#collatz.py
# This program will read positive integer inputs from users and calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one
# Author Michael Casey

#Gatehring user input
number = int(input ('Enter any positive number: '))

#setting cutoff value
cutoff = 1

# if user input is not a positive number, quit the program
if number <0:
    print ("That's not a positive number!!")
    quit ()


#check if number is even or odd

while number != 1:
    if number % 2 == 0:
        number = number/2
        print (int(number))
    else:
        number = 3*number+1
        print (int(number))
