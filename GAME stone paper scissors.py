import random
lst = ['s', 'p', 'sci']

chance = 5
no_of_chance = 0
computer_point = 0
human_point = 0

print("\t\t\t STONE , PAPER , SCISSORS\t\t\t")
print(" \n s for stone \n p for paper \n sci for scissors\n")

while no_of_chance < chance:

    _input = input('stone,paper,scissor')
    _random = random.choice(lst)

    if _input == _random:
        print("Tie ...Both scored 0")

    elif _input == "s" and _random == "p":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess {_random} \n")
        print("computer won!!\n")
        print(f"your point {human_point} computer point {computer_point}\n")

    elif _input == "s" and _random == "sci":
        human_point = human_point + 1
        print(f"your guess {_input} and computer guess {_random} \n")
        print("human won a point!!\n")
        print(f"your point {human_point} computer point {computer_point}\n")

    elif _input == "p" and _random == "s":
        human_point = human_point + 1
        print(f"your guess {_input} and computer guess {_random} \n")
        print("human won a point!!\n")
        print(f"your point {human_point} computer point {computer_point}\n")

    elif _input == "p" and _random == "sci":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess {_random} \n")
        print("computer won!!\n")
        print(f"your point {human_point} computer point {computer_point}\n")

    elif _input == "sci" and _random == "s":
        computer_point_point = computer_point + 1
        print(f"your guess {_input} and computer guess {_random} \n")
        print("computer won a point!!\n")
        print(f"your point {human_point} computer point {computer_point}")

    elif _input == "sci" and _random == "p":
        human_point_point = human_point + 1
        print(f"your guess {_input} and computer guess {_random} \n")
        print("human won a point!!\n")
        print(f"your point {human_point} computer point {computer_point}\n")

    else:
        print("you have wrong choice")

    no_of_chance = no_of_chance + 1
    print(f'{chance - no_of_chance} left out of {chance}')

print("GAME OVER")

if computer_point == human_point:
    print("TIE")

elif computer_point < human_point:
    print("HUMAN WON")

else:
    print("COMPUTER WON")


print(f"final result : your points are {human_point} computer points are {computer_point}")

f







