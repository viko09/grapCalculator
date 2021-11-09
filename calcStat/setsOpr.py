from matplotlib_venn import venn2
from matplotlib_venn import venn3
from matplotlib import pyplot as plt


def sets():
    print('How many sets you want operate?')
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
        print('Set B: ')
        setB = set(map(float, input().split(',')))

        print("Your first set is: ", setA)
        print("Your second set is: ", setB, '\n')
        print("Are those sets correct? Y/N")
        corornot = input()

        while corornot != "N" and corornot != "Y":
            print("Please choose 'Y' (Yes) or 'N' (No).")
            corornot = input()

        while corornot == "N":
            print("Which set do you want to change?")
            print("1 or 2")
            setCh = input()

            while setCh != "1" and setCh != "2":
                print("Please select 1 or 2.")
                setCh = input()

            if setCh == "1":
                print("Type the elements of your set, please enter real numbers.")
                print('Set A: ')
                setA = set(map(float, input().split(',')))
                print("Your first set is: ", setA)
                print("Your second set is: ", setB)
                print("Is it correct? Y/N")
                corornot = input()

                while corornot != "N" and corornot != "Y":
                    print("Please choose 'Y' (Yes) or 'N' (No).")
                    corornot = input()

                if corornot == "Y":
                    break

            elif setCh == "2":
                print("Type the elements of your set, please enter real numbers.")
                print('Set B: ')
                setB = set(map(float, input().split(',')))
                print("Your first set is: ", setA)
                print("Your second set is: ", setB, '\n')
                print("Is it correct? Y/N")
                corornot = input()

                while corornot != "N" and corornot != "Y":
                    print("Please choose 'Y' (Yes) or 'N' (No).")
                    corornot = input()

                if corornot == "Y":
                    break

        if corornot == "Y":

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
        print('Set B: ')
        setB = set(map(float, input().split(',')))
        print('Set C: ')
        setC = set(map(float, input().split(',')))

        print("Your first set is: ", setA)
        print("Your second set is: ", setB)
        print("Your third set is: ", setC, '\n')
        print("Are those sets correct? Y/N")

        corornot = input()

        while corornot != "N" and corornot != "Y":
            print("Please choose 'Y' (Yes) or 'N' (No).")
            corornot = input()

        while corornot == "N":
            print("Which set do you want to change?")
            print("1, 2 or 3")
            setCh = input()

            while setCh != "1" and setCh != "2" and setCh != "3":
                print("Please select '1', '2' or '3'.")
                setCh = input()

            if setCh == "1":
                print("Type the elements of your set, please enter real numbers.")
                print('Set A: ')
                setA = set(map(float, input().split(',')))
                print("Your first set is: ", setA)
                print("Your second set is: ", setB)
                print("Your third set is: ", setB)
                print("Is it correct? Y/N")
                corornot = input()

                while corornot != "N" and corornot != "Y":
                    print("Please choose 'Y' (Yes) or 'N' (No).")
                    corornot = input()

                if corornot == "Y":
                    break

            elif setCh == "2":
                print("Type the elements of your set, please enter real numbers.")
                print('Set B: ')
                setB = set(map(float, input().split(',')))
                print("Your first set is: ", setA)
                print("Your second set is: ", setB)
                print("Your third set is: ", setC, '\n')
                print("Is it correct? Y/N")
                corornot = input()

                while corornot != "N" and corornot != "Y":
                    print("Please choose 'Y' (Yes) or 'N' (No).")
                    corornot = input()

                if corornot == "Y":
                    break

            elif setCh == "3":
                print("Type the elements of your set, please enter real numbers.")
                print('Set C: ')
                setC = set(map(float, input().split(',')))
                print("Your first set is: ", setA)
                print("Your second set is: ", setB)
                print("Your third set is: ", setC, '\n')
                print("Is it correct? Y/N")
                corornot = input()

                while corornot != "N" and corornot != "Y":
                    print("Please choose 'Y' (Yes) or 'N' (No).")
                    corornot = input()

                if corornot == "Y":
                    break

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
        print("Y/N")
        opt = input()

        while opt != "Y" and opt != "N":
            print("Please choose 'Y' (Yes) or 'N' (No).")
            opt = input()

        if opt == "Y":
            print('Your plot will be deployed in a few moments, press any key to continue.')
            input()
            venn3([setA, setB, setC], ('A', 'B', 'C'))
            plt.show()

        elif opt == "N":
            print("Thanks, press any key to continue.")
            input()
