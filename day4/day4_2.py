import re
full_pairs = 0

with open('day4.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        line = line.rstrip()
        line = re.split(r"-|,", line)
        if int(line[3]) >= int(line[0]) >= int(line[2]) or int(line[1]) >= int(line[2]) >= int(line[0]):
            full_pairs += 1
    print(full_pairs)

