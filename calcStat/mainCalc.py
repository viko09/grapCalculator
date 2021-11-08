# ###################################
# ###########CALCULATOR##############
# ############by. Viko###############

from calcStat.importDatSet import data
from calcStat.setsOpr import sets

print('=' * 42)
print('       ¡Welcome to my project!\n'
      '             FCFM - BUAP\n'
      'Created by: Victor Manuel Luna Mendoza ;)')
print('=' * 42)

print('What would you like to do?\n')
print('1. Import a data set for its analysis')
print('2. Operations with sets')

opc = input()

while opc != "1" and opc != "2":
    print("I don't recognize your operation. Please type '1' or '2'.")
    print("Choose one of the options.")
    opc = input()

if opc == "1":
    data()
elif opc == "2":
    sets()
