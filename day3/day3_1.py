#Import string to use lowercase and uppercase letters
import string, math 
letters = list(string.ascii_letters)
#Creating a dictionary for the priorities
keys = range(1, 53)
priorities = dict(zip(keys, letters))
#Sum of the values of the properties found
sum = 0
#Opening txt with input
with open('day3_1.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        #line.strip to not count the newline character
        line.strip()
        for part_a in range(0, math.floor(len(line)/2)):
            for part_b in range(math.floor(len(line)/2)+1, len(line)):
                if part_a == part_b:
                    #TODO
                    sum += {i for i in priorities if priorities[i]==part_a}
    print(sum)
        
