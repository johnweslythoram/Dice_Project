import random
import time

l = [["┌─────────┐",
      "|         |",
      "|    ●    |",
      "|         |",
      "└─────────┘"]
    , ["┌─────────┐",
       "| ●       |",
       "|         |",
       "|       ● |",
       "└─────────┘"]
    , ["┌─────────┐",
       "| ●       |",
       "|    ●    |",
       "|       ● |",
       "└─────────┘"]
    , ["┌─────────┐",
       "| ●     ● |",
       "|         |",
       "| ●     ● |",
       "└─────────┘"]
    , ["┌─────────┐",
       "| ●     ● |",
       "|    ●    |",
       "| ●     ● |",
       "└─────────┘"]

    , ["┌─────────┐",
       "| ●     ● |",
       "| ●     ● |",
       "| ●     ● |",
       "└─────────┘"]]


def main():
    print("********** Select one of the game below to play with computer **********")
    print()
    print("1. Dice Simulatar")
    print("2. Boston Game")
    print("3. Lowest or Highest Game")
    print("4. Lowest out game")
    print("5. Exit")
    print()
    print()
    s = int(input("Enter your selection: "))
    if s == 1:
        DiceSimulator()
    elif s == 2:
        BostonGame()
    elif s == 3:
        LowestOrHighest()
    elif s == 4:
        LowestOut()
    elif s == 5:
        exit()
    else:
        print("********** Invalid selection **********")
        print()
        print()
        print()
        print("please wait redirecting to games section!!!!")
        time.sleep(3)
        main()


def DiceSimulator():
    d1 = True
    while d1:
        dice = []
        print()
        x = int(input("How many dice you want to roll : "))
        for i in range(x):
            r = random.randint(0, 5)
            dice.append(r)
        print("Wait for 2 sec dice is rolling!!!")
        time.sleep(2)
        print()
        print()
        print()
        for line in range(5):
            for die in dice:
                print(l[die][line], end="   ")
            print()
        print()
        print("Do you want to roll again? or do you want to quite!")
        d2 = str(input("To play press (p/P) or to quite press any chracter : "))
        if d2.lower() != 'p':
            d1 = False
            print()
            print()
            print()
            print("please wait redirecting to games!!!!")
            time.sleep(3)
            main()


def exit():
    print()
    print()
    print("Thanks for playing!")


