import abc
import enum


class Holiday(enum.Enum):
    """
    enumerated class to define different holidays.
    """
    HALLOWEEN = 0,
    CHRISTMAS = 1,
    EASTER = 2


class Spider(enum.Enum):
    """
    This enum specifies the different distinct spider types.
    """
    TARANTULA = 0,
    WOLF_SPIDER = 1


class CandyFlavour(enum.Enum):
    """
    This enum specifies the different distinct Candy Flavour types.
    """
    SEA_SALT = 0,
    REGULAR = 1


class Colour(enum.Enum):
    """
    This enum specifies the different distinct colour types.
    """
    ORANGE = 0,
    BLUE = 1,
    PINK = 2,
    WHITE = 3,
    GREY = 4,
    RED = 5,
    GREEN = 6


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


class SantaSWorkshop(Toys):
    """
    Santa's Workshop is a Christmas-themed Toy
    """
    def __init__(self, dimensions_height, dimensions_width, number_of_rooms):
        super().__init__("Santa's Workshop", "Santa's Workshop Description", "7", False, 6)
        self.dimensions_height = dimensions_height
        self.dimensions_width = dimensions_width
        self.number_of_rooms = number_of_rooms


class RCSpider(Toys):
    """
    RC (Remote Controlled) Spider is a Halloween-themed Toy
    """
    def __init__(self, speed, jump_height, glow_in_the_dark):
        super().__init__("RC (Remote Controlled) Spider", "RC (Remote Controlled) Spider Description", "8", True, 12)
        self.speed = speed
        self.jump_height = jump_height
        self.glow_in_the_dark = glow_in_the_dark
        self.type_of_spider = (Spider.TARANTULA, Spider.WOLF_SPIDER)


class RobotBunny(Toys):
    """
    Robot Bunny is an Easter-themed Toy
    """
    def __init__(self, number_of_sound_effects):
        super().__init__("Robot Bunny", "Robot Bunny Description", "9", True, 3)
        self.number_of_sound_effects = number_of_sound_effects
        self.colour = (Colour.ORANGE, Colour.BLUE, Colour.PINK)


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


class DancingSkeleton(StuffedAnimals):
    """
    Dancing Skeleton is a Halloween-themed Stuffed Animal
    """
    def __init__(self, glow_in_the_dark):
        super().__init__("Dancing Skeleton", "Dancing Skeleton Description", "4", "Polyester Fibrefill", "S", "Acrylic")
        self.glow_in_the_dark = glow_in_the_dark


class Reindeer(StuffedAnimals):
    """
    Reindeer is a Christmas-themed Stuffed Animal
    """
    def __init__(self, has_glow_in_the_dark_nose):
        super().__init__("Reindeer", "Reindeer Description", "5", "Wool", "S", "Cotton")
        self.has_glow_in_the_dark_nose = has_glow_in_the_dark_nose


class EasterBunny(StuffedAnimals):
    """
    Easter Bunny is an Easter-themed Stuffed Animal
    """
    def __init__(self):
        super().__init__("Easter Bunny", "Easter Bunny Description", "6", "Polyester Fibrefill", "S", "Linen")
        self.colour = (Colour.WHITE, Colour.GREY, Colour.PINK, Colour.BLUE)


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


class PumpkinCaramelToffee(Candy):
    """
    CremeEggs is a Halloween-themed Candy
    """
    def __init__(self):
        super().__init__("Pumpkin Caramel Toffee", "Pumpkin Caramel Toffee Description", "1", True, False)
        self.candy_flavour = (CandyFlavour.REGULAR, CandyFlavour.SEA_SALT)


class CandyCanes(Candy):
    """
    CremeEggs is a Christmas-themed Candy
    """
    def __init__(self):
        super().__init__("Candy Canes", "Candy Canes Candy Description", "2", False, True)
        self.candy_stripes = (Colour.RED, Colour.GREEN)


class CremeEggs(Candy):
    """
    CremeEggs is an Easter-themed Candy
    """
    def __init__(self, pack_size):
        super().__init__("Creme Eggs", "Creme Eggs Candy", "3", True, False)
        self.pack_size = pack_size


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

    def createOrder(self):
        print(f"Creating a new order: \n")


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
        pass

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
