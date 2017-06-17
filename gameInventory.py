# This is the file where you must work. Write code in the functions, create new functions, 
# so they work according to the specification

# Displays the inventory.
def display_inventory(inventory):
    print("Inventory:")
    for key in inventory:
        print(inventory[key], key)
    print("Total number of items: %d" % sum(inventory.values()))


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    my_list = []
    for key in added_items: #key = elem neve
        if key in my_list:
            continue
        else:
            my_list.append(key)
            count = added_items.count(key) # count = egyes elemek darabszáma
            if key in inventory:
                inventory[key] += count
            else:
                inventory[key] = count
    return inventory


def length(x):
    n = 0
    maxlength = 0
    for element in x:
        length = len(element)
        if length > maxlength:
            maxlength=length
    return maxlength

def keywithmaxval(d):
    v=list(d.values())
    k=list(d.keys())
    return len(str(v[v.index(max(v))]))


# Takes your inventory and displays it in a well-organized table with 
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory) 
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None):
    print("Inventory:\n")
    x = longest + biggest + DECORATION_STRING_LENGTH
    print(" "*biggest+'count'+" "*longest+'item name')
    print('-' * x)
    if order=="count,desc":
        asc=False
    elif order=="count,asc":
        asc=True
    elif order=="":
        for key in inv:
            print(str(inventory[key]).rjust(biggest+5," "),end="")
            print(str(key).rjust(longest+9," "),end="\n")
        print("-" * x+"\nTotal number of items: %d" % sum(inv.values()))
        return
    for i in sorted(inventory, key=lambda n: (-inventory[n],n),reverse=asc):
        print(str(inv[i]).rjust(biggest+5," "),end="")
        print(str(i).rjust(longest+9," "),end="\n")
    print("-" * x+"\nTotal number of items: %d" % sum(inv.values()))


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's 
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    with open(filename,"r") as inputstream:
        for line in inputstream:
            currentline=line.split(",")
        inventory=add_to_inventory(inventory,currentline)
    return inventory


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text 
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    with open(filename,"r") as outputstream:
        for line in outputstream:
            currentline=line.split(",")
        inventory=add_to_inventory(inventory,currentline)
    return inventory
