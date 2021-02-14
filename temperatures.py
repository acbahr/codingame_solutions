import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
temps = input()   # temps input as a space separated string
result = ''

if n == 0:
    print('0')
else:
    temps_split = temps.split() # creates list of temps
    result = temps_split[0]
    
    for temp in temps_split:
        if abs(int(temp)) < abs(int(result)):
            result = temp
        elif abs(int(temp)) == abs(int(result)):
            result = max(int(temp),int(result))


# Write an answer using print

print(result)
