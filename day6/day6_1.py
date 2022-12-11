with open('day6.txt', 'r', encoding="utf-8") as f:
    data = f.read().rstrip()
    #data[:4] takes the first 4 characters and puts them in a list
    to_check = list(data[:4])
    #Looping from the fourth character to the length of the string (all the characters in the .txt)
    for i in range(4,len(data)):
        #When there will be 4 items in the list as a set (that gives only unique elements) that 
        #are all different; then prints the count until the marker 
        if len(set(to_check)) == 4:
            print(i);
            break
        #Pops away the first character (that has been checked)
        to_check.pop(0)
        #Inserts a new item to check into the list
        to_check.append(data[i])
    
