# Author: SCT (ADMG) 9/29/21

points = int(input("How many points did you score?\n"))
if points >= 15:
    print("You won gold!")
else:
    if points >= 12:
        print("You won silver!")
    else:
        if points < 9:
            print("You didnt win a metal.")
        else:
            print("You won bronze!")
