import random
import time


def dice():
    gameover= False
    while gameover == False:
        player = random.randint(1,6)
        print("You rolled " + str(player) )

        ai = random.randint(1,6)
        print("The computer rolls...." )
        time.sleep(2)
        print("The computer has rolled a " + str(ai) )

        if player > ai :
            print("You win")  # notice indentation
        else:
            print("You lose")

        print("Quit? Y/N")
        continue1 = input()

        if continue1 == "Y" or continue1 == "y":
            exit()
            gameover= True
        elif continue1 == "N" or continue1 == "n":
            gameover= False
        else:
            print("I did not understand that. Playing again.")


d=dice()