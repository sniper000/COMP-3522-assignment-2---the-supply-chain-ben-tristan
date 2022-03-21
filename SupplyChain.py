import abc
import enum
import pandas as pd
import openpyxl


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


class HolidayFactory(abc.ABC):
    """
    The base factory class. All worlds expect this factory class to
    populate the world. The CharacterFactory class defines an interface
    to create the a Product family consisting of Friendlies, Enemies,
    and Animals. These vary by world.
    """

    @abc.abstractmethod
    def create_toys(self) -> Toys:
        pass

    @abc.abstractmethod
    def create_stuffed_animals(self) -> StuffedAnimals:
        pass

    @abc.abstractmethod
    def create_candy(self) -> Candy:
        pass


class HalloweenFactory(HolidayFactory):
    """
    This factory class implements the CharacterFactory Interface. It
    returns a product family consisting of RC Spider, Stuffed Animals, and
    Pumpkin Caramel Toffee.
    """

    def create_toys(self) -> Toys:
        """
        :return: returns a RC Spider
        """
        return RCSpider()

    def create_stuffed_animals(self) -> StuffedAnimals:
        """
        :return: Returns a Dancing Skeleton
        """
        return DancingSkeleton()

    def create_candy(self) -> Candy:
        """
        :return: Returns a Pumpkin Caramel Toffee
        """
        return PumpkinCaramelToffee()

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
        print("_________________________")
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
                    print("writing daily transactions...")
                    self.printDailyTransactions()
                    print("thanks!")
                    exit(0)

        except ValueError:
            print("invalid input")

    def createOrder(self):
        print(f"Creating a new order: \n")
        print("_________________________")
        op = OrderProcessor()
        new_list = op.processOrder()
        for item in new_list:
            self.appendOrder(item)
            # print(item)

    def appendOrder(self, order):
        self.orders.append(order)

    def checkInventories(self):
        self.inventory.print()
        if self.inventory.candyCount() > 10:
            print("Candy is in stock")
        if 10 > self.inventory.candyCount() > 3:
            print("Candy is low in stock")
        if 3 >= self.inventory.candyCount() > 0:
            print("Candy is very low in stock")
        if self.inventory.candyCount() == 0:
            print("Candy is out of stock")

        if self.inventory.toyCount() > 10:
            print("Toys are in stock")
        if 10 > self.inventory.toyCount() > 3:
            print("Toys are low in stock")
        if 3 >= self.inventory.toyCount() > 0:
            print("Toys are very low in stock")
        if self.inventory.toyCount() == 0:
            print("Toys are out of stock")

        if self.inventory.stuffedAnimalCount() > 10:
            print("Stuffed Animals are in stock")
        if 10 > self.inventory.stuffedAnimalCount() > 3:
            print("Stuffed Animals are low in stock")
        if 3 >= self.inventory.stuffedAnimalCount() > 0:
            print("Stuffed Animals are very low in stock")
        if self.inventory.stuffedAnimalCount() == 0:
            print("Stuffed Animals are out of stock")

    def printDailyTransactions(self):
        with open('dailyTransactions.txt', 'w') as f:
            for order in self.orders:
                f.write(order.__str__())


class Order:
    """
    Order class defines what product the user requires from the factory.
    """

    def __init__(self, factoryMapping, orderNumber, productId, itemName, quantity, description, productDetails):
        self.factoryMapping = factoryMapping
        self.orderNumber = orderNumber
        self.productId = productId
        self.itemName = itemName
        self.quantity = quantity
        self.description = description
        self.productDetails = productDetails

    def __str__(self):
        return (f"Order {self.orderNumber}, Item {self.factoryMapping[1]}, Product Id {self.productId},"
                f"Name {self.itemName}, Quantity {self.quantity} \n")


class OrderProcessor:
    """
    OrderProcessor class that connects Orders to the factory.
    """

    def __init__(self):
        pass

    def processOrder(self):
        filename = input("enter filename: \n")
        df_sheet_all = pd.read_excel(filename, sheet_name="Sheet1")
        order_list = []
        for i in range(0, len(df_sheet_all) - 1):
            order = df_sheet_all.loc[i]
            order_number = order['order_number']
            holiday = order['holiday']
            item = order['item']
            name = order['name']
            quantity = order['quantity']
            product_id = order['product_id']
            description = order['description']
            factoryMapping = (holiday, item)
            product_details = {
                'has_batteries': order['has_batteries'],
                'min_age': order['min_age'],
                'dimensions': order['dimensions'],
                'num_rooms': order['num_rooms'],
                'speed': order['speed'],
                'jump_height': order['jump_height'],
                'has_glow': order['has_glow'],
                'spider_type': order['spider_type'],
                'num_sound': order['num_sound'],
                'colour': order['colour'],
                'has_lactose': order['has_lactose'],
                'has_nuts': order['has_nuts'],
                'variety': order['variety'],
                'pack_size': order['pack_size'],
                'stuffing': order['stuffing'],
                'size': order['size'],
                'fabric': order['fabric']
            }
            order_list.append(Order(factoryMapping, order_number,
                                    product_id, name, quantity, description, product_details))

        print("Processing complete!")
        print("returning to main menu: ")
        return order_list


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
