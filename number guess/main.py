import random
print("Welcome to Number Guess Game 👊")
while True:
    try:
        highest_Number = int(input("Enter the highest possible number: "))
        if highest_Number > 0:
            break;
        else:
            print("Please enter positive number! ")
    except ValueError:
        print("It's not a integer! Please enter a integer: ")

value = random.randint(1,highest_Number)
guess_cnt = 0

while True:
    while True:
        try:
            guessed_Number = int(input("What's your guess? "))
            break;
        except ValueError:
            print("It's not a integer! Please enter a integer")

    guess_cnt += 1
    if guessed_Number == value:
        print(f"\nyou got it. ✅")
        print(f"you guessed it in {guess_cnt} times 👍")
        break;
    elif guessed_Number > value:
        print("😭 too high! guess small number ")
    else:
        print("😭 too low! guess high number ")
    