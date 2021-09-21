"""Choose Your Own Adventure Football Game."""

__author__ = "730408740"

# import packages
from random import randint

# define global variables
points: int
player: str
greet_done: int = 0
FOOTBALL: str = "\U0001F3C8"
FIELD_GOAL: str = "\U0001F64C"


def greet() -> None:
    """Welcome message and player name."""
    print(f"Welcome to the UNC Football Touchdown Challenge! {FOOTBALL}")
    print("You pick the play and see if you can score against the CPU!")
    global player
    player = input("Enter Player Name: ")
    global greet_done
    greet_done = 1
    return None


def one_play_touchdown() -> None:
    """Primary pass/run/score game mode."""
    print(f"Hi {player}, welcome to the 1-play touchdown!")
    print("Pick a play and see if you can score against the defense!")
    play: int = int(input("Choose your play: run (1) or pass (2) "))
    defense = randint(1, 2)
    if play == defense:
        print("No Touchdown")
    else:
        print(f"TOUCHDOWN! {FOOTBALL}")
        global points
        points += 7
    return None

# pick play
# make run = 1 and pass = 2
# pick defense
# if play == defense, print a random message
# if play != defense, print TOUCHDOWN
# print points


def field_goal_kick(points: int) -> int:
    """Secondary field goal kicking game mode."""
    print(f"Welcome, {player}, to the field goal kicking challenge!")
    print("Choose to kick a field goal between 17-59 yards.")
    print("Longer kicks are harder to make, but see how good of a kicker you are!")
    dist: int = int(input("Choose your field goal distance (17-59): "))
    if dist < 30:
        if dist >= 17:
            prob: int = randint(1, 10)
            if prob <= 9:
                print(f"It's Good! {FIELD_GOAL}")
                points += 3
            else:
                print("No Good")
    else:
        if dist < 50:
            if dist < 40:
                prob: int = randint(1, 10)
                if prob <= 7:
                    print(f"It's Good {FIELD_GOAL}")
                    points += 3
                else:
                    print("No Good")
            else:
                prob: int = randint(1, 10)
                if prob <= 6:
                    print(f"It's Good {FIELD_GOAL}")
                    points += 3
                else:
                    print("No Good")
        else:
            prob: int = randint(1, 10)
            if prob <= 5:
                print(f"It's Good {FIELD_GOAL}")
                points += 3
            else:
                print("No Good")
    return points

# print welcome message
# pick distance
# randint make or miss
# if randint <= x, print It's Good
# if randint > x, print No Good


def end_game() -> None:
    """The end of the game."""
    done: int = int(input("Are you sure you want to quit? Choose Yes (0) or No (1) "))
    if done == 0:
        print(f"Goodbye, {player}, you played well today!")
        print(f"Score: {player} - {points} \n CPU: 0")


# define main function
def main() -> None:
    """The program's entrypoint."""
    global player
    global points
    points = 0
    greet()
    i = 0
    while i < 1:
        print(f"Score: {player} - {points} \n CPU: 0")
        mode: int = int(input("Choose your game mode: Quit (0), One Play Touchdown (1) or Field Goal Kicker (2) "))
        if mode == 0:
            i = 1
            end_game()
        else:
            if mode == 1:
                one_play_touchdown()
            else:
                points = field_goal_kick(points)

# 3 possible paths:
# 1) custom procedure, ask for input, reassign points global var, 1 pt per choice
# 2) function, int param/return val, pass points as arg to fun call, return points
# 3) end game, print goodbye message, show total accumulated points


if __name__ == "__main__":
    main()