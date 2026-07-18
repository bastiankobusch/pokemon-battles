import time
import numpy as np
import sys

#Delay printing
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05) #Printing speed

#Create pokemon class

class pokemon:
    def __init__(self, name, moves, evs, health='===================='):
        self. name = name
        self.moves = moves
        self.attack = evs ['ATTACK']
        self.defense = evs ['DEFENSE']
        self.bars = 20 #Amount of health


def fight(self, pokemon2):
    #Allows the two pokemon to fight each other

    #Print fight information
    print('-----POKEMON BATTLE-----')
    print(f'\n{self.name}')
    print('ATTACK/', self.attack)
    print('DEFENSE/', self.defense)
    print('LEVEL 5')
    print('\nVS')
    print(f'\n{pokemon2.name}')
    print('ATTACK/', pokemon2.attack)
    print('DEFENSE/', pokemon2.defense)
    print('LEVEL 5')

    time.sleep(2)

#Battle logic

#Continue as long as pokemon has health

    while (self.bars > 0) and (pokemon2.bars > 0):
        #Print pokemons current health
        print(f'{self.name}\t\tHLTH\t{self.health}')
        print(f'{pokemon2.name}\t\tHLTH\t{pokemon2.health}\n')

        print(f'Go {self.name}!')

        try: 
            move_choice = int(input('Pick a move (1-4): '))

            if move_choice == 1:
                


        