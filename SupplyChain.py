import abc
import enum


class Holiday(enum.Enum):
    """
    enumerated class to define different holidays.
    """
    HALLOWEEN = 0,
    CHRISTMAS = 1,
    EASTER = 2


class Toys(abc.ABC):
    """
    Toys defines the interface for one of the products that the
    abstract factory is responsible to create
    """

    @abc.abstractmethod
    def __init__(self, name, description, product_id, battery_operated, recommended_age):
        self.name = name
        self.description = description
        self.product_id = product_id
        self.battery_operated = battery_operated
        self.recommended_age = recommended_age


class StuffedAnimals(abc.ABC):
    """
    Stuffed Animals defines the interface for one of the products that the
    abstract factory pattern is responsible to create.
    """

    @abc.abstractmethod
    def __init__(self, name, description, product_id, stuffing, size, fabric):
        self.name = name
        self.description = description
        self.product_id = product_id
        self.stuffing = stuffing
        self.size = size
        self.fabric = fabric


class Candy(abc.ABC):
    """
    Candy defines the interface for one of the products that the
    abstract factory pattern is responsible to create.
    """

    def __init__(self, name, description, product_id, contain_nuts, lactose_free):
        self.name = name
        self.description = description
        self.product_id = product_id
        self.contain_nuts = contain_nuts
        self.lactose_free = lactose_free


class Inventory:
    """
    Inventory class that maintains inventory of gifts for storefront.
    """

    def __init__(self, toyInventory, stuffedAnimalInventory, candyInventory):
        self.toyInventory = toyInventory
        self.stuffedAnimalInventory = stuffedAnimalInventory
        self.candyInventory = candyInventory

    def addToy(self, item):
        self.toyInventory.append(item)

    def addStuffedAnimal(self, item):
        self.stuffedAnimalInventory.append(item)

    def addCandy(self, item):
        self.candyInventory.append(item)

    def toyCount(self):
        return int(len(self.toyInventory))

    def stuffedAnimalCount(self):
        return int(len(self.stuffedAnimalInventory))

    def candyCount(self):
        return int(len(self.candyInventory))

    def print(self):
        [print(item) for item in self.inventory]


class Storefront:
    """
    Entry point for the user. Maintains Orders and Inventories.
    """

    def __init__(self, orders, inventory):
        self.orders = orders
        self.inventory = inventory

    def userMenu(self):
        print("welcome to the Web Store!")
        try:
            userInput = input(f"enter: \n"
                              f"0 to process an order \n"
                              f"1 to check current inventory \n"
                              f"2 to exit \n"
                              )

            if userInput == '0':
                pass
            if userInput == '1':
                self.checkInventories()
            if userInput == '2':
                print("thanks!")
                exit(0)

        except ValueError:
            print("invalid input")

    def createOrder(self):
        pass

    def appendOrder(self, order):
        self.orders.append(order)

    def checkInventories(self):
        print("which inventory would you like to check?")
        try:
            inventoryInput = input(f"enter: \n"
                                   f"0 for Toy \n"
                                   f"1 for Stuffed Animal \n"
                                   f"2 for Candy")
            if inventoryInput == '0':
                count = self.inventory.toyCount()
            elif inventoryInput == '1':
                count = self.inventory.stuffedAnimalCount()
            elif inventoryInput == '2':
                count = self.inventory.candyCount()

            if count >= 10:
                print("in stock")
            elif count == 0:
                print("out of stock")
            elif 10 > count > 3:
                print("low stock")
            elif 3 > count > 0:
                print("very low stock")

        except ValueError:
            print("invalid input")

    def printDailyTransactions(self):
        pass


class Order:
    """
    Order class defines what product the user requires from the factory.
    """

    def __init__(self, factoryMapping, orderNumber, productId, item, itemName, productDetails):
        self.factoryMapping = factoryMapping
        self.orderNumber = orderNumber
        self.productId = productId
        self.item = item
        self.itemName = itemName
        self.productDetails = productDetails


class OrderProcessor:
    """
    OrderProcessor class that connects Orders to the factory.
    """

    def __init__(self):
        pass


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
