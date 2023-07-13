# Inventory System

Quick and simple CLI in-memory inventory management system written in Python.

To run the CLI tool: 
`python index.py`

## CLI Actions


### 1. Show inventory

Shows the current inventory


### 2. Add item

Enables the user to add an item. The user may define the name, price, quantity, and item_type. The id and added field are generated and added on creation 


### 3. Update item

Enables the user to update all of the properties of a selected item.
Selection of an item is done based on the index found on the farthest left of the shown table.

### 4. Search item

Searches for an item once the user gives a search criteria and the property to look in. (name, type)

### 5. Sort by: name, price, quantity

Sorts the existing inventory based on which property the user selects (name, price, quantity)


### 6. Generate report

Selecting this option opens a sub menu with the following types of calculations that can be made.

#### 1.1 Get total count of inventory

Calculates the total amount of items found in the inventory.

#### 1.2 Get total value of inventory

Calculates the total value based on each inventory item's quantity and price

#### 1.3 Exit

Selecting this action exits the user from the sub menu and returns them to the main menu.


### 7. Exit

Selecting this action terminates the program immediately

## Current item entity definition

* index: Property to use to select a given record
* id: Property generated on creation following uuidv4
* name: Name of the item. 
* price: Price of the item.
* quantity: Amount of a given item
* type: Type of the item
* added: Date property generated on creation to refer to its creation date.

