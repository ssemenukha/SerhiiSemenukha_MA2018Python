import random


# Rock-paper-scissors-lizard-Spock template

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

choices = ["rock", "Spock", "paper", "lizard", "scissors"]


# helper functions
def name_to_number(name):
    return choices.index(name)


def number_to_name(number):
    return choices[number]


def rpsls(player_choice):
    # print a blank line to separate consecutive games
    print("")

    # print out the message for the player's choice
    print("Your choice: {}".format(player_choice))

    # convert the player's choice to player_number using the function name_to_number()
    player_choice_number = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    computer_choice_number = random.randrange(0, 5)

    # convert comp_number to comp_choice using the function number_to_name()
    computer_choice = number_to_name(computer_choice_number)

    # print out the message for computer's choice
    print("Computer choice: {}".format(computer_choice))

    # compute difference of comp_number and player_number modulo five
    duel = (computer_choice_number - player_choice_number) % 5

    # use if/elif/else to determine winner, print winner message
    if duel == 0:
        print("Friendship wins!")
    elif duel <= 2:
        print("Computer wins!")
    else:
        print("You wins!")


# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric
