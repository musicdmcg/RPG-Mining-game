#-----------------------------------------------------------------------------
# Module: Map
#-----------------------------------------------------------------------------
'''Map Variables and Functions'''
# Imports and Global Variables------------------------------------------------
from tabulate import tabulate
rooms = {'shaft': {'description': 'the mineshaft. '
    + 'The shaft is the only place you can move vertically',
'dangers': [], 'tools': 'basic pick', 'treasure': 0}, 
'weak_stone': {'description': 'an area of weak stone. '
        + 'You can mine through it with just a '
        + 'basic pickaxe. ',
'dangers': ['cave-in'], 'tools': 'basic pick', 'treasure': 0}, 
'stone': {'description': 'an area of hardened stone. '
    + 'You can only mine through it with an '
  + 'upgraded pickaxe',
'dangers': [], 'tools': 'upgraded pick', 'treasure': 1}, 
'gas_pockets': {'description': 'an area of weak stone. ' 
        + 'You can hear a hissing from somewhere '
        + 'close. You can mine through the stone '
        + 'with just a basic pickaxe. ',
'dangers': ['cave-in', 'suffocation'], 'tools': 'basic pick', 'treasure': 1},
'abandoned_shaft': {'description': 'an old abandoned '
            + 'mineshaft. It appears deserted. ',
'dangers': ['unstable_floor', 'cave-in'], 'tools': 'basic pick', 'treasure': 3}, 
'damp_cave': {'description': 'dimly lit cave. '
        + 'There are puddles in low spots, '
        + 'stalagtites and stalagmites extend from '
        + 'the ceiling and floor. ',
'dangers': ['slipping'], 'tools': 'basic pick', 'treasure': 1},
'crystal_cave': {'description': 'a large cave with waist '
            + ' high water. Crystals grow from the '
            + 'ceilings and floors. ',
'dangers': [], 'tools': 'basic pick', 'treasure': 3}, 
'flooded_cave': {'description': 'a flooded cave. '
            + 'You will need scuba gear to pass '
            + 'through it. ',
'dangers': ['drowning'], 'tools': 'scuba gear', 'treasure': 2}}
mine_map = [[{'shaft':False}, {'weak_stone':False}, {'stone':False}, {'stone':False}],
[{'shaft':False}, {'stone':False}, {'gas_pockets':False}, {'abandoned_shaft':False}], 
[{'shaft':False}, {'damp_cave':False}, {'flooded_cave':False}, {'crystal_cave':False}]]
#-Functions-------------------------------------------------------------------
def load_map():
    '''exports map as external file. final_msg = message print
    after function runs'''
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

print(mine_map[0][0])