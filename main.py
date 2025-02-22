import random
import time

print("Welcome to number guesser ;). I am going to pick a number from 1 to 20.See if you guess the number in correct from 1 to 20.")
time.sleep(1)

print("picking number...")
time.sleep(1.7)

guess = int(input("whats your guess ?: "))
correct_number = random.randint(1, 20)
guess_count = 1

while guess != correct_number:
  guess_count += 1

  if guess < correct_number:
    guess = int(input("Wrong you need to guess higher. Whats your guess ?: "))  
  else:
    guess = int(input("Wrong you need to guess lower. Whats your guess ?: "))

print(f'Congrats! The right answer was {correct_number}. It took you {guess_count} guesses.')