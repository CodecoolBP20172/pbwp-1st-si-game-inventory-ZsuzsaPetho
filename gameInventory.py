import csv

# This is the file where you must work. Write code in the functions, create new functions, 
# so they work according to the specification
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 
# Displays the inventory.
def display_inventory(inventory):
    print('Inventory: ')
    items = 0
    for pair in inv.items():
        items += pair[1]
        print("%s %s" % (pair[1], pair[0]) )
    print('Total number of items: %i' % items)

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    for list_item in added_items:
        #list_item = list_item.replace('  ', '')
        list_item = ' '.join(list_item.split())
        #list_item = list_item.strip()
        if list_item == '':
            continue
        if list_item in inventory:
            inventory[list_item] += 1
        else:
            inventory.update({list_item : 1})
    return inventory

# Takes your inventory and displays it in a well-organized table with 
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory) 
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def sort_inv(inventory,my_bool,len_count,len_item_name,items):
    for value in sorted(inventory, key=inventory.get, reverse=my_bool):
            print(str(inventory[value]).rjust(len_count) + value.rjust(len_item_name))
            items += inventory[value]
    return items
def max_len_search(inventory):
    len_count = 0
    len_item_name = 0
    for pair in inv.items():
        if len_count < len(str(pair[1])):
            len_count = len(str(pair[1]))
        if len_item_name < len(pair[0]):
            len_item_name = len(pair[0])
    return (len_count + 5), (len_item_name + 5)

def print_table(inventory, order=None):
    len_count, len_item_name = max_len_search(inventory)
    items = 0
    print('Inventory: ' + '\n' + 'count'.rjust(len_count) + 'item_name'.rjust(len_item_name)+ '\n' + '-'*(len_count+len_item_name))
    if order == "count,desc":
        items = sort_inv(inventory,True,len_count,len_item_name,items)
    elif order == "count,asc":
        items = sort_inv(inventory,False,len_count,len_item_name,items)
    else:
        for pair in inv.items():
            items += pair[1]
            print(str(pair[1]).rjust(len_count) + pair[0].rjust(len_item_name))
    print('-'*(len_count+len_item_name)+'\nTotal number of items: %i' % items)

# Imports new inventory items from a file
# The filename comes as an argument, but by default it's 
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).

def import_inventory(inventory, filename="import_inventory.csv"):
    try:
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            temp_list = list(reader)
            print(temp_list[0])
            inventory = add_to_inventory(inventory,temp_list[0])
    except:
        print ('There is problem with the file')
    return inventory

# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text 
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    with open(filename,'w') as out_file:
        #for value in inventory:
        #    print(('{},'.format(value))*(inventory[value]), end = '', file=out_file)
        out_list = []
        for value in inventory:
            for i in range(inventory[value]):
                out_list.append(value)
        for list_item in out_list[:-1]:
            print(('{}'.format(list_item)), end = ',', file=out_file)
        print(out_list[-1], end = '', file = out_file)
"""
display_inventory(inv)
inv = add_to_inventory(inv,dragon_loot)
print_table(inv)
print_table(inv, 'count,desc')
print_table(inv, 'count,asc')
inv = import_inventory(inv, 'test_inventory.csv')
print_table(inv, 'count,desc')
inv = import_inventory(inv, 'exam.csv')
#export_inventory(inv, 'output.csv')
print_table(inv, 'count,desc')
inv = import_inventory(inv, 'output.csv')
print_table(inv, 'count,desc')
"""
