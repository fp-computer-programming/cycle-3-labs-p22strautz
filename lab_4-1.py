# Author: SCT (ADMG) 9/30/21

magic_charge = int(input("What is your magic charge?\n"))

shield_charge = int(input("What is your shield charge?\n"))

if magic_charge >= 90 and shield_charge >= 75:
    print("You defeated the dragon! But the princess is in another castle.")
else:
    print("The dragon burns you to a crisp.")
