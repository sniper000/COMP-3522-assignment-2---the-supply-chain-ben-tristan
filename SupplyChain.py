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

    def __init__(self, orders, inventory):
        self.orders = orders
        self.inventory = inventory

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
