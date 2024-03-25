#-----------------------------------------------------------------------------
# Title: Mining RPG
# Name: Drew McGregor
# Class: CS30
# Assignment: RPG-Map
# Version: 1.0
#-----------------------------------------------------------------------------
'''
         Player can move around a 2d map of a mineshaft.
'''
#-----------------------------------------------------------------------------
#-Imports and Global Variables------------------------------------------------
from tabulate import tabulate
rooms = {'shaft': {'description': 'the mineshaft. '
                    + 'The shaft is the only place you can move vertically',
            'dangers': [], 'tools': [], 'cleared': True},
        'weak_stone': {'description': 'an area of weak stone. '
                        + 'You can mine through it with just a '
                        + 'basic pickaxe. ',
            'dangers': ['cave-in'], 'tools': [], 'cleared': False}, 
        'stone': {'description': 'an area of hardened stone. '
                    + 'You can only mine through it with an '
                  + 'upgraded pickaxe',
            'dangers': [], 'tools': ['upgraded pickaxe'], 'cleared': False}, 
        'gas_pockets': {'description': 'an area of weak stone. ' 
                        + 'You can hear a hissing from somewhere '
                        + 'close. You can mine through the stone '
                        + 'with just a basic pickaxe. ',
            'dangers': ['cave-in', 'suffocation'], 'tools': [],
            'cleared': False},
        'abandoned_shaft': {'description': 'an old abandoned '
                            + 'mineshaft. It appears deserted. ',
            'dangers': ['unstable_floor', 'cave-in'], 'tools': [],
            'cleared': False}, 
        'damp_cave': {'description': 'dimly lit cave. '
                        + 'There are puddles in low spots, '
                        + 'stalagtites and stalagmites extend from '
                        + 'the ceiling and floor. ',
            'dangers': ['slipping'], 'tools': [], 'cleared': False},
        'crystal_cave': {'description': 'a large cave with waist '
                            + ' high water. Crystals grow from the '
                            + 'ceilings and floors. ',
            'dangers': []}, 'tools': [], 'cleared': False, 
        'flooded_cave': {'description': 'a flooded cave. '
                            + 'You will need scuba gear to pass '
                            + 'through it. ',
            'dangers': ['drowning'], 'tools': ['scuba gear'],
            'cleared': False}}
mine_map = [['shaft', 'weak_stone', 'stone', 'stone'],
       ['shaft', 'stone', 'gas_pockets', 'abandoned_shaft'], 
       ['shaft', 'damp_cave', 'flooded_cave', 'crystal_cave']]
player = {'xpos': 0, 'ypos': 2, 'movement_options': [], 'inventory':[]}
#-Functions ------------------------------------------------------------------
def get_YesNo(msg, error_msg):
    '''Asks user yes no question, outputs true for yes, false for no.
    msg = yes/no question'''
    answer = input(msg).lower()
    if answer == 'yes' or answer == 'y':
        return True
    elif answer == 'no' or answer == 'n':
        return False
    else:
        print(error_msg)
        get_YesNo(msg, error_msg)


def get_choice(valid_inputs, msg, error_msg):
    ''' asks user question until a valid input is given, presenting error
    msg on bad input
    valid_inputs = list of valid items
    msg = message given to user on run
    error_msg = msg on bad input
    '''
    choice = input(msg).lower()
    if choice == 'q':
        if get_YesNo('Are you sure you want to quit?', 'The only valid otions are yes or no'):
            main_menu()
        else:
            choice = get_choice(valid_inputs, msg, error_msg)
    if choice not in valid_inputs:
        print(error_msg)
        choice = get_choice(valid_inputs, msg, error_msg)
    return choice


def offer_options(original_options, msg, error_msg):
    """Assign and print numerical values to items in a list"""
    print('\n\n')
    for item in original_options:
        print(f"{original_options.index(item)+1}. {item}")
    numbers = [str(number+1) for number in range(len(original_options))]
    full_options = original_options.copy()
    full_options.extend(numbers)
    choice = get_choice(full_options, msg, error_msg)
    if choice == 'q':
        if get_YesNo('Are you sure you want to quit?', 'The only valid options are yes or no'):
            main_menu()
    elif choice not in full_options:
        print(error_msg)
        choice = get_choice(full_options, msg, error_msg)
    elif choice.isnumeric():
        choice = full_options[int(choice)-1]
    return choice


def update_movement_options(xpos, ypos):
    '''Modifies player['movement_options'] assuming player is at xpos, ypos'''
    global player
    player['movement_options'].clear()
    if xpos == 0:
        player['movement_options'].extend(['up', 'down', 'right'])
    elif xpos == 1 or xpos == 2:
        player['movement_options'].extend(['left', 'right'])
    elif xpos == 3:
        player['movement_options'].append('left')
    try:
        if ypos == 2:
            player['movement_options'].remove('up')
        elif ypos == 0:
                 player['movement_options'].remove('down')
    except:
        pass


def move():
    '''Lets a user move the player around the map'''
    update_movement_options(player['xpos'], player['ypos'])
    choice = offer_options(player['movement_options'], 
                  'Where would you like to move? ', 
                  'invalid input, please try again')
    if choice == 'up':
        player['ypos'] += 1
    elif choice == 'down':
        player['ypos'] -= 1
    elif choice == 'right':
        player['xpos'] += 1
    elif choice == 'left':
        player['xpos'] -= 1


def view_map():
    with open('mining_map') as m:
        print(m.read())

def main_options():
    choice = offer_options(['move', 'mine', 'view_map'], 'What would you like to do? ', "That's not a valid option, try again").lower()
    if choice == 'move':
        move()
    elif choice == 'mine':
        mine() #doesn't exist yet
    elif choice == 'view_map':
        view_map() #doesn't exist yet

def main_menu():
    '''Essentially a main() function'''
    with open('mining_map', 'w') as m:
        m.write(tabulate(mine_map, tablefmt = 'outline'))
    print('MAIN MENU\n')
    view_map()
    stop  = input('press enter to start or "q" to quit.').lower()
    while stop != '' or stop != 'q':
        if stop == '':
            print('game starting')
            while True:
                print('You enter '
                    + f"""{rooms[mine_map[player['ypos']]
                        [player['xpos']]]['description']}""")
                print(player)
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