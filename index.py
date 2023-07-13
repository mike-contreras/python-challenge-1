from datetime import date
from functools import reduce
import uuid

inventory = []
inventoryKeys = ['index', 'id', 'name', 'price', 'quantity', 'type', 'added']

def add_item():
    item_id = str(uuid.uuid4())
    name = input('Enter item name: ')
    price = float(input('Enter item price: '))
    quantity = int(input('Enter item quantity: '))
    item_type = input('Enter item type: ')
    added = str(date.today())
    item = { 'id': item_id, 'name': name, 'price': price, 'quantity': quantity, 'type': item_type, 'added': added,  }
    print(item)
    is_correct = input('Is the item correct?: (Y/N)   ')
    if is_correct == 'Y':
        inventory.append(item)
        print(f'Item added: {item["name"]}')
    else:
        print('Item not added, exiting \n')

def update_item():
    print_inventory_table()
    if len(inventory) == 0:
        print('\n\n\nEmpty Inventory!\n\n\n')
    else:
        index_selected = int(input('Enter index of item to update'))
        item = inventory[index_selected]
        new_item = {}
        for property in item.keys():
            updated_value = input(f'Update {property} of item, current value: {item[property]}: ').replace(" ", "")
            if updated_value == '':
                print(f'{item[property]} not updated because value not provided\n')
                updated_value = item[property]
            new_item[property] = updated_value
        inventory[index_selected] = new_item
        print(f'Updated the following item: {item["name"]} found in index {index_selected}\n\n')

def search_item():
    property_name = select_search_prop()
    search_value = input(f'What to search for in {property_name}')
    item = search_by(property_name, search_value)
    if item:
        print(item)
    else:
        print(f'No item found in property {property_name} with value {search_value}')

def select_search_prop():
    search_option = int(input('Search by: 1. name, 2. type'))
    if search_option == 1:
        return 'name'
    elif search_option == 2:
        return 'type'

def search_by(property_name, value):
    return list(filter(lambda item: value in item[property_name], inventory))

def sort_items():
    property_name = select_sort_by()
    order = input('Select the order, asc or desc: ')
    sort_by(property_name,order)
    print(f'Inventory sorted by {property_name} in {order} order')


def sort_by(property, order):
    inventory.sort(key=lambda item: item[property], reverse= order == 'desc')

def select_sort_by():
    option = int(input('Search by: 1. name, 2. price, 3. quantity'))
    if option == 1:
        return 'name'
    elif option == 2:
        return 'price'
    elif option == 3:
        return 'quantity'

def generate_report():
    while True:
        print('--- Inventory Report --- \n')
        print('1. Get total count of inventory')
        print('2. Get total value of inventory')
        print('3. Return to main menu')
        selected = int(input('Enter selection: '))
        if selected == 1:
            get_total_count_inventory()
        elif selected == 2:
            get_total_value_inventory()
        elif selected == 3:
            print('Returning to main menu')
            break

def get_total_count_inventory():
    total = reduce(lambda acc, item: acc+item['quantity'], inventory, 0)
    print(f'Total count: {total}')

def get_total_value_inventory():
    total = reduce(lambda acc, item: acc+(item['quantity']*item['price']), inventory, 0)
    print(f'Total value: ${total}')


def print_inventory_table():
    if len(inventory) == 0:
        print('\n\n\nEmpty Inventory!\n\n\n')
    else:
        print(' + {:^10} | {:^40} | {:^30} | {:^10} | {:^10} | {:^10} | {:^10} '. format(*inventoryKeys))
        for index, row in enumerate(inventory):
            print(' - {:^10} | {:^40} | {:^30} | {:^10} | {:^10} | {:^10} | {:^10} '.format(index, *row.values()))

def inventory_menu():
    while True:
        print('\n\n--- Inventory Management System --- \n')
        print('1. Show inventory')
        print('2. Add item')
        print('3. Update item')
        print('4. Search item')
        print('5. Sort by: name, price, quantity')
        print('6. Generate report')
        print('7. Exit')
        selected = int(input('Enter selection: '))

        if selected == 1:
            print_inventory_table()
        if selected == 2:
            add_item()
        elif selected == 3:
            update_item()
        elif selected == 4:
            search_item()
        elif selected == 5:
            sort_items()
        elif selected == 6:
            generate_report()
        elif selected == 7:
            print('Terminating program')
            break

inventory_menu()
