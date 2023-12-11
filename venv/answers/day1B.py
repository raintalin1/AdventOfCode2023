import fileRead
import logging as log

log.basicConfig(level=log.DEBUG,filename ="log.log", filemode="w")

# go thru adding one letter to an array
# if its a word to a numeber find that number and use it
# if its a number use it
# do the same with the last digit

unprocessed = fileRead.readFile("day1.txt").returnList(2)
numberdict = {
    "zero":0,
    "one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9
}

arrhold = ""
numhold = []

class sort():
    def __init__(self, line, rev):
        arrhold = ""
        for i in line:
            log.debug(f"-i: {i}")

            for num in numberdict:
                if num in arrhold: #if str lines up with a dict key
                    if rev == 0:
                        numhold.append(arrhold)

                    elif rev == 1:
                        numhold.append(arrhold[::-1])


                    line
                    i=""
                    break

            if i.isdigit():
                    numhold.append(i)
                    break

            arrhold = f"{arrhold}{i}"
            log.debug(f"*arrhold: {arrhold}\n"
                        f"%line: {line}")
        


for line in unprocessed:# when both breaks

    sort(line, 0)
    #sort(line[::-1], 1)

print(numhold)

print(unprocessed)