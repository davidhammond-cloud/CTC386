def celsiusconversion(Fahrenheit):
    celsius= (Fahrenheit - 32) * 5/9
    return celsius

def play_game():
    computer = "rock"
    playing = True

print("Menu")
print("Option 1: To see a joke")
print("Option 2: To see your name printed a certain number of times")
print("Option 3: To see a positive quote")
print("Option 4: Play a Guessing Game")
print("Option 5: Convert temperature from Fahrenheit to Celsius")
print("Option 6: Play Rock, Paper, Scissor")
print("Option 7: Exit")

y= int(input("Enter 1, 2, 3, 4, 5, 6, or 7 to choose a menu option: "))
if (y == 1):
    print("what did the horse say after it tripped?")
    print("Help! I've fallen and I can't giddy-up!")
elif (y== 2):
    name = input(("What is your name? :"))
    for i in range (15):
        print(name)
elif (y == 3):
    x=int(input("Enter a number: "))
    print("Enter a number: ")
    for i in range (x):
        print("You don't have to know where the staircase is going to start climbing")
elif (y== 4):
    print("Let's play a guess my number game")

    secretnumber = 54
    x = -1

    while x != secretnumber:
        x= -1

        while x < 0 or x > 100:
            x = float(input("Enter a number in the range of 0 and 100: "))

        if x > secretnumber:
            print("Your guess is too high", "try again")

        elif (x < secretnumber):
            print("Your guess is too low", "try again")

        else:
            print("You won! You must be a mind reader")
elif (y == 5):
    x = int(input("Enter today's temperature in Fahrenheit: "))
    output=celsiusconversion(x)
    print("Today's temperature in celsius is ", output, "degrees")

elif (y == 6):
    computer = "rock"
    playing = True

    while playing:
        user = input("Enter rock, paper, scissors, or quit: ")

        if user == "quit":
            playing = False
            print("Thanks for playing!")

        elif (user == "rock") or (user == "paper") or (user == "scissors"):

            print("Computer chose:", computer)

            if user == computer:
                print("It's a tie!")

            elif ((user == "rock" and computer == "scissors") or 
                (user == "paper" and computer == "rock") or
                (user == "scissors" and computer == "paper")):
                print("You win!")

            else:
                print("Computer wins!")

            if computer == "rock":
                computer = "paper"
            elif computer == "paper":
                computer = "scissors"
            else:
                 computer = "rock"
                 print()

        else:
            print("Invalid input. Try again.\n")

# Start the game
    play_game()
elif (y == 7):
    print("Goodbye!")
