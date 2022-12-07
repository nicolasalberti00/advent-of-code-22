sum = 0
LOSE = 0
DRAW = 3
WIN = 6

with open('day2_1.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        char_col_1 = line[0]
        char_col_2 = line[2]
        if char_col_1 == 'A':
            if char_col_2 == 'Y':
                sum += WIN + 2
            elif char_col_2 == 'X':
                sum += DRAW + 1
            else:
                sum += LOSE + 3
        elif char_col_1 == 'B':
            if char_col_2 == 'Z':
                sum += WIN + 3
            elif char_col_2 == 'Y':
                sum += DRAW + 2
            else:
                sum += LOSE + 1
        elif char_col_1 == 'C':
            if char_col_2 == 'X':
                sum += WIN + 1
            elif char_col_2 == 'Z':
                sum += DRAW + 3
            else:
                sum += LOSE + 2
    print(sum)
