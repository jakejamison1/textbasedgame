import sys
print("A zombie has escaped your lab. Gather items")
print('from each room to help locate and kill')
print('patient zero. You can exit the lab going North, South, East or West.')
print('Type North, South, East, or West to move.')
print('Type the item name in room to pick up item')
print('To exit the game type Exit')
print('')
print('')
# dict
rooms = {'Lab': {'East': 'Infirmary', 'North': 'Office', 'South': 'Kitchen', 'West': 'Armory',},
    'Armory': {'East': 'Lab',},
    'Kitchen': {'East': 'Closet', 'North': 'Lab',},
    'Closet': {'West': 'Kitchen',},
    'Infirmary': {'West': 'Lab', 'North': 'Storage room',},
    'Storage room': {'South': 'Infirmary',},
    'Office': {'East': 'Bathroom', 'South': 'Lab',},
    'Bathroom': {}}
items = {
    'Lab': '',
    'Armory': 'riotgear',
    'Kitchen': 'food',
    'Closet': 'flashlight',
    'Infirmary': 'syringe',
    'Storage room': 'firstaid',
    'Office': 'axe',
    'Bathroom': 'patient zero',

}
state = 'Lab'
inventory = []


# function
def get_new_state(state, direction):
    new_state = state  # declaring
    for i in rooms:  # loop
        if i == state:  # if
            if direction in rooms[i]:  # if
                new_state = rooms[i][direction]  # assigning new_state

    return new_state  # return


while 1:  # gameplay loop
    print('You are in the ', state)  # printing state
    if state == 'Bathroom':
        print('Hurry and capture patient zero', end='')
        for i in range(50):
            for j in range(1000000):
                pass
            print(".", end='', flush=True)
        print()
        if len(inventory) == 6:
            print('You subdued him and found a cure! congratulations')
        else:
            print('Sorry, you lost. The infection is spreading!')

#user input
    print('Available to you in this room is', items[state])
    print('You currently have', inventory)
    direction = input('Enter the item you want OR the Direction to go OR Exit to quit: ')
    if direction.lower() == items[state].lower():
        if items[state] not in inventory:
            inventory.append(items[state])
        continue
    direction = direction.capitalize()
    if direction == 'Exit':  # if
        sys.exit(0)  # exit function
    if direction == 'East' or direction == 'West' or direction == 'North' or direction == 'South':
        new_state = get_new_state(state, direction)  # calling function
        if new_state == state:
            print('We need to hurry before patient zero escapes the facility!')  # print
        else:
            state = new_state  # changing state value to new_state
    else:
        print('Cannot go that way!!')  # print
