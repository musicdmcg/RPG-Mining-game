#-----------------------------------------------------------------------------
# Title: Mining RPG
# Name: Drew McGregor
# Class: CS30
# Assignment: Modules: RPG - Inventory
# Version: 2.3
#-----------------------------------------------------------------------------
'''
         Player can move around a 2d map of a mineshaft and view map of it.
'''
#-----------------------------------------------------------------------------
#-Imports and Global Variables------------------------------------------------
from tabulate import tabulate
import user_inputs as u
import map as m
import player as p
#-Functions ------------------------------------------------------------------
def main_options():
    '''offers player possible options'''
    choice = u.offer_options(['move', 'mine', 'view_map'],
                           'What would you like to do? ',
                           "That's not a valid option, try again").lower()
    if choice == 'move':
        p.move()
    elif choice == 'mine':
        p.mine()
    elif choice == 'view_map':
        m.view_map()


def main_menu():
    '''Essentially a main() function'''
    print('MAIN MENU\n')
    m.load_map()
    stop  = input('press enter to start or "q" to quit.').lower()
    while stop != '' or stop != 'q':
        if stop == '':
            print('game starting')
            while True:
                print(p.player)
                main_options()
        elif stop == 'q':
            print('shutting down')
            break
        else:
            print('invalid input, please try again')
            stop  = input('press enter to start or "q" to quit.')
            continue


#-Main -----------------------------------------------------------------------
main_menu()