def BostonGame():
    time.sleep(1)
    print("           Boston Game           ")
    print()
    print()
    print("    About the Game")
    b1 = '''    Each player has three dice to start with. One player goes first .

    They roll three dice. Take out the highest number. Roll the remaining two dice, take out the highest number again, and then roll the last dice one more time.

    Then you add up your score.

    So, as an example, you might roll 3, 2, and 5. Take out the 5. Then you roll the lower two dice.

    You get 1 and 4. Take out the 4.

    Lastly, you roll a 3. So your score is 5, 4, and 3. Add them up to get 12.
    
    Write down 12 on the scoresheet.

    Then the next person goes. Keep on adding up your scores.
    
    Compare both the scores and declare the winner'''
    print(b1)

    print()
    time.sleep(3)

    def Boston(k):
        for i in l[k]:
            print(i)

    def play(z):
        print("To play Round-", z + 1, "Press (P/p) or to Quite press any other character : ")
        b = str(input())
        if b.lower() == 'p':
            return 1
        if b.lower() != 'p':
            print("If you want to quit game or else continue!!!!")
            print("To continuee!!!! Press the key (p/P) or to quite press any other character")
            b1 = str(input())
            if b1 == 'p':
                return 1
            else:
                print()
                print()
                print()
                print("please wait redirecting to games!!!!")
                time.sleep(3)
                main()

    def play1(z):
        print("To play Round-", z + 1, "Press (P/p) or to Quite press any other character : ")
        b = str(input())
        if b.lower() == 'p':
            return 1
        if b.lower() != 'p':
            print("If you quite computer wins!!!!")
            print("To continuee!!!! Press the key (p/P) or to quite press any other character")
            b1 = str(input())
            if b1 == 'p':
                return 1
            else:
                print("********** Computer wins **********")
                print()
                print()
                print()
                print("please wait redirecting to games!!!!")
                time.sleep(3)
                main()

    dice = []
    dice2 = []
    sum_b = 0
    sum_b1 = 0
    stop = 0
    print("Do you want to play or give first turn to computer")
    turn = str(input("press (c/C) for computer turn or any other character for your turn : "))
    if turn.lower() == 'c':
        # computer turn
        for i in range(3):
            d = []
            for j in range(i, 3):
                a = random.randint(0, 5)
                d.append(a)
            dice2.append(d)

        for z in range(3):
            print("Round-", z + 1)
            for line in range(5):
                for die in dice2[z]:
                    print(l[die][line], end="    ")
                print()
            k = max(dice2[z])
            sum_b1 += k
            print("Round-", z + 1, "Highest Number of dice")
            Boston(k)
            time.sleep(2)

        print("Wait for 5 seconds to start your turn!!!!!!!!")
        time.sleep(5)
        # human turn
        for i in range(3):
            d = []
            for j in range(i, 3):
                a = random.randint(0, 5)
                d.append(a)
            dice.append(d)
        for z in range(3):
            print("Round-", z + 1)
            b2 = play1(z)
            if b2 == 1:
                for line in range(5):
                    for die in dice[z]:
                        print(l[die][line], end="    ")
                    print()
            else:
                print("********** Computer Wins **********")
                stop = 1
                break
            k = max(dice[z])
            sum_b += k
            print("Round-", z + 1, "Highest Number of dice")
            Boston(k)

    if turn.lower() != "c":
        for i in range(3):
            d = []
            for j in range(i, 3):
                a = random.randint(0, 5)
                d.append(a)
            dice.append(d)

        for z in range(3):
            print("Round-", z + 1)
            b2 = play(z)
            if b2 == 1:
                for line in range(5):
                    for die in dice[z]:
                        print(l[die][line], end="    ")
                    print()
            else:
                print("Ended")
                break
            k = max(dice[z])
            sum_b += k
            print("Round-", z + 1, "Highest Number of dice")
            Boston(k)

        print(sum_b + 3)
        print("Wait for 5 seconds to start computer turn!!!!!!!!")
        time.sleep(5)

        # computer turn
        for i in range(3):
            d = []
            for j in range(i, 3):
                a = random.randint(0, 5)
                d.append(a)
            dice2.append(d)

        for z in range(3):
            print("Round-", z + 1)
            for line in range(5):
                for die in dice2[z]:
                    print(l[die][line], end="    ")
                print()
            k = max(dice2[z])
            sum_b1 += k
            print("Round-", z + 1, "Highest Number of dice")
            Boston(k)
            time.sleep(2)

    if stop == 0:
        print("Calculating Boston Score")
        print("Loading!!!!! Please Wait!!!")
        time.sleep(4)
        print("********** Your score : ", sum_b + 3, " **********")
        print("********** Computer score : ", sum_b1 + 3, " **********")
        if sum_b1 > sum_b:
            print("********** Computer Wins **********")
        else:
            print("********** You Win the Game! Congratulations! **********")
        print()
        print()
        print()
        print("please wait redirecting to games!!!!")
        time.sleep(3)
        main()


