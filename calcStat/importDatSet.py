import os
import pandas as pd


def data():
    print('\nInput your csv file, please.')
    readFile = input("Copy here the path: ")

    while os.path.isfile(readFile) == False:
        print("Please check the path and copy it again...")
        readFile = input("Copy here the path: ")

    if os.path.isfile(readFile):
        existingFile = pd.read_csv(readFile)
        print(existingFile.head())
        print('\nIs this your dataset?')
        answer = input('Yes/No: ')

        while answer != "Yes" and answer != "No":
            print("Please select 'Yes' or 'No'.")
            answer = input('Yes/No: ')

        while answer == "No":
            readFile = input("Copy here the path: ")

            while not os.path.isfile(readFile):
                print("Please check the path and copy it again...")
                readFile = input("Copy here the path: ")

            if os.path.isfile(readFile):
                existingFile = pd.read_csv(readFile)
                print(existingFile.head())
                print('\nIs this your dataset?')
                answer = input('Yes/No: ')

                while answer != "Yes" and answer != "No":
                    print("Please select 'Yes' or 'No'.")
                    answer = input('Yes/No: ')

        if answer == "Yes":
            print('-/' * 30)
            print('What would you like to calculate?')
            print('1. Median')
            print('2. Mean')
            print('3. Mode')
            opc = input()

            while opc != "1" and opc != "2" and opc != "3":
                print("Please select '1', '2' or '3'.")
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
