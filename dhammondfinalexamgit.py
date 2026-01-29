print("Menu")
print("Option 1: To see a joke")
print("Option 2: To see your favorite food printed a certain number of times")
print("Option 3: Play a Guessing Game")
y= int(input("Enter 1, 2, or 3 to choose a menu option: "))
if (y == 1):
    print("what did the horse say after it tripped?")
    print("Help! I've fallen and I can't giddy-up!")
if (y== 2):
    food = input("What is your favorite food? :")
    for i in range (20):
        print(food)
if (y == 3):
    print("Let's play a guess my number game")

    secretnumber = 0
    x = -1

    while x != secretnumber:
        x= -1

        while x < 0 or x > 10:
            x = float(input("Enter a number in the range of 0 and 10: "))

        if x > secretnumber:
            print("Your guess is too high", "try again")

        else:
            print("You won! You must be a mind reader")
