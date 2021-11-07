from matplotlib_venn import venn2
from matplotlib_venn import venn3
from matplotlib import pyplot as plt


def sets():
    print('How many sets you want operate?\n')
    print('2')
    print('3')

    opc = input()

    if opc == "2":
        print("Type the elements of your set, please.")
        print('Set A: ')
        setA = set(map(float, input().split(',')))
        print("Your fisrt set is: ", setA)
        print('Set B: ')
        setB = set(map(float, input().split(',')))
        print("Your second set is: ", setB)
        S = setA | setB

        # complement A'
        print('Complement A' ':', S - setA)

        # Union
        print("Union A U B :", setA | setB)

        # Intersection
        print("Intersection A n B:", setA & setB)

        print('='*45)
        print('Would you like to plot a Venn diagram?')
        print('Yes/No')
        opt = input()

        if opt == "Yes":
            print('Your plot will be deployed in a few moments, press any key to continue.')
            input()
            venn2([setA, setB], ('A', 'B'))
            plt.show()
        else:
            print("Thanks, press any key to continue.")
            input()

    elif opc == "3":
        print("Type the elements of your set, please.")
        print('Set A: ')
        setA = set(map(float, input().split(',')))
        print(setA)
        print('Set B: ')
        setB = set(map(float, input().split(',')))
        print(setB)
        print('Set C: ')
        setC = set(map(float, input().split(',')))
        print(setC)
        S = setA | setB | setC

        # complement A'
        print('Complement A' ':', S - setA)

        # Union
        print("Union A U B :", setA | setB)

        # Union
        print("Union A U C:", setA | setC)

        # Intersection
        print("Intersection A n B:", setA & setB)

        # Intersection
        print("Intersection A n C:", setA & setC)

        # S-(A & C)
        print("S-(A & C) :", S - (setA & setC))

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
    else:
        print("I don't recognize your operation.")
