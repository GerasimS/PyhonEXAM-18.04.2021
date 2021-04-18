#1
'''
setCheck = {'a2','b3','c3','d4','f2','g2','h3'}

def safe_pawns(setCheck: set) -> set:
    row_numbers = []
    list_of_pawns = list(setCheck)
    letters_string = "abcdefgh"
    safe_pawns = []
    #Проверява за съседи, които пазят
    for pawn in list_of_pawns:
        if pawn[0] == "a":
            if letters_string[1] + str(int(pawn[1])-1) in list_of_pawns:
                safe_pawns.append(pawn)
        elif pawn[0] == "h":
            if letters_string[6] + str(int(pawn[1])-1) in list_of_pawns:
                safe_pawns.append(pawn)
        else:
            if ((letters_string[letters_string.index(pawn[0]) + 1] + str(int(pawn[1]) - 1))
            in list_of_pawns):
                 safe_pawns.append(pawn)
            elif (letters_string[letters_string.index(pawn[0]) - 1] + str(int(pawn[1]) - 1)
            in list_of_pawns):
                safe_pawns.append(pawn)
    #Маха пешките от най-долния ред
    for pawn in list_of_pawns:
        row_numbers.append(pawn[1])
    lowest_row_indexes = []
    for i, row_number in enumerate(row_numbers):
        if row_number == min(row_numbers):
            lowest_row_indexes.append(i)
    for i, lowest_row_index in enumerate(lowest_row_indexes):
        del list_of_pawns[lowest_row_index - i]
        del row_numbers[lowest_row_index - i]
    return set(safe_pawns)

setSafe = safe_pawns(setCheck)
'''

#2
'''
dumi = ['i', 'when', 'begun', 'near']
text = "When I was One I had begun When I was Two I was nearly new"


def nwords(dumi: list, text: str) -> dict:
    dicdumi = { duma : 0 for duma in dumi }
    for d in dicdumi:
        dicdumi[d] = text.lower().split().count(d)
    print(dicdumi)

nwords(dumi, text)
'''

#3
'''
l1 = [1,13,99,1287]

def checkAscending(l1: list) -> bool:
    n = len(l1)
    if n == 1 or n == 0:
        return True
    return l1[0] <= l1[1] and checkAscending(l1[1:])

print(checkAscending(l1))
'''

#4

import random

class Time():
    timen = "00:00"

    def __init__(self):
        self.timen = str(random.randrange(0,23)) + ':' + str(random.randrange(0,5)) + str(random.randrange(0,9))
    
    
    def changeTime(self, new_time: str):
        if int(new_time[:-3]) < 24 and int(new_time[:-3]) >= 0 and int(new_time[3:]) < 60 and int(new_time[3:]) >= 0 and (new_time[1] == ":" or new_time[2] == ":"):
            self.timen = new_time
        else:
            print("Incorrect format!")
    
    def addTime(self, time1: int):
        if time1 >= 1 and time1 <= 120:
            if time1 == 120:
                self.timen = str(int(self.timen[:-3]) + 2) + self.timen[2:]
            elif time1 > 59:
                self.timen = str(int(self.timen[:-3]) + 1) + ":" + str(int(self.timen[3:]) + (time1 - 60))
            else:
                self.timen = self.timen[:-2]+ str(int(self.timen[3:]) + time1)
            if int(self.timen[:-3]) > 24:
                self.timen = str(int(self.timen[:-3]) - 24) + self.timen[2:]
        else:
            print("Enter a number between 0 and 121!")

    def printTime(self):
        if int(self.timen[:-3]) > 12:
            print("The time is " + str(int(self.timen[:-3]) - 12) + self.timen[2:] + " p.m.")
        else:
            print("The time is " + self.timen + " a.m.")


time1 = Time()
time1.changeTime('23:24')
time1.printTime()
time1.addTime(120)
time1.printTime()



