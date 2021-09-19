"""Choose Your Own Adventure Football Game."""

__author__ = "730408740"

# import packages
from random import randint

# define global variables
points: int = 0
player: str


def greet() -> None:
    """Welcome message and player name."""
    print("Welcome to the UNC Football Touchdown Challenge!")
    print("You pick the play and see if you can score against the CPU!")
    global player
    player = input("Enter Player Name: ")
    return None


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
    else:
        return None

# pick play
# make run = 1 and pass = 2
# pick defense
# if play == defense, print a random message
# if play != defense, print TOUCHDOWN
# print points
# ask to play again


def field_goal_kick(x: int) -> int:
    """Secondary field goal kicking game mode."""
    print(f"Welcome, {player}, to the field goal kicking challenge!")
    print("Choose to kick a field goal between 17-59 yards.")
    print("Longer kicks are harder to make, but see how good of a kicker you are!")
    dist: int = int(input("Choose your field goal distance (17-59): "))
    if dist < 30:
        if dist < 17:
            return None
        else:
            prob: int = randint(1, 2)
            if prob == 1:
                print("It's Good!")
                points += 3
                print(f"Score: {player} - {points} \n CPU: 0")
            else:
                print("No Good")
    else:
        if dist < 50:
            if dist < 40:
                prob: int = randint(1, 3)
                if prob == 1:
                    print("It's Good")
                    points += 3
                    print(f"Score: {player} - {points} \n CPU: 0")
                else:
                    print("No Good")
            else:
                prob: int = randint(1, 4)
                if prob == 1:
                    print("It's Good")
                    points += 3
                    print(f"Score: {player} - {points} \n CPU: 0")
                else:
                    print("No Good")
        else:
            prob: int = randint(1, 5)
                if prob == 1:
                    print("It's Good")
                    points += 3
                    print(f"Score: {player} - {points} \n CPU: 0")
                else:
                    print("No Good")
    again: int = int(input("Play again? Choose Yes (0) or No (1)")
    if again == 0:
        field_goal_kick(points)
    else:
        return points

# print welcome message
# pick distance
# randint make or miss
# if randint == 1, print It's Good
# if randint != 1, print No Good


def end_game() -> None:
    """The end of the game."""
    done: int = int(input("Are you sure you want to quit? Choose Yes (0) or No (1) "))
    if done == 0:
        print(f"Goodbye, {player}, you played well today!")
        print(f"Score: {player} - {points} \n CPU: 0")
        return None
    else:
        return None


# define main function
def main() -> None:
    """The program's entrypoint."""
    greet()
    mode: int = int(input("Choose your game mode: One Play Touchdown (1) or Field Goal Kicker (2) "))
    if mode == 1:
        one_play_touchdown()
    else:
        field_goal_kick(points)

# 3 possible paths:
# 1) custom procedure, ask for input, reassign points global var, 1 pt per choice
# 2) function, int param/return val, pass points as arg to fun call, return points
# 3) end game, print goodbye message, show total accumulated points
    

if __name__ == "__main__":
    main()