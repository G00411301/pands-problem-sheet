#secondstring.py
# This program asks a user to input a string and outputs every second letter in reverse order
# Author Michael Casey

#Gater input from user

rawstring = input("Please enter a sentence: ")

#calculate length of string
length1 = len(rawstring)

#print (length1)

#convert string into a list of characters
#source: https://www.geeksforgeeks.org/python-program-convert-string-list/
def Convert(rawstring):
    list1=[]
    list1[:0]=rawstring
    return list1

#assign list to variable mylist
mylist = Convert(rawstring)

#print (mylist)
#reverse the order of the list
#source: https://www.programiz.com/python-programming/methods/list/reverse
mylist.reverse()
#print (mylist)
#Source https://www.kite.com/python/answers/how-to-get-every-nth-element-from-a-list-in-python
mylistcut = mylist[::2]

#Printing list without brackets and commas
#source https://stackoverflow.com/questions/11178061/print-list-without-brackets-in-a-single-row
print (*mylistcut)



