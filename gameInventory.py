# This is the file where you must work. Write code in the functions, create new functions,
# so they work according to the specification
import csv
DECORATION_STRING_LENGTH = 14
# Displays the inventory.
def display_inventory(inventory):
    print("Inventory:")
    for key in inventory:
        print(inventory[key], key)
    print("Total number of items: %d" % sum(inventory.values()))


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    my_list = []
    for key in added_items:  # key = elem neve
        if key in my_list:
            continue
        else:
            my_list.append(key)
            count = added_items.count(key)  # count = egyes elemek darabszáma
            if key in inventory:
                inventory[key] += count
            else:
                inventory[key] = count
    return inventory


# Takes the inventory and finds the longest element.
def k_length(inventory):
    n = 0
    maxlength = 0
    for element in inventory:
        length = len(element)
        if length > maxlength:
            maxlength = length
    return maxlength


# Takes the inventory and finds the longest value.
def v_length(inventory):
    return len(str(max(list(inventory.values()))))


# Takes your inventory and displays it in a well-organized table with
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory)
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=""):
    print("Inventory:\n")
    k_longest = k_length(inventory)
    v_longest = v_length(inventory)
    x = k_longest + v_longest + DECORATION_STRING_LENGTH
    print(" " * v_longest + 'count' + " " * k_longest + 'item name')
    print('-' * x)
    if order == "count,desc":
        desc = True
    elif order == "count,asc":
        desc = False
    elif order == "":
        for key in inventory:
            print(str(inventory[key]).rjust(v_longest + 5, " "), end="")
            print(str(key).rjust(k_longest + 9, " "), end="\n")
        print("-" * x + "\nTotal number of items: %d" % sum(inventory.values()))
        return
    else:
        print("Invalid order!\n" + "-" * x)
        return
    for i in sorted(inventory, key=lambda n: inventory[n], reverse=desc):
        print(str(inventory[i]).rjust(v_longest + 5, " "), end="")
        print(str(i).rjust(k_longest + 9, " "), end="\n")
    print("-" * x + "\nTotal number of items: %d" % sum(inventory.values()))


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    with open(filename, "r") as inputstream:
        for line in inputstream:
            currentline = line.split(",")
        inventory = add_to_inventory(inventory, currentline)
    return inventory


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    outputlist = []
    for key in inventory:
        value = 0
        while value < inventory[key]:
            outputlist.append(key)
            value += 1
    with open(filename, "w", newline="") as outputstream:
        writer = csv.writer(outputstream)
        writer.writerow(outputlist)
