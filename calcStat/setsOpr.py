from matplotlib_venn import venn2
from matplotlib_venn import venn3
from matplotlib import pyplot as plt


def sets():
    print('How many sets you want operate?\n')
    print('2')
    print('3')

    opc = input()

    while opc != "2" and opc != "3":
        print("I don't recognize your operation. Please type '2' or '3'.")
        opc = input()

    if opc == "2":
        print("Type the elements of your set, please enter real numbers.")
        print('Set A: ')
        setA = set(map(float, input().split(',')))
        print("Your fisrt set is: ", setA)
        print('Set B: ')
        setB = set(map(float, input().split(',')))
        print("Your second set is: ", setB, '\n')
        S = setA | setB

        # complement A'
        print('Complement A' ':', S - setA, '\n')

        # Union
        print("Union A U B :", setA | setB, '\n')

        # Intersection
        print("Intersection A n B:", setA & setB, '\n')

        print('='*45)
        print('Would you like to plot a Venn diagram?')
        print('Y/N')
        opt = input()

        while opt != "Y" and opt != "N":
            print("Please choose 'Y' (Yes) or 'N' (No).")
            opt = input()

        if opt == "Y":
            print('Your plot will be deployed in a few moments, press any key to continue.')
            input()
            venn2([setA, setB], ('A', 'B'))
            plt.show()

        elif opt == "N":
            print("Thanks, press any key to continue.")
            input()

    elif opc == "3":
        print("Type the elements of your set, please enter real numbers.")
        print('Set A: ')
        setA = set(map(float, input().split(',')))
        print(setA)
        print('Set B: ')
        setB = set(map(float, input().split(',')))
        print(setB)
        print('Set C: ')
        setC = set(map(float, input().split(',')))
        print(setC, '\n')
        S = setA | setB | setC

        # complement A'
        print('Complement A: ', S - setA, '\n')

        # Union
        print("Union A U B: ", setA | setB, '\n')

        # Union
        print("Union A U C: ", setA | setC, '\n')

        # Intersection
        print("Intersection A n B: ", setA & setB, '\n')

        # Intersection
        print("Intersection A n C: ", setA & setC, '\n')

        # S-(A & C)
        print("S-(A & C) :", S - (setA & setC), '\n')

        print('=' * 45)
        print('Would you like to plot a Venn diagram?')
        print("Yes/No")
        opt = input()


        if opt == "Yes":
            print('Your plot will be deployed in a few moments, press any key to continue.')
            input()
            venn3([setA, setB, setC], ('A', 'B', 'C'))
            plt.show()
        else:
            print("Thanks, press any key to continue.")
            input()

