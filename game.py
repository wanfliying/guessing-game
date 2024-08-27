import random

print("Welcome to Guess the Number Episode 1! [All random numbers are integers]")
i = 0
while i < 1:
    Rounds_not_confirmed = input("How many rounds do you want? ")
    if float(Rounds_not_confirmed) > 0:
        if float(Rounds_not_confirmed) // 1 == float(Rounds_not_confirmed):
            Rounds = str(Rounds_not_confirmed)
            i = 2
        else:
            print("Invalid Round #! Round # must be above 0 and has to be an integer.")
    else:
        print("Invalid Round #! Round # must be above 0 and has to be an integer.")
Round = 1
while Round <= int(Rounds):
    print("Round", Round)
    i = 0
    while i < 1:
        Minimum_not_confirmed = input("What is the range of the random number [Minimum]? ")
        if float(Minimum_not_confirmed) // 1 == float(Minimum_not_confirmed):
            Minimum = int(Minimum_not_confirmed)
            i = 2
        else:
            print("Invalid Minimum! Minimum must be an integer, not a decimal.")
    i = 0
    while i < 1:
        Maximum_not_confirmed = input("What is the range of the random number [Maximum]? ")
        if float(Maximum_not_confirmed) // 1 == float(Maximum_not_confirmed):
            Maximum = int(Maximum_not_confirmed)
            i = 2
        else:
            print("Invalid Maximum! Maximum must be an integer, not a decimal.")
    min_pos_guess = int(Minimum)
    max_pos_guess = int(Maximum)
    i = 0
    print("The number is in between " + str(Minimum) + " and " + str(Maximum) + ", inclusive.")
    Attempts = 0
    random_number = random.randint(int(Minimum), int(Maximum))
    while i < 1:
        Guess = input("What number do you want to guess? ")
        if float(Guess) // 1 == float(Guess):
            if int(Guess) >= int(min_pos_guess):
                if int(Guess) <= int(max_pos_guess):
                    Attempts += 1
                    if int(Guess) > int(random_number):
                        print("Too high! Try again.")
                        max_pos_guess = int(Guess)
                    elif int(Guess) < int(random_number):
                        print("Too low! Try again.")
                        min_pos_guess = int(Guess)
                    elif int(Guess) == int(random_number):
                        print("You got it! The number is " + str(random_number) + ".")
                        print("You guessed it in " + str(Attempts) + " attempts!")
                        break
                else:
                    print("Invalid Guess! Number must be between " + str(min_pos_guess) + " and " + str(max_pos_guess))
                    print("inclusive according to your guesses.")
            else:
                print("Invalid Guess! Number must be between " + str(min_pos_guess) + " and " + str(max_pos_guess))
                print("inclusive according to your guesses.")
        else:
            print("Invalid Guess! Number must be an integer, not a decimal.")
    Round += 1
print("Thanks for playing!")
