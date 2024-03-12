#-----------------------------------------------------------------------------
# Title: Mining RPG
# Name: Drew McGregor
# Class: CS30
# Assignment: RPG-Map
# Version: 0.1
#-----------------------------------------------------------------------------
'''
     Here is the headers docString 
     this is where you explain what the program does
'''
#-----------------------------------------------------------------------------
#-Imports and Global Variables------------------------------------------------
room_descriptions = {'shaft': 'description', 'weak_stone': 'write a decription', 'stone': 'write a decription', 'gas_pockets': 'description', 'abandoned_shaft': 'description', 'damp_cave': 'description', 'crystal_cave': 'description'}
#map = [[shaft, weak_stone, stone, stone], 
#        [shaft, stone, gas_pockets, abandoned_shaft], 
#        [shaft, damp_cave, flooded_cave, crytal_cave]]
player = {'xpos': 0, 'ypos': 0, 'movement_options': []}
#-Functions ------------------------------------------------------------------
def get_YesNo(msg):
    '''Asks user yes no question, outputs true for yes, false for no, checks formatting.
    msg = yes/no question'''
    answer = input(msg).lower()
    if answer == 'yes' or answer == 'y':
        return True
    elif answer == 'no' or answer == 'n':
        return False
    else:
        get_YesNo(msg)


def get_choice(valid_inputs, msg, error_msg):
    ''' asks user question until a valid input is given, presenting error
    msg on bad input
    valid_inputs = list of valid items
    msg = message given to user on run
    error_msg = msg on bad input
    '''
    choice = input(msg).lower()
    if choice == 'q':
        if get_YesNo('Are you sure you want to quit?'):
            main_menu()
        else:
            choice = get_choice(valid_inputs, msg, error_msg)
    if choice not in valid_inputs:
        print(error_msg)
        choice = get_choice(valid_inputs, msg, error_msg)
    return choice


def offer_options(original_options, msg, error_msg):
    """Assign and print numerical values to items in a list"""
    for item in original_options:
        print(f"{original_options.index(item)+1}. {item}")
    numbers = [str(number+1) for number in range(len(original_options))]
    full_options = original_options.copy()
    full_options.extend(numbers)
    choice = get_choice(full_options, 'Choose an option', 'try again')
    if choice == 'q':
        if get_YesNo('Are you sure you want to quit?'):
            main_menu()
    elif choice not in full_options:
        print(error_msg)
        choice = get_choice(full_options, msg, error_msg)
    elif choice.isnumeric():
        choice = full_options[int(choice)-1]
    return choice


def update_movement_options(xpos, ypos):
    global player
    if xpos == 0:
        player['movement_options'].extend(['up',   'down', 'right'])
    elif xpos == 1 or xpos == 2:
        player['movement_options'].extend(['left', 'right'])
    elif xpos == 3:
        player['movement_options'].append('left')
    try:
        if ypos == 0:
            player['movement_options'].remove('up')
        elif ypos == 2:
            player['movement_options'].remove('down')
    except:
        pass
        
    
#-Main -----------------------------------------------------------------------