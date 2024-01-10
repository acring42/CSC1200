'''
Date : 2/10/2023

Name : Austin Ring

Class : CSC 1200

Lab : Lab 2

Problem: Jukebox Song Selector

Input : Int(Genre Choice) and Int(Song Choice)

Output : List of Songs from Selected Genre and the Song selected
'''

print("Welcome to the Jokebox!\nPlease enter one of the following options:")
print("\t1. Rock\n\t2. Rap\n\t3. Metal")
choice = input("Choice: ")

if choice == "1":
    print("\n\t1. Stairway to Heaven - Led Zeppelin\n\t2. Panama - Van Halen\n\t3. Free Bird - Lynyrd Skynyrd")
    song1 = input("Please choose a song: ")
    if song1 == "1":
        print("\nNow Playing: Stairway to Heaven - Led Zeppelin")
    elif song1 == "2":
        print("\nNow Playing: Panama - Van Halen")
    elif song1 == "3":
        print("\nNow Playing: Free Bird - Lynyrd Skynyrd")
    else:
        print("\n!!!Invalid Response!!!")
elif choice == "2":
    print("\n\t1. m.A.A.d city - Kendrick Lamar\n\t2. trademark usa - Baby Keem\n\t3. Raydar - JID")
    song2 = input("Please choose a song: ")
    if song2 == "1":
        print("\nNow Playing: m.A.A.d city - Kendrick Lamar")
    elif song2 == "2":
        print("\nNow Playing: trademark usa - Baby Keem")
    elif song2 == "3":
        print("\nNow Playing: Raydar - JID")
    else:
        print("\n!!!Invalid Response!!!")
elif choice == "3":
    print("\n\t1. Enter Sandman - Metallica\n\t2. Holy Wars...The Punishment Due - Megadeth\n\t3. Toxicity - System of a Down")
    song3 = input("Please choose a song: ")
    if song3 == "1":
        print("\nNow Playing: Enter Sandman - Metallica")
    elif song3 == "2":
        print("\nNow Playing: Holy Wars...The Punishment Due - Megadeth")
    elif song3 == "3":
        print("\nNow Playing: Toxicity - System of a Down")
    else:
        print("\n!!!Invalid Response!!!")
else:
    print("\n!!!Invalid Response!!!")