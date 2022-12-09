#Import string to use lowercase and uppercase letters
import string, math 
letters = list(string.ascii_letters)
#Creating a dictionary for the priorities
values = range(1, 53)
priorities = dict(zip(letters, values))
#Sum of the values of the properties found
sum = 0
#Opening txt with input
with open('day3_1.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    for line in range(0,len(lines),3):
        first = set(lines[line].rstrip())
        second = set(lines[line+1].rstrip())
        third = set(lines[line+2].rstrip())
        intersect = first.intersection(second, third)
        res = intersect.pop()
        sum += priorities.get(res)
    print(sum)
        
