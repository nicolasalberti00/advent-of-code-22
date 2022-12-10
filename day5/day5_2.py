import re

#Dictionary with crates
crates = {
        1: ['P', 'Z', 'M', 'T', 'R', 'C', 'N'],
        2: ['Z', 'B', 'S', 'T', 'N', 'D'],
        3: ['G', 'T', 'C', 'F', 'R', 'Q', 'H', 'M'],
        4: ['Z', 'R', 'G'],
        5: ['H', 'R', 'N', 'Z'],
        6: ['D', 'L', 'Z', 'P', 'W', 'S', 'H', 'F'],
        7: ['M', 'G', 'C', 'R', 'Z', 'D', 'W'],
        8: ['Q', 'Z', 'W', 'H', 'L', 'F', 'J', 'S'],
        9: ['N', 'W', 'P', 'Q', 'S']
        }
#Function to remove words and leaving just numbers to work with
to_remove = ['move', 'from', 'to']
re_removed_words = re.compile(r"\b(" + "|".join(to_remove) + ")\\W", re.I)
def remove_words(line):
    global re_removed_words
    return re_removed_words.sub("", line)

number = []

with open('day5.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        line = line.rstrip()
        line = remove_words(line)
        #Remove whitespaces
        line = line.split()
        #convert strings to int
        nums = [int(s) for s in line]
        moves = nums[0]
        #looping for the number of moves
        while nums[0]:
                to_move = crates[nums[1]].pop(moves-1)
                crates[nums[2]].insert(0, to_move)
                nums[0] -= 1
                moves -= 1
    #The result is the first letter of each value in the dictionary
    print(crates)

 
