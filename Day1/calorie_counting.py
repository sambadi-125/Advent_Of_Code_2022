file = open("data.txt", "r")
topCalories = [0,0,0]
temporalCalories = 0

line = file.readline()

while line:
    line = line.strip()

    if line:
        temporalCalories += int(line)

    line = file.readline()

    if line == "\n" or not line:
        if temporalCalories > topCalories[0]:
            topCalories[2] = topCalories[1]
            topCalories[1] = topCalories[0]
            topCalories[0] = temporalCalories
        elif temporalCalories > topCalories[1]:
            topCalories[2] = topCalories[1]
            topCalories[1] = temporalCalories
        elif temporalCalories > topCalories[2]:
            topCalories[2] = temporalCalories

        temporalCalories = 0

file.close()

print(sum(topCalories))
