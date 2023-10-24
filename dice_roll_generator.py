import random

def dice_roll_generator():
    print("\n----------------------------------")
    while True:
        try:
            dices = int(input("<< Enter Number of dices(1 or 2): "))
            if dices in [1, 2]:
                break
            else:
                print("?> Enter 1 or 2 only")
        except ValueError:
            print("?> Invalid Value")
        
    for i in range(dices):
        if dices == 1:
            print(f">> Value of dice is: {random.randint(1, 6)}")
        else:
            print(f">> Value of dice {i+1} is: {random.randint(1, 6)}")
    
    print("----------------------------------\n")
    if (input("<> Press any key to exit or 'y' to continue: ")).lower() == "y":
        dice_roll_generator()
    else:
        exit()

if __name__ == "__main__":
    dice_roll_generator()