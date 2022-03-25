# Name: Tristan Engen
# Student number: A01051088
# Name: Benjamin Lui
# Student number: A01242661
from SupplyChain import Inventory, Storefront


def main():
    inventory1 = []
    inventory2 = []
    inventory3 = []
    inventory = Inventory(inventory1, inventory2, inventory3)
    orders = []
    store = Storefront(orders, inventory)
    store.userMenu()


if __name__ == '__main__':
    main()