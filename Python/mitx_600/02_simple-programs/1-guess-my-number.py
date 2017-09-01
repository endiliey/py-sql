low = 0
guess = 50
hi = 100
print("Please think of a number between 0 and 100!")
while True:
    print("Is your secret number " + str(guess) + "?")
    char = input("Enter 'h' to indicate the guess is too high." +
                " Enter 'l' to indicate the guess is too low." +
                " Enter 'c' to indicate I guessed correctly. ")
    if char == 'l':
        low = guess
        guess = low + (hi - low) // 2
    elif char == 'h':
        hi = guess
        guess = low + (hi - low) // 2
    elif char == 'c':
        print("Game over. Your secret number was: " + str(guess))
        break
    else:
        print("Sorry, I did not understand your input.")