import fileRead

unprocessed = fileRead.readFile("day1.txt").returnList(1)

processed = []
for i in unprocessed:
    numbers = list(filter(str.isdigit, i))
    if len(numbers)>=2:
        processed.append([numbers[0], numbers[len(numbers)-1]])
    else:
        processed.append([numbers[0], numbers[0]])

answer = 0
for i in range(len(processed)):
    answer = answer+int(processed[i][0]+processed[i][1])

print(answer)