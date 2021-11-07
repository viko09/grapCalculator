import os
import pandas as pd


def data():
    print('Input your csv file, please.')
    readFile = input("Copy here the path: ")

    if os.path.isfile(readFile):
        existingFile = pd.read_csv(readFile)
        print(existingFile.head())
        print('\nIs this your dataset?')
        answer = input('Yes/No: ')

        if answer == "Yes":
            print('-/' * 30)
            print('What would you like to calculate?')
            print('1. Median')
            print('2. Mean')
            print('3. Mode')
            opc = input()

            if opc == "1":
                print("Choose a column?")
                nameOfcol = input()
                col = existingFile[nameOfcol]
                print("The median of {} is: ".format(nameOfcol), col.median())

            if opc == "2":
                print("Choose a column?")
                nameOfcol2 = input()
                col = existingFile[nameOfcol2]
                print("The mean of {} is: ".format(nameOfcol2), col.mean())

            if opc == "3":
                print("Choose a column?")
                nameOfcol = input()
                col = existingFile[nameOfcol]
                print("The mode of {} is: ".format(nameOfcol), col.mode())

        if answer == 'No':
            print('Try again...')
    else:
        print("The path you enter is not correct.")
