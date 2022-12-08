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
    for line in lines:
        #line.strip to not count the newline character
        line.strip()
        #Find half of the line length
        half = len(line) // 2
        #Check if the letters from the two compartment are equal or not
        rucksack_a = line[:half]
        rucksack_b = line[half:]
        for letter in rucksack_a:
            if letter in rucksack_b:
                sum += priorities.get(letter)
                break
    print(sum)
        
