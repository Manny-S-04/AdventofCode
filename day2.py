with open("day2.txt", "r") as file:

    aocinput = [line for line in file]
    #aocinput = file.readline()

templist = []
for item in aocinput:
    nospace = item.replace(" ", "")
    noline = nospace.strip("\n")
    temp = list(noline)
    templist.append(temp)


def calc(rounds:list):
    score = 0
    for match in rounds:
        key = match[0]
        value = match[1]

        # Calculate the score based on the rules
        if key == 'A':
            if value == 'X':
                score += 4
            elif value == 'Y':
                score += 8
            elif value == 'Z':
                score += 3
        elif key == 'B':
            if value == 'X':
                score += 1
            elif value == 'Y':
                score += 5
            elif value == 'Z':
                score += 9
        elif key == 'C':
            if value == 'X':
                score += 7
            elif value == 'Y':
                score += 2
            elif value == 'Z':
                score += 6

    print("Total Score:", score)


def calc2(rounds:list):
    score = 0
    for match in rounds:
        key = match[0]
        value = match[1]

        # Calculate the score based on the rules
        if key == 'A':
            if value == 'X':
                score += 3
            elif value == 'Y':
                score += 4
            elif value == 'Z':
                score += 8
        elif key == 'B':
            if value == 'X':
                score += 1
            elif value == 'Y':
                score += 5
            elif value == 'Z':
                score += 9
        elif key == 'C':
            if value == 'X':
                score += 2
            elif value == 'Y':
                score += 6
            elif value == 'Z':
                score += 7

    print("Total Score:", score)


calc(templist)
calc2(templist)