def LowestOrHighest():
    time.sleep(1)
    print()
    print("           Lowest or Highest Game           ")
    print()
    print()
    m1 = '''This is a rare 2 player dice game on this list. Each player sits with six dice, to begin with.

Choose one player to go first. They roll just one dice. The other player must then call ‘higher’ or ‘lower’. Then they roll one dice themselves.

If their dice show a number that corresponds with what they have said, then they win both dice.

For example, if the first player rolls a 2, and the second player says ‘higher’, then the second player will win if a 3, 4, 5, or 6 is thrown.'''
    print(m1)
    print()
    time.sleep(3)
    print("Do you want to play or give first turn to computer")
    turn1 = str(input("press (c/C) for computer turn or any other character for your turn : "))
    a5 = a6 = ''
    stop1 = 0
    a2 = random.randint(0, 5)
    if turn1.lower() != 'c':

        a3 = str(input(("It's your turn press (p/P) for roll the dice or press any character to quite the game : ")))
        if a3.lower() != 'p':
            print("Do you want to quite game or else do you want to continue!")
            a5 = str(input(("To continue press (p/P) or press any character to quite the game : ")))
            if a5.lower() == 'p':
                for i in l[a2]:
                    print(i)
                time.sleep(1)
            else:
                print("You quit the game")

                print()
                print()
                print()
                print("please wait redirecting to games!!!!")
                time.sleep(3)
                main()
        if a3.lower() == 'p':
            for i in l[a2]:
                print(i)
            time.sleep(1)
        print("Please wait its computer turn!!!!!!!")
        time.sleep(2)
        if a2 >= 4:
            a5 = 'Lowest'
            a6 = 'Higher'
            print("Computer calls Lower!")
        else:
            a5 = 'Higher'
            a6 = 'Lowest'
            print("Computer calls Higher!")
        print("Computer is rolling dice wait for 1 sec!")
        time.sleep(1)
        a4 = random.randint(0, 5)
        for i in l[a4]: print(i)

        print("Calculating Lowest or Hihest Score")
        print("Loading!!!!! Please Wait!!!")
        time.sleep(4)
        print("********** Your score : ", a2 + 1, " **********")
        print("********** Computer score : ", a4 + 1, " **********")
        if a4 == a2:
            print("********** Drawn **********")
        elif a5 == 'Lowest' and a4 < a2:
            print("********** Computer Wins **********")

            print("Computer chooses", a5, "so computer score is", a5, "than you.")
        elif a5 == 'Higher' and a4 > a2:
            print("********** Computer Wins **********")
            print("Computer chooses", a5, "so computer score is", a5, "than you.")
        else:
            print("********** You Win the Game! Congratulations! **********")
        print()
        print()
        print()
        print("please wait redirecting to games!!!!")
        time.sleep(3)
        main()



    else:
        print("Please wait its computer turn!!!!!!!")
        time.sleep(2)
        print("Computer is rolling dice wait for 1 sec!")
        time.sleep(1)
        a4 = random.randint(0, 5)
        for i in l[a4]: print(i)

        print("Please wait for your turn!!!")
        time.sleep(2)
        print("Please select Lowest or Highest")
        a7 = str(input("For lowest press (l/L) or for Highest press (h/H) : "))
        if a7 == 'l':
            a5 = 'Lowest'
            a6 = 'Highest'
        else:
            a5 = 'Highest'
            a6 = 'Lowest'
        time.sleep(2)
        a3 = str(input(("It's your turn press (p/P) for roll the dice or press any character to quite the game : ")))
        if a3.lower() != 'p':
            print("If you quite the game computer will win the game!!!")
            a5 = str(input(("To continue press (p/P) or press any character to quite the game : ")))
            if a5.lower() == 'p':
                for i in l[a2]:
                    print(i)
                time.sleep(1)
            else:
                print("********** Computer wins **********")
                stop1 = 1
                print()
                print()
                print()
                print("please wait redirecting to games!!!!")
                time.sleep(3)
                main()
        if a3.lower() == 'p':
            for i in l[a2]:
                print(i)
            time.sleep(1)

        print("Calculating Lowest or Hihest Score")
        print("Loading!!!!! Please Wait!!!")
        time.sleep(4)
        print("********** Your score : ", a2 + 1, " **********")
        print("********** Computer score : ", a4 + 1, " **********")
        if a4 == a2:
            print("********** Drawn **********")
        elif a5 == 'Lowest' and a2 < a4:
            print("********** You Win the Game! Congratulations! **********")

            print("You chooses", a5, "so You score is", a5, "than Computer.")

        elif a5 == 'Highest' and a2 > a4:
            print("********** You Win the Game! Congratulations! **********")

            print("You chooses", a5, "so You score is", a5, "than Computer.")
        else:
            print("********** Computer Wins **********")

        print()
        print()
        print()
        print("please wait redirecting to games!!!!")
        time.sleep(3)
        main()


