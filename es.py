# es.py
# This program reads in a file and counts how many e's are in it 
# Author Michael Casey

# source  Youtube - https://www.youtube.com/watch?v=SJ2nWs4yl9k
import sys

filename = None
startingpoint = 0

#checking to mkae sure an argument/filename has been included in the command line
while len(sys.argv)<2:
#if there is only one name ie. "python .\es.py the below message pops up and closes the program"
    print ("Please include file name/path in command line")
    quit()

#I assume the second argument passed into the command line is a file/path
filename = sys.argv[1]


#filename = "test.txt"
#I assume file is in current directory or command line input includes the path
with open (filename, 'r') as f:
   data = f.read()
   #counting how many e's are in the text file - source geeksforgeeeks.org
   nume = data.count('e')
   numE = data.count('E')
   alle = nume + numE
   print ("There are", alle, "e's in", filename)
   




