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

numbers = []
counterA = 0
counterB = [0,0,0]
for game in games: # ['Game 1', ['3blue', '4red'], ['1red', '2green', '6blue'], ['2green']]
    for i in range(len(game)-1):
            for hand in game[i+1]:
                split_str = re.findall(r'\d+|\D+', hand)
                if int(split_str[0]) > blue and split_str[1] == "blue":
                    game.append([1])
                if int(split_str[0]) > red and split_str[1] == "red" :
                    game.append([1])
                if int(split_str[0]) > green and split_str[1] == "green":
                    game.append([1])

    if isinstance(game[len(game)-1][0], int):
        pass
    else:
        numbers.append(game[0])
        counterA = game[0] + counterA

print(f"{counterA}")