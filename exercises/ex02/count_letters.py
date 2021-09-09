"""Counting letters in a string."""

__author__ = "730408740"


letter: str = input("What letter do you want to search for?: ")
word: str = input("Enter a word: ")

i = 0
counter = 0
while i < len(word):
    if word[i] == letter:
        counter = counter + 1
    else:
        counter = counter
    i = i + 1
print("Count:", counter)