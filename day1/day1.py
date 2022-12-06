best_calories = 0
sum = 0

with open('day1.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines();
    for line in lines:
        if line.strip():
            sum += int(line);
        else:
            if best_calories < sum:
                best_calories = sum
            sum = 0
    print(best_calories)
