"""Task 1: Write a function that lets the user add items to a list.
Task 2: Include a feature to remove items from the list.
Task 3: Add a function that prints out the entire list in a formatted way."""


# Create Shopping List
shopping_list = []


# Task 1
def add_item(item, list):
    list.append(item)


# Task 2
def remove_item(item, list):
    if item in list:
        list.remove(item)
    else:
        print(f'{item} is not currently on shopping list')


# Task 3
def print_list(list):
    for i in range(len(list)):
        print(f' {i}. {list[i]}\n')


add_item('milk', shopping_list)
add_item('water', shopping_list)
add_item('apples', shopping_list)
add_item('cookies', shopping_list)

remove_item('cookies', shopping_list)
remove_item('bananas', shopping_list)

print_list(shopping_list)