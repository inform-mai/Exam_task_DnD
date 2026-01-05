from ksandr_player import *
from garou import *
def tracker_initiative(persons):
    list_rolls = {}
    for person in persons:
        list_rolls[person] = person.roll_d20() + person.agility
    sorted_list_rolls = sorted(list_rolls.items(), key=lambda item: item[1], reverse=True)
    print('Порядок хода:')
    for i in range(len(sorted_list_rolls)):
        print(f'{i + 1}) {sorted_list_rolls[i][0].name}: {sorted_list_rolls[i][1]}', end='\n')
    return sorted_list_rolls

