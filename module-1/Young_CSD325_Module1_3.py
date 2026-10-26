# Name: Scott Young
# Course: CSD 325 - Advanced Python
# Assignment: Module 1.3 - On the Wall
# Date: October 25, 2026
# Description: A program that counts down the number
# of bottles of beer on the wall using a function


def countdown(number_of_bottles):
    """Count down the bottles of beer on the wall."""
    for number in range(number_of_bottles, 0, -1):
        if number == 1:
           print("1 bottle of beer on the wall,")
           print("1 bottle of beer.")
           print("Take one down, pass it around,")
           print("No more bottles of beer on the wall.")
        else:
            print(f"{number} bottles of beer on the wall,")
            print(f"{number} bottles of beer.")
            print("Take one down, pass it around,")
            if number - 1 == 1:
                print("1 bottle of beer on the wall.")
            else:
                print(f"{number -1} bottles of beer on the wall.")
        print()
bottles = int(input("How many bottles are on the wall? "))
countdown(bottles)
print("Time to buy more beer!")