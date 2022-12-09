import re
full_pairs = 0

with open('day4.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        line = line.rstrip()
        line = re.split(r"-|,", line)
        if (int(line[0]) <= int(line[2]) and int(line[1]) >= int(line[3])) or (int(line[2]) <= int(line[0]) and int(line[3]) >= int(line[1])):
            full_pairs += 1
    print(full_pairs)