def LowestOut():
    time.sleep(1)
    print()
    print("           Lowest Out Game           ")
    print()
    print()
    m = '''This is a quick dice game where players are rapidly knocked out until you have one winner.

Each player starts with 6 dice. They all roll the six dice and count up the total of all the quantities shown on their dice.

Quite simply, the player with the lowest score loses that round and is knocked out.'''
    print(m)
    print()
    time.sleep(3)
    dice1 = []
    dice2 = []
    stop = 0
    print("Do you want to play or give first turn to computer")
    turn1 = str(input("press (c/C) for computer turn or any other character for your turn : "))
    if turn1.lower() != 'c':
        print("It's your turn please wait to roll the dice!")
        time.sleep(1)
        a7 = str(input("To roll the dice press (p/P) or to quite press any character :"))
        if a7.lower() != "p":
            print("Do you want to quite game or else do you want to continue!")
            a8 = str(input(("To continue press (p/P) or press any character to quite the game : ")))
            if a8.lower() == 'p':
                for i in range(6):
                    r = random.randint(0, 5)
                    dice1.append(r)

                for line in range(5):
                    for die in dice1:
                        print(l[die][line], end="")
                    print()
            else:
                print("You quite the game")
                main()
        if a7.lower() == "p":
            for i in range(6):
                r = random.randint(0, 5)
                dice1.append(r)

            for line in range(5):
                for die in dice1:
                    print(l[die][line], end="")
                print()

        time.sleep(1.5)
        print("Please wait its computer turn!!!!!!!")
        time.sleep(2)
        print("Computer is rolling dice wait for 1 sec!")
        time.sleep(2)
        for i in range(6):
            r = random.randint(0, 5)
            dice2.append(r)

        for line in range(5):
            for die in dice2:
                print(l[die][line], end="")
            print()

    if turn1.lower() == 'c':
        print("Its computer turn, Please wait for 2 sec!!!!!!!")
        time.sleep(2)
        print("Computer is rolling dice wait for 1 sec!")
        time.sleep(2)
        for i in range(6):
            r = random.randint(0, 5)
            dice2.append(r)

        for line in range(5):
            for die in dice2:
                print(l[die][line], end="")
            print()
        time.sleep(2)

        print("It's your turn please wait to roll the dice!")
        time.sleep(1)
        a7 = str(input("To roll the dice press (p/P) or to quite press any character :"))
        if a7.lower() != "p":
            print("If you quite computer will win the game or else do you want to continue!")
            a8 = str(input(("To continue press (p/P) or press any character to quite the game : ")))
            if a8.lower() == 'p':
                for i in range(6):
                    r = random.randint(0, 5)
                    dice1.append(r)

                for line in range(5):
                    for die in dice1:
                        print(l[die][line], end="")
                    print()
            else:
                print("********** Computer Wins **********")
                stop = 1
                print()
                print()
                print()
                print("please wait redirecting to games!!!!")
                time.sleep(3)
                main()
        if a7.lower() == "p":
            for i in range(6):
                r = random.randint(0, 5)
                dice1.append(r)

            for line in range(5):
                for die in dice1:
                    print(l[die][line], end="")
                print()

    if stop == 0:
        print("Calculating Boston Score")
        print("Loading!!!!! Please Wait!!!")
        time.sleep(4)
        print("********** Your score : ", sum(dice1) + 6, " **********")
        print("********** Computer score : ", sum(dice2) + 6, " **********")
        if sum(dice2) + 6 > sum(dice1) + 6:
            print("********** Computer Wins **********")
        else:
            print("********** You Win the Game! Congratulations! **********")
    print()
    print()
    print()
    print("please wait redirecting to games!!!!")
    time.sleep(3)
    main()


main()
