# random number select krlo
import random

# score => 100 - (num of attempts * 5) 
# score => 100 - 5 * 3

computer_option = random.randint(1,100) #69
game_status = False

for i in range(10):
    num = int(input("Guess your number: ")) #69

    #
    if num not in range(1,100+1):
        print("Invalid Option")
    elif computer_option == num:
        print(f"Congrates you have won your score is {100 - (i*5)}")
        game_status = True
        break
    elif num > computer_option:
        print("You guessed too large number")
    else:
        print("You guessed too small number")

if game_status == False:
    print("You have lost the game")
    

