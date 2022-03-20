import enum


class Holiday(enum.Enum):
    """
    enumerated class to define different holidays.
    """
    HALLOWEEN = 0,
    CHRISTMAS = 1,
    EASTER = 2


class Inventory:
    """
    Inventory class that maintains inventory of gifts for storefront.
    """

    def __init__(self, inventory):
        self.inventory = None

    def getInventory(self):
        return self.inventory

    def add(self, item):
        self.inventory.append(item)

    def count(self):
        return self.inventory.length

    def print(self):
        [print(item) for item in self.inventory]


class Storefront:
    """
    Entry point for the user. Maintains Orders and Inventories.
    """

    def __init__(self):
        orders = []
        list = []
        inventory = Inventory(list)

    def userMenu(self):
        pass

    def createOrder(self):
        pass

    def appendOrder(self, order):
        self.orders.append(order)

    def checkInventories(self):
        if self.inventory.count >= 10:
            print("in stock")
        elif self.inventory.count == 0:
            print("out of stock")
        elif 10 > self.inventory.count > 3:
            print("low stock")
        elif 3 > self.inventory.count > 0:
            print("very low stock")

    def printDailyTransactions(self):
        pass


class Order:
    """
    Order class defines what product the user requires from the factory.
    """

    def __init__(self):
        pass


class OrderProcessor:
    """
    OrderProcessor class that connects Orders to the factory.
    """
    def __init__(self):
        pass

def main():
    Storefront()


if __name__ == '__main__':
    main()