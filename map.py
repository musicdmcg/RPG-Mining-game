#-----------------------------------------------------------------------------
# Module: Map
#-----------------------------------------------------------------------------
'''Map Variables and Functions'''
# Imports and Global Variables------------------------------------------------
from tabulate import tabulate
rooms = {'shaft': {'description': 'the mineshaft. '
    + 'The shaft is the only place you can move vertically',
'dangers': [], 'tools': 'basic pick', 'treasure': []},
'weak_stone': {'description': 'an area of weak stone. '
        + 'You can mine through it with just a '
        + 'basic pickaxe. ',
'dangers': ['cave-in'], 'tools': 'basic pick', 'treasure': []}, 
'stone': {'description': 'an area of hardened stone. '
    + 'You can only mine through it with an '
  + 'upgraded pickaxe',
'dangers': [], 'tools': 'upgraded pick', 'treasure': []}, 
'gas_pockets': {'description': 'an area of weak stone. ' 
        + 'You can hear a hissing from somewhere '
        + 'close. You can mine through the stone '
        + 'with just a basic pickaxe. ',
'dangers': ['cave-in', 'suffocation'], 'tools': 'basic pick', 'treasure': []},
'abandoned_shaft': {'description': 'an old abandoned '
            + 'mineshaft. It appears deserted. ',
'dangers': ['unstable_floor', 'cave-in'], 'tools': 'basic pick', 'treasure': []}, 
'damp_cave': {'description': 'dimly lit cave. '
        + 'There are puddles in low spots, '
        + 'stalagtites and stalagmites extend from '
        + 'the ceiling and floor. ',
'dangers': ['slipping'], 'tools': 'basic pick', 'treasure': []},
'crystal_cave': {'description': 'a large cave with waist '
            + ' high water. Crystals grow from the '
            + 'ceilings and floors. ',
'dangers': [], 'tools': 'basic pick', 'treasure': []}, 
'flooded_cave': {'description': 'a flooded cave. '
            + 'You will need scuba gear to pass '
            + 'through it. ',
'dangers': ['drowning'], 'tools': 'scuba gear', 'treasure': []}}
mine_map = [['shaft', 'weak_stone', 'stone', 'stone'],
['shaft', 'stone', 'gas_pockets', 'abandoned_shaft'], 
['shaft', 'damp_cave', 'flooded_cave', 'crystal_cave']]
#-Functions-------------------------------------------------------------------
def load_map():
    '''exports map as external file. final_msg = message print
    after function runs'''
    player_map = mine_map
    for layer in player_map:
        for room in layer:
            if 'cleared' not in room:
                layer.remove(room)
    try:
        with open('mining_map.txt', 'w') as m:
            m.write(tabulate(mine_map, tablefmt = 'outline'))
    except:
        print('The map failed to write. Please reload the game')
    else:
        print('map loaded')


def view_map():
    '''attempts to print map'''
    try:
        with open('mining_map.txt') as m:
            print(m.read())
    except:
        print('map failed to load')
    else:
        print('you open your map')
    finally:
        print('good luck')
