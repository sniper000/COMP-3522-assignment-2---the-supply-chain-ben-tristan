import abc
import enum


class Holiday(enum.Enum):
    """
    enumerated class to define different holidays.
    """
    HALLOWEEN = 0,
    CHRISTMAS = 1,
    EASTER = 2


class Product(enum.Enum):
    TOY = 0,
    STUFFED_ANIMAL = 1,
    CANDY = 2


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


class CremeEggs(Candy):
    """
    CremeEggs is an Easter Candy
    """

    def __init__(self):
        super().__init__("Creme Eggs", "Creme Eggs Candy", "111", True, True)


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
        print("Printing inventory: ")
        [print(item) for item in self.toyInventory]
        [print(item) for item in self.stuffedAnimalInventory]
        [print(item) for item in self.candyInventory]


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
            while True:
                userInput = input(f"enter: \n"
                                  f"0 to process an order \n"
                                  f"1 to check current inventory \n"
                                  f"2 to exit \n"
                                  )

                if userInput == '0':
                    self.createOrder()
                if userInput == '1':
                    self.checkInventories()
                if userInput == '2':
                    print("thanks!")
                    exit(0)

        except ValueError:
            print("invalid input")

    # factoryMapping, orderNumber, productId, item, itemName, quantity, productDetails
    def createOrder(self):
        print(f"Creating a new order: \n")
        try:
            holiday = int(input(f"Enter: \n"
                                f"0 for Halloween \n"
                                f"1 for Christmas \n"
                                f"2 for Easter \n"))

            factory_holiday = None

            if holiday == '0':
                factory_holiday = Holiday.HALLOWEEN
            elif holiday == '1':
                factory_holiday = Holiday.CHRISTMAS
            elif holiday == '2':
                factory_holiday = Holiday.EASTER

            item = int(input(f'Enter: \n'
                             f'0 for Toy \n'
                             f'1 for Stuffed Animal \n'
                             f'2 for Candy \n'))

            factory_item = None
            if item == '0':
                factory_item = Product.TOY
            elif item == '1':
                factory_item = Product.STUFFED_ANIMAL
            elif item == '2':
                factory_item = Product.CANDY

            factoryMapping = (factory_holiday, factory_item)
            orderNum = int(input("Enter Order Number \n"))
            productID = input("Enter product Id \n")
            item = input("enter item \n")
            itemName = input("enter item name \n")
            quantity = int(input("enter quantity \n"))
            productDetails = {}
            order = Order(factoryMapping, orderNum, productID, item, itemName, quantity, productDetails)

            if item == '0':
                [self.inventory.addToy(item) for item in order.processOrder()]
            elif item == '1':
                [self.inventory.addStuffedAnimal(item) for item in order.processOrder()]
            elif item == '2':
                [self.inventory.addCandy(item) for item in order.processOrder()]

            self.appendOrder(order)

        except ValueError:
            print("invalid input")

            print("order complete!")
            print(order)

    def appendOrder(self, order):
        self.orders.append(order)

    def checkInventories(self):
        print("which inventory would you like to check?")
        try:
            inventoryInput = input(f"enter: \n"
                                   f"0 for Toy \n"
                                   f"1 for Stuffed Animal \n"
                                   f"2 for Candy")
            count = None

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
            elif 3 >= count > 0:
                print("very low stock")

        except ValueError:
            print("invalid input")

    def printDailyTransactions(self):
        pass


class Order:
    """
    Order class defines what product the user requires from the factory.
    """

    def __init__(self, factoryMapping, orderNumber, productId, item, itemName, quantity, productDetails):
        self.factoryMapping = factoryMapping
        self.orderNumber = orderNumber
        self.productId = productId
        self.item = item
        self.itemName = itemName
        self.quantity = quantity
        self.productDetails = productDetails

    def processOrder(self):
        return OrderProcessor(self, self.factoryMapping, self.productDetails).createOrder()

    def __str__(self):
        pass


class OrderProcessor:
    """
    OrderProcessor class that connects Orders to the factory.
    """

    def __init__(self, order, factoryMapping, productDetails):
        self.order = order
        self.factoryMapping = factoryMapping
        self.productDetails = productDetails

    def createOrder(self):
        return [CremeEggs, CremeEggs, CremeEggs]


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
