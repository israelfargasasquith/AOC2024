import re
import os

#First we read the file into two arrays


with open(os.getcwd()+os.sep+"AOC2024"+os.sep+"input") as input:
    firstColumm =[]
    secondColumm =[]
    distance = 0
    for line in input:
        parts = line.split()
        #print("First colummn: ",parts[0]," Second column: ",parts[1])
        firstColumm.append(int(parts[0]))
        secondColumm.append(int(parts[1]))
    
    firstColumm.sort()
    secondColumm.sort()

    for value1, value2 in zip(firstColumm,secondColumm):
        distance += abs(value1-value2)
    print("Total distance: ",distance)