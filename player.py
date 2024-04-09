#-----------------------------------------------------------------------------
# Module: Player
#-----------------------------------------------------------------------------
'''Player Variables and Functions'''
# Imports and Global Variables------------------------------------------------
import user_inputs as u
import map as m
player = {'xpos': 0, 'ypos': 0, 'movement_options': [], 'inventory':['basic pick']}
#-Functions-------------------------------------------------------------------
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
        if ypos == 0:
            player['movement_options'].remove('up')
        elif ypos == 2:
                 player['movement_options'].remove('down')
    except:
        pass

def mine():
    '''put description here'''
    if 'cleared' in m.mine_map[player['ypos']][player['xpos']]:
        print("There's nothing left to mine in this room")
        print(m.mine_map)
    else:
        if m.rooms[m.mine_map[player['ypos']][player['xpos']]]['tools'] in player['inventory']:
            player['inventory'].extend(m.rooms[m.mine_map[player['ypos']][player['xpos']]]['treasure'])
            m.mine_map[player['ypos']][player['xpos']] += ' (cleared)'
            m.load_map()
        else:
            print(f'''You need {m.rooms[m.mine_map[player['ypos']]
            [player['xpos']]]['tools']} to clear this room. ''')


def move():
    '''Lets a user move the player around the map'''
    update_movement_options(player['xpos'], player['ypos'])
    choice = u.offer_options(player['movement_options'], 
                  'Where would you like to move? ', 
                  'invalid input, please try again')
    if choice == 'up':
        player['ypos'] -= 1
    elif choice == 'down':
        player['ypos'] += 1
    elif choice == 'right':
        player['xpos'] += 1
    elif choice == 'left':
        player['xpos'] -= 1
    print(f"""You enter {m.rooms[m.mine_map[player['ypos']]
                        [player['xpos']]]['description']}""")