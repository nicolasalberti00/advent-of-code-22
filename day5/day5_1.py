import re

#Lists with crates
one = ['P', 'Z', 'M', 'T', 'R', 'C', 'N']
two = ['Z', 'B', 'S', 'T', 'N', 'D']
three = ['G', 'T', 'C', 'F', 'R', 'Q', 'H', 'M']
four = ['Z', 'R', 'G']
five = ['H', 'R', 'N', 'Z']
six = ['D', 'L', 'Z', 'P', 'W', 'S', 'H', 'F']
seven = ['M', 'G', 'C', 'R', 'Z', 'D', 'W']
eight = ['Q', 'Z', 'W', 'H', 'L', 'F', 'J', 'S']
nine = ['N', 'W', 'P', 'Q', 'S']
#Function to remove words and leaving just numbers to work with
to_remove = ['move', 'from', 'to']
re_removed_words = re.compile(r"\b(" + "|".join(to_remove) + ")\\W", re.I)
def remove_words(line):
    global re_removed_words
    return re_removed_words.sub("", line)

with open('day5.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        line = line.rstrip()
        line = remove_words(line)
        print(line)
 
