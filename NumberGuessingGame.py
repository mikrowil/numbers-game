import random
import math

print("Hello, and welcome to the numbers guessing game! Select a range of numbers")
lower_bounds = input("Please Enter the lower bounds: ")
higher_bounds = input("Please Enter the higher bounds: ")
attempts = int(input("Please enter the number of attempts: "))
number = math.floor((random.random() * int(higher_bounds)) + int(lower_bounds))

is_game_on = True

while is_game_on:
    if attempts <= 0:
        print("Sorry you ran out of attempts")
        break

    guess = int(input("Number of attempts left: {}, What is your guess: ".format(attempts)))

    if guess == number:
        print("You Win!!")
        break
    elif guess > number:
        print("Too high")
    elif guess < number:
        print("Too low")

    attempts = attempts - 1
