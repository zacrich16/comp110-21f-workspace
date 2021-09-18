"""Choose Your Own Adventure Football Game."""

__author__ = "730408740"

# import packages
from random import randint

# define global variables
points: int = 0
player: str

# define greet function and welcome message
def greet() -> None:
    """Welcome message and player name."""
    print("Welcome to the UNC Football Touchdown Challenge!")
    print("You pick the play and see if you can score against the CPU!")
    global player
    player = input("Enter Player Name: ")

def op_1() -> None:


# define main function
def main() -> None:
    """The program's entrypoint."""
    greet()


def one_play_touchdown() -> None:
    """Primary pass/run/score game mode."""
    print(f"Hi {player}, welcome to the 1-play touchdown!")
    print("Pick a play and see if you can score against the defense!")
    play: int = int(input("Choose your play: run (1) or pass (2)"))
    defense = randint(1, 2)
    if play == defense:
        print("No Touchdown")
    else:
        print("TOUCHDOWN!")
        global points
        points += 7
        print(f"Score: {player} - {points} \n CPU: 0")
    again: int = int(input("Play again? Choose yes (0) or no (1)")
    if again == 0:
        one_play_touchdown()

# pick play
# make run = 1 and pass = 2
# pick defense
# if play == defense, print a random message
# if play != defense, print TOUCHDOWN
# print points
# ask to play again

# 3 possible paths:
# 1) custom procedure, ask for input, reassign points global var, 1 pt per choice
# 2) function, int param/return val, pass points as arg to fun call, return points
# 3) end game, print goodbye message, show total accumulated points
    

if __name__ == "__main__":
    main()