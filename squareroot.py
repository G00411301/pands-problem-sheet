#squareroot.py
# This program asks a user to input a floating point and estimates its square root
# Author Michael Casey

#create a function that calculates the sqare root
def root(number):
    tol = 0.0001
    start = 1
    while True:
#newtons method for estimating square roots
        start = (start + number / start)/2
        difference = abs(number - start **2)
        if difference <= tol:
            break
    return start

#gather input from user
def result():
   while True:
       number = input("Please enter a positive number: ")
       number = float(number)
       print("The square root of", number, "is approx.", root(number))
       break
result()

#return sqare root result
#reference: stackoverflow
