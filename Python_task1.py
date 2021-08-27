from random import *
from copy import *


def score_cal(x1, y1, x2, CrDgCrPs, CrDgWrPs):
    if x2 == x1:
        print("You have guessed the number correctly. You won the game.")
        return 1
    else:
        for i in range(0, 4):
            if x2[i] in y1:
                if x2[i] == x1[i]:
                    CrDgCrPs.append(x2[i])
                else:
                    CrDgWrPs.append(x2[i])
                y1[y1.index(x2[i])] = -35487
        print(len(CrDgCrPs), " correct digits at correct position: ", CrDgCrPs)
        print(len(CrDgWrPs), " correct digits at wrong position ", CrDgWrPs)
        return 0


def result(ch):
    while ch == 1:
        ran, score = randint(1000, 9999), 20
        x1, nog = [int(i) for i in str(ran)], 15
        while nog > 0:
            y1, CrDgCrPs, CrDgWrPs = deepcopy(x1), [], []
            guess = int(input("Guess the 4 digit number : "))
            x2 = [int(i) for i in str(guess)]

            rstd=score_cal(x1, y1, x2, CrDgCrPs, CrDgWrPs)

            if(rstd==1):
                score+=5
                break
            else:
                score-=2
            nog -= 1
            print("Sorry wrong number. Guess again.\nGuesses left : ",nog)

        print("Your score is : ", score)
        ch = int(input("You have finished the game. Do you want to play again?\n1 - Yes\n0 - No\n"))


result(ch = int(input("Do you want to play the MASTERMIND GAME?\n1 - Yes\n0 - No\n")))
