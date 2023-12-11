import fileRead
import string
import re

unprocessed = fileRead.readFile("day2.txt").returnList(3)

red = 12
green = 13
blue = 14

games = []
for game in unprocessed:
   games.append(game.split(":"))

for gameset in games:
    gameset[0] = int(gameset[0].replace("Game ", ''))
    gameset[1] = ''.join(list(map(lambda x: x.strip(), gameset[1].split())))    #removes spaces
    gameset[1] = gameset[1].split(";")  #splits the sets from each other
    for set in gameset[1]:
        gameset.append(set.split(","))#splits the rounds in the set
    gameset.pop(1)

numbers = 0
counterB = []
cubeMin = [0,0,0] # 0: blue, 1: red, 2: green
for game in games: # ['Game 1', ['3blue', '4red'], ['1red', '2green', '6blue'], ['2green']]
    for i in range(len(game)-1):
            for hand in game[i+1]:

                split_str = re.findall(r'\d+|\D+', hand)
                split_str[0]= int(split_str[0])

                if (split_str[1] == "blue") and (cubeMin[0] < split_str[0]):
                    cubeMin[0] = split_str[0]
                elif split_str[1] == "red" and cubeMin[1] < split_str[0]:
                    cubeMin[1] = split_str[0]
                elif split_str[1] == "green" and cubeMin[2] < split_str[0]:
                    cubeMin[2] = split_str[0]
    counterB.append(cubeMin[0]*cubeMin[1]*cubeMin[2])
    cubeMin = [0, 0, 0]

for num in counterB:
    numbers = numbers + num

print(numbers)