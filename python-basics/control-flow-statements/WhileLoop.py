# Variables oh how I love to play with them:

guess = 0
answer = 5

# Mini game that uses user input to check vs a hardcoded answer, when guessed correctly game is ended:

while answer != guess:
    guess = int(input('Make a guess: '))  # We know will get a string back so we cast it to integer

else:  # Only triggered if the while loop is ended without a break statement
    print('You guessed right!')
