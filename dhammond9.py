#git hubtest comment
print("Menu")
print("Option 1: To see a joke")
print("Option 2: To see your name printed a certain number of times")
print("Option 3: To see a positive quote")
print("Option 4: Play a Guessing Game")
print("Option 5: Convert temperature from Fahrenheit to Celsius")
y= int(input("Enter 1, 2, 3, 4, or 5 to choose a menu option: "))
if (y == 1):
    print("what did the horse say after it tripped?")
    print("Help! I've fallen and I can't giddy-up!")
if (y== 2):
    print("What is your name? :")
    for i in range (15):
        print(name)
if (y == 3):
    x=int(input("Enter a number: "))
    print("Enter a number: ")
    for i in range (x):
        print("You don't have to know where the staircase is going to start climbing")
if (y== 4):
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
if (y == 5):
    def celsiusconversion(celsius):
        celsius= F-32 * 5/9
        return celsius
F = int(input("Enter today's temperature in Fahrenheit: "))
output=celsiusconversion(F)
print("Today's temperature in celsius is ", output, "degrees")
