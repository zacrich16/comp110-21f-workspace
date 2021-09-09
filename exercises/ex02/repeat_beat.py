"""Repeating a beat in a loop."""

__author__ = "730408740"


beat: str = input("What beat do you want to repeat? ")
repeat: int = int(input("How many times do you want to repeat it? "))
i = 1
song: str = ""

if repeat <= 0:
    print("No beat...")
else:
    while i <= repeat:
        if i == repeat:
            song = song + beat
        else: 
            song = song + beat + " "
        i = i + 1
    print(song)