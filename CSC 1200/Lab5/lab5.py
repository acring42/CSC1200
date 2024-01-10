'''
Date : 3/4/2023

Name : Austin Ring

Class : CSC 1200

Lab : Lab 5

Problem: Reading from a file and counting the words
'''

def count(list1, dictionary):
    for item in list1:
        if item in dictionary:
            dictionary[item] = dictionary.get(item)+1
        else:
            dictionary[item] = 1
    return dictionary

def main():
    file1 = open("song.txt")
    dictionary = {}
    for line in file1:
        lyrics = line.lower()
        lyrics = lyrics.strip()
        lyrics = lyrics.split()
        dictionary = count(lyrics, dictionary)
    for items, values in dictionary.items():
        print(items, values)
    file1.close()

main()

