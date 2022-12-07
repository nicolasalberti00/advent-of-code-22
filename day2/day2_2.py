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
                sum += DRAW + 1
            elif char_col_2 == 'X':
                sum += LOSE + 3
            else:
                sum += WIN + 2
        elif char_col_1 == 'B':
            if char_col_2 == 'Y':
                sum += DRAW + 2
            elif char_col_2 == 'X':
                sum += LOSE + 1
            else:
                sum += WIN + 3
        elif char_col_1 == 'C':
            if char_col_2 == 'Y':
                sum += DRAW + 3
            elif char_col_2 == 'X':
                sum += LOSE + 2
            else:
                sum += WIN + 1
    print(sum)
