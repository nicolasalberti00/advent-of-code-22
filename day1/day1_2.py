best_1 = 0
best_2 = 0
best_3 = 0
sum = 0

with open('day1.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines();
    for line in lines:
        if line.strip():
            sum += int(line);
        else:
            if best_1 < sum:
                best_2 = best_1
                best_3 = best_2
                best_1 = sum
            else:
                if best_2 < sum:
                    best_3 = best_2
                    best_2 = sum
                else:
                    if best_3 < sum:
                        best_3 = sum
            sum = 0
    print('Elf number 1 is carrying ' + str(best_1) + ' calories')
    print('Elf number 2 is carrying ' + str(best_2) + ' calories')
    print('Elf number 3 is carrying ' + str(best_3) + ' calories')
    print('The sum of the calories of the 3 best Elves is ' + str(best_1 + best_2 + best_3))
