#bmi.py
# This program will read inputs from users in relation to their hright and weight and calculate their BMI
# Author Michael Casey

#Gatehring weight
weight = int(input ('how much do you weigh (kg)?:'))
#Gathering Height
height = int(input ('How tall are you (cm)?:'))

#calculating bmi
# Step 1: conveert height to m2
height2 = height / 100

#Testing Calculation
#print (height2)

height3 = height2**2

#Testing Calculation
#print (height3)

bmi = weight / height3
print (bmi)


#Decided to add a message depending on the result of the calculation, the idea came from the "if" function in excel,
#I referenced https://stackoverflow.com/questions/13628791/determine-whether-integer-is-between-two-other-integers
if 18.5 <= bmi <= 25:
    print ('Your BMI is average')
if 25 < bmi <= 30 :
    print ('Your BMI is classified as overweight')
if 25 < bmi <= 30:
    print ('Your BMI is classified as obeise')
if 30 < bmi:
    print ('Your BMI is classified as morbidly obeise')



