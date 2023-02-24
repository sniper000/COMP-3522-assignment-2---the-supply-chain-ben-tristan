# COMP-3522-assignment-2---the-supply-chain-ben-tristan

This is a supply chain system that simulates a store that keeps festive seasonal items all year long. The system takes in bulk orders that come in from the store's website in the form of excel files. The system implements the Abstract Factory pattern to achieve this.

Features

User Menu - When the program runs, it provides a terminal menu that the store owner would have access to. The menu lets the cashier:

Process Web Orders: At the end of each day, the store owner downloads an excel file of all the online orders placed that day and processes them through the system.
Check Inventory: Allows the cashier to check what is currently in stock and provides a status indicator for items. Prints a list of all the items, their information, and the stock status indicator.
Exit: Exits the program and prints out the daily transaction report.
Inventory - The store maintains the following items:

Toys: For each festive season, the store stocks a unique toy. Despite that, there are some properties of each toy that all toys have in common. These are whether the toy is battery operated or not, the minimum recommended age of the child that the toy is safe for, a name, a description, and a product ID (a unique combination of letters and numbers).
Santa's Workshop: The premium Christmas present, this is not a battery-operated toy. The doll house comes in different varieties. They can vary in dimensions (width and height) and the number of rooms.
The RC Spider: The toy to get during Halloween. This toy is battery operated. The different varieties of spiders that are sold have the following properties: speed, jump height, some spiders glow in the dark, while others do not, and the type of spider - This can either be a Tarantula or a Wolf Spider and nothing else.
Robot Bunny: The toy for toddlers and infants out there. The toy is battery operated. These come in different varieties as well! Their properties are...
Error Handling - The system handles errors and unexpected player behavior (read: input) gracefully using the Easier to Ask for Forgiveness philosophy.

Output Formatting - The system formats the output to display the correct information in a pleasant, readable manner.
