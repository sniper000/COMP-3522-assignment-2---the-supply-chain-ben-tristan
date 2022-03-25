import abc
import enum
import string

import pandas as pd
import openpyxl
from datetime import date

from numpy.core.defchararray import upper


class Holiday(enum.Enum):
    """
    enumerated class to define different holidays.
    """
    HALLOWEEN = "HALLOWEEN",
    CHRISTMAS = "CHRISTMAS",
    EASTER = "EASTER"


class CandyFlavour(enum.Enum):
    """
    This enum specifies the different distinct Candy Flavour types.
    """
    SEA_SALT = "sea salt",
    REGULAR = "regular"


class Colour(enum.Enum):
    """
    This enum specifies the different distinct colour types.
    """
    ORANGE = "orange",
    BLUE = "blue",
    PINK = "pink",
    WHITE = "white",
    GREY = "grey",
    RED = "red",
    GREEN = "green"


class Product(enum.Enum):
    TOY = "Toy",
    STUFFED_ANIMAL = "StuffedAnimal",
    CANDY = "Candy"


class Toys(abc.ABC):
    """
    Toys defines the interface for one of the products that the
    abstract factory is responsible to create
    """

    @abc.abstractmethod
    def __init__(self, name, description, product_id, has_batteries, min_age):
        self.name = name
        self.description = description
        self.product_id = product_id
        self.has_batteries = has_batteries
        self.min_age = min_age


class SantaSWorkshop(Toys):
    """
    Santa's Workshop is a Christmas-themed Toy
    """

    def __init__(self, name, description, product_id, has_batteries, min_age, dimensions, num_rooms):
        super().__init__(name, description, product_id, has_batteries, min_age)
        self.dimensions = dimensions
        self.num_rooms = num_rooms


class RCSpider(Toys):
    """
    RC (Remote Controlled) Spider is a Halloween-themed Toy
    """

    def __init__(self, name, description, product_id, has_batteries, min_age, speed, jump_height, has_glow,
                 spider_type):
        super().__init__(name, description, product_id, has_batteries, min_age)
        self.speed = speed
        self.jump_height = jump_height
        self.has_glow = has_glow
        self.spider_type = spider_type


class RobotBunny(Toys):
    """
    Robot Bunny is an Easter-themed Toy
    """

    def __init__(self, name, description, product_id, has_batteries, min_age, num_sound, colour
                 ):
        super().__init__(name, description, product_id, has_batteries, min_age)
        self.num_sound = num_sound
        self.colour = colour


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

    def __init__(self, name, description, product_id, stuffing, size, fabric, has_glow):
        super().__init__(name, description, product_id, stuffing, size, fabric)
        self.has_glow = has_glow


class Reindeer(StuffedAnimals):
    """
    Reindeer is a Christmas-themed Stuffed Animal
    """

    def __init__(self, name, description, product_id, stuffing, size, fabric, has_glow):
        super().__init__(name, description, product_id, stuffing, size, fabric)
        self.has_glow = has_glow


class EasterBunny(StuffedAnimals):
    """
    Easter Bunny is an Easter-themed Stuffed Animal
    """

    def __init__(self, name, description, product_id, stuffing, size, fabric, colour):
        super().__init__(name, description, product_id, stuffing, size, fabric)
        self.colour = colour


class Candy(abc.ABC):
    """
    Candy defines the interface for one of the products that the
    abstract factory pattern is responsible to create.
    """

    @abc.abstractmethod
    def __init__(self, name, description, product_id, has_nuts, has_lactose):
        self.name = name
        self.description = description
        self.product_id = product_id
        self.has_nuts = has_nuts
        self.has_lactose = has_lactose


class PumpkinCaramelToffee(Candy):
    """
    CremeEggs is a Halloween-themed Candy
    """

    def __init__(self, name, description, product_id, has_nuts, has_lactose, variety):
        super().__init__(name, description, product_id, has_nuts, has_lactose)
        self.variety = variety


class CandyCanes(Candy):
    """
    CremeEggs is a Christmas-themed Candy
    """

    def __init__(self, name, description, product_id, has_nuts, has_lactose, colour):
        super().__init__(name, description, product_id, has_nuts, has_lactose)
        self.colour = colour


class CremeEggs(Candy):
    """
    CremeEggs is an Easter-themed Candy
    """

    def __init__(self, name, description, product_id, has_nuts, has_lactose, pack_size):
        super().__init__(name, description, product_id, has_nuts, has_lactose)
        self.pack_size = pack_size


class HolidayFactory(abc.ABC):
    """
    The base factory class. All worlds expect this factory class to
    populate the world. The CharacterFactory class defines an interface
    to create the a Product family consisting of Toys, Stuffed Animals or Candy. These vary by Holiday.
    """

    @abc.abstractmethod
    def create_toys(self, **kwargs) -> Toys:
        pass

    @abc.abstractmethod
    def create_stuffed_animals(self, **kwargs) -> StuffedAnimals:
        pass

    @abc.abstractmethod
    def create_candy(self, **kwargs) -> Candy:
        pass


class HalloweenFactory(HolidayFactory):
    """
    This factory class implements the CharacterFactory Interface. It
    returns a product family consisting of RC Spider, Stuffed Animals, and
    Pumpkin Caramel Toffee.
    """

    def create_toys(self, **kwargs) -> Toys:
        """
        :return: returns a RC Spider
        """
        spider_type = ""
        for key, item in kwargs.items():
            if key == "name":
                name = item
            if key == "description":
                description = item
            if key == "product_id":
                product_id = item
            if key == "has_batteries":
                has_batteries = item
            if key == "min_age":
                min_age = item
            if key == "speed":
                speed = item
            if key == "jump_height":
                jump_height = item
            if key == "has_glow":
                has_glow = item
            if key == "spider_type":
                spider_type = item
        return RCSpider(name, description, product_id, has_batteries, min_age, speed, jump_height, has_glow,
                        spider_type)

    def create_stuffed_animals(self, **kwargs) -> StuffedAnimals:
        """
        :return: Returns a Dancing Skeleton
        """
        for key, item in kwargs.items():
            if key == "name":
                name = item
            if key == "description":
                description = item
            if key == "product_id":
                product_id = item
            if key == "stuffing":
                stuffing = item
            if key == "size":
                size = item
            if key == "fabric":
                fabric = item
            if key == "has_glow":
                has_glow = item
        return DancingSkeleton(name, description, product_id, stuffing, size, fabric, has_glow)

    def create_candy(self, **kwargs) -> Candy:
        """
        :return: Returns a Pumpkin Caramel Toffee
        """
        for key, item in kwargs.items():
            if key == "name":
                name = item
            if key == "description":
                description = item
            if key == "product_id":
                product_id = item
            if key == "has_nuts":
                has_nuts = item
            if key == "has_lactose":
                has_lactose = item
            if key == "variety":
                if item.lower() == CandyFlavour.REGULAR.name.lower() or item.lower() == CandyFlavour.SEA_SALT.name.lower():
                    variety = item
        return PumpkinCaramelToffee(name, description, product_id, has_nuts, has_lactose, variety)


class ChristmasFactory(HolidayFactory):
    """
    This factory class implements the HolidayFactory Interface. It
    returns a product family consisting of Santa's Workshop, Reindeer, and
    Candy Cane.
    """

    def create_toys(self, **kwargs) -> Toys:
        """
        :return: returns a Santa's Workshop
        """
        for key, item in kwargs.items():
            if key == "name":
                name = item
            if key == "description":
                description = item
            if key == "product_id":
                product_id = item
            if key == "has_batteries":
                has_batteries = item
            if key == "min_age":
                min_age = item
            if key == "dimension":
                dimension = item
            if key == "num_rooms":
                num_rooms = item
        return SantaSWorkshop(name, description, product_id, has_batteries, min_age, dimension, num_rooms)

    def create_stuffed_animals(self, **kwargs) -> StuffedAnimals:
        """
        :return: Returns a Reindeer
        """
        for key, item in kwargs.items():
            if key == "name":
                name = item
            if key == "description":
                description = item
            if key == "product_id":
                product_id = item
            if key == "stuffing":
                stuffing = item
            if key == "size":
                size = item
            if key == "fabric":
                fabric = item
            if key == "has_glow":
                has_glow = item
        return Reindeer(name, description, product_id, stuffing, size, fabric, has_glow)

    def create_candy(self, **kwargs) -> Candy:
        """
        :return: Returns a Candy Canes
        """
        for key, item in kwargs.items():
            if key == "name":
                name = item
            if key == "description":
                description = item
            if key == "product_id":
                product_id = item
            if key == "has_nuts":
                has_nuts = item
            if key == "has_lactose":
                has_lactose = item
            if key == "colour":
                if item.lower() == Colour.RED.name.lower() or item.lower() == Colour.GREEN.name.lower():
                    colour = item
        return CandyCanes(name, description, product_id, has_nuts, has_lactose, colour)


class EasterFactory(HolidayFactory):
    """
    This factory class implements the HolidayFactory Interface. It
    returns a product family consisting of Robot Bunny, Easter Bunny, and
    Creme Eggs.
    """

    def create_toys(self, **kwargs) -> Toys:
        """
        :return: returns a Robot Bunny
        """
        for key, item in kwargs.items():
            if key == "name":
                name = item
            if key == "description":
                description = item
            if key == "product_id":
                product_id = item
            if key == "has_batteries":
                has_batteries = item
            if key == "min_age":
                min_age = item
            if key == "num_sound":
                num_sound = item
            if key == "colour":
                colour = item
                if item.lower() == Colour.ORANGE.name.lower() or item.lower() == Colour.BLUE.name.lower() or \
                        item.lower() == Colour.PINK.name.lower():
                    colour = item
        return RobotBunny(name, description, product_id, has_batteries, min_age, num_sound,
                          colour)

    def create_stuffed_animals(self, **kwargs) -> StuffedAnimals:
        """
        :return: Returns an Easter Bunny
        """
        for key, item in kwargs.items():
            if key == "name":
                name = item
            if key == "description":
                description = item
            if key == "product_id":
                product_id = item
            if key == "stuffing":
                stuffing = item
            if key == "size":
                size = item
            if key == "fabric":
                fabric = item
            if key == "colour":
                if item.lower() == Colour.WHITE.name.lower() or item.lower() == Colour.GREY.name.lower() or \
                        item.lower() == Colour.PINK.name.lower() or item.lower() == Colour.BLUE.name.lower():
                    colour = item
        return EasterBunny(name, description, product_id, stuffing, size, fabric, colour)

    def create_candy(self, **kwargs) -> Candy:
        """
        :return: Returns a Creme Eggs
        """
        for key, item in kwargs.items():
            if key == "name":
                name = item
            if key == "description":
                description = item
            if key == "product_id":
                product_id = item
            if key == "has_nuts":
                has_nuts = item
            if key == "has_lactose":
                has_lactose = item
            if key == "pack_size":
                pack_size = item
        return CremeEggs(name, description, product_id, has_nuts, has_lactose, pack_size)


class HolidayMapper:
    """
    class that maps different enums to different factories.
    """
    holiday_mapper = {
        Holiday.HALLOWEEN: HalloweenFactory,
        Holiday.CHRISTMAS: ChristmasFactory,
        Holiday.EASTER: EasterFactory
    }

    def get_factory(self, holiday_type: Holiday) -> HolidayFactory:
        """
        Retrieves the associated factory for the specified HolidayEnum
        :param holiday_type: holidayEnum
        :return: a holidayFactory if found, None otherwise
        """
        factory_class = self.holiday_mapper.get(holiday_type)
        return factory_class()


class Inventory:
    """
    Inventory class that maintains inventory of gifts for storefront.
    """

    def __init__(self, toyInventory, stuffedAnimalInventory, candyInventory):
        """
        initializer for the inventory class.
        :param toyInventory: a list of Toys
        :param stuffedAnimalInventory: a list of StuffedAnimals
        :param candyInventory: a list of Candy
        """
        self.toyInventory = toyInventory
        self.stuffedAnimalInventory = stuffedAnimalInventory
        self.candyInventory = candyInventory

    def countItemsToys(self, name):
        """
        counts toys in toy inventory
        :param name: a String
        :return: an int
        """
        i = 0

        for toy in self.toyInventory:
            if toy.name == name:
                i += 1
        return i

    def countItemsAnimals(self, name):
        """
        counts animals in stuffed animals inventory
        :param name: a String
        :return: an int
        """
        i = 0

        for animal in self.stuffedAnimalInventory:
            if animal.name == name:
                i += 1
        return i

    def countItemsCandy(self, name):
        """
        counts candy in candy inventory
        :param name: a String
        :return: an int
        """
        i = 0

        for candy in self.candyInventory:
            if candy.name == name:
                i += 1
        return i

    def removeToy(self, item, quantity):
        """
        removes toys from toy inventory
        :param item: Toy
        :param quantity: an int
        :return: None
        """
        i = int(quantity)
        for toy in self.toyInventory:
            if i == 0:
                return
            if item.name == toy.name:
                i -= 1
                self.toyInventory.remove(toy)

    def removeStuffedAnimal(self, item, quantity):
        """
        removes stuffed animals from stuffed animals inventory
        :param item: StuffedAnimal
        :param quantity: an int
        :return: None
        """
        i = int(quantity)
        for stuffedAnimals in self.stuffedAnimalInventory:
            if i == 0:
                return
            if item.name == stuffedAnimals.name:
                i -= 1
                self.stuffedAnimalInventory.remove(stuffedAnimals)

    def removeCandy(self, item, quantity):
        """
        removes candy from candy inventory
        :param item: Candy
        :param quantity: an int
        :return: None
        """
        i = int(quantity)
        for candy in self.candyInventory:
            if i == 0:
                return
            if item.name == candy.name:
                i -= 1
                self.candyInventory.remove(candy)

    def addToys(self, item, quantity):
        """
        adds toys to toys inventory.
        :param item: Toys
        :param quantity: an int
        :return: None
        """
        for i in range(quantity):
            self.toyInventory.append(item)

    def addStuffedAnimals(self, item, quantity):
        """
        adds stuffed animals to stuffed animals inventory.
        :param item: StuffedAnimal
        :param quantity: an int
        :return: None
        """
        for i in range(quantity):
            self.stuffedAnimalInventory.append(item)

    def addCandy(self, item, quantity):
        """
        adds candy to candy inventory.
        :param item: Candy
        :param quantity: an int
        :return: None
        """
        for i in range(quantity):
            self.candyInventory.append(item)

    def checkInventory(self, product_id):
        """
        allows users to search for items in their inventory by inventory id.
        :param product_id: a String
        :return: None
        """
        count = 0
        for item in self.toyInventory:
            if item.product_id == product_id:
                count += 1
        for item in self.candyInventory:
            if item.product_id == product_id:
                count += 1
        for item in self.stuffedAnimalInventory:
            if item.product_id == product_id:
                count += 1
        print(f"your search returned {count} result")
        if count > 10:
            print("item is in stock")
        if 10 > count > 3:
            print("item is low in stock")
        if 3 > count > 0:
            print("item is very low in stock")
        if count == 0:
            print("item is out stock")

    def print(self):
        """
        Displays all objects in inventories -> for debug
        :return: None
        """
        print("Printing inventory: ")
        [print(item.name) for item in self.toyInventory]
        [print(item.name) for item in self.stuffedAnimalInventory]
        [print(item.name) for item in self.candyInventory]


class Storefront:
    """
    Entry point for the user. Maintains Orders and Inventories.
    """

    def __init__(self, orders, inventory):
        """
        initializer for Storefront.
        :param orders: list of Orders
        :param inventory: Inventory
        """
        self.orders = orders
        self.inventory = inventory

    def userMenu(self):
        """
        User menu -> application entry point.
        :return: None
        """
        print("welcome to the Web Store!")
        print("_________________________")
        try:
            while True:
                userInput = input(f"enter: \n"
                                  f"0 to process an order \n"
                                  f"1 to check current inventory \n"
                                  f"2 to exit \n")

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
        """
        processes online orders from specified orders file.
        :return: None
        """
        print(f"Creating a new order: \n")
        print("_________________________")
        op = OrderProcessor()
        new_list = op.processOrder()
        for item in new_list:
            holiday = upper(item.get_factoryMapping()[0])
            product = item.factoryMapping[1]
            productID = item.getProductID()
            quantity = item.getQuantity()
            name = item.getItemName()
            description = item.getDescription()
            product_details = item.getProductDetails()

            holiday_map = None
            if holiday == "HALLOWEEN":
                holiday_map = Holiday.HALLOWEEN
            if holiday == "CHRISTMAS":
                holiday_map = Holiday.CHRISTMAS
            if holiday == "EASTER":
                holiday_map = Holiday.EASTER

            holiday_factory = HolidayMapper().get_factory(holiday_map)

            if product == Product.CANDY.value:
                has_lactose = product_details.get("has_lactose")
                has_nuts = product_details.get("has_nuts")
                variety = product_details.get("variety")
                pack_size = product_details.get("pack_size")
                colour = product_details.get("colour")

                candy = holiday_factory.create_candy(name=name, description=description, product_id=productID,
                                                     has_nuts=has_nuts, has_lactose=has_lactose,
                                                     colour=colour, variety=variety, pack_size=pack_size)

                count = self.inventory.countItemsCandy(candy.name)

                if count > int(quantity):
                    print("processing order...")
                    self.inventory.removeCandy(candy, quantity)
                    print(f"successfully process: {item}")
                else:
                    self.inventory.addCandy(candy, 100)
                    print(f"insufficient stock for: {item} ... restocking item!")

            if product == "StuffedAnimal":
                colour = product_details.get("colour")
                stuffing = product_details.get("stuffing")
                size = product_details.get("size")
                fabric = product_details.get("fabric")

                stuffedAnimals = holiday_factory.create_stuffed_animals(name=name, description=description,
                                                                        product_id=productID, colour=colour,
                                                                        stuffing=stuffing, size=size, fabric=fabric,
                                                                        has_glow=has_glow)

                count = self.inventory.countItemsAnimals(stuffedAnimals.name)

                if count > int(quantity):
                    print("processing order...")
                    self.inventory.removeStuffedAnimal(stuffedAnimals, quantity)
                    print(f"successfully processed : {item}")
                else:
                    self.inventory.addStuffedAnimals(stuffedAnimals, 100)
                    print(f"insufficient stock for: {item} ... restocking item!")

            if product == "Toy":
                battery_operated = product_details.get("battery_operated")
                recommended_age = product_details.get("recommended_age")
                dimensions = product_details.get("dimensions")
                num_rooms = product_details.get("num_rooms")
                speed = product_details.get("speed")
                jump_height = product_details.get("jump_height")
                spider_type = product_details.get("spider_type")
                number_of_sound_effects = product_details.get("num_sound")
                colour=product_details.get("colour")
                has_glow=product_details.get("has_glow")

                toys = holiday_factory.create_toys(name=name, description=description, product_id=productID,
                                                   has_batteries=battery_operated, min_age=recommended_age,
                                                   dimension=dimensions, num_rooms=num_rooms, speed=speed,
                                                   jump_height=jump_height, spider_type=spider_type,
                                                   num_sound=number_of_sound_effects, colour=colour, has_glow=has_glow)
                count = self.inventory.countItemsToys(toys.name)

                if count > int(quantity):
                    print("processing order...")
                    self.inventory.removeToy(toys, quantity)
                    print(f"successfully processed: {item}")
                else:
                    self.inventory.addToys(toys, 100)
                    print(f"insufficient stock for: {item} ... restocking item!")
            print("writing...")
            self.appendOrder(item)

    def appendOrder(self, order):
        """
        appends order to the user order list
        :param order: an Order
        :return: None
        """
        self.orders.append(order)

    def checkInventories(self):
        """
        calls checkInventories in the inventory class.
        :return: None
        """
        user_input = input("enter product_id")
        self.inventory.checkInventory(user_input)

    def printDailyTransactions(self):
        """
        Writes all order transactions to a txt file on program exit.
        :return: None
        """
        date_time = date.today().strftime("%b-%d-%Y")
        with open('dailyTransactions.txt', 'w') as f:
            f.write("WEB STORE - Daily Transaction Report \n")
            f.write(f"{date_time} \n")
            for order in self.orders:
                f.write(order.__str__())


class Order:
    """
    Order class defines what product the user requires from the factory.
    """

    def __init__(self, factoryMapping, orderNumber, productId, itemName, quantity, description, productDetails):
        """
        initializer for the Order object.
        :param factoryMapping: a tuple -> to be mapped
        :param orderNumber: an int
        :param productId: a String
        :param itemName: a String
        :param quantity: an int
        :param description: a String
        :param productDetails: a Dictionary
        """
        self.factoryMapping = factoryMapping
        self.orderNumber = orderNumber
        self.productId = productId
        self.itemName = itemName
        self.quantity = quantity
        self.description = description
        self.productDetails = productDetails

    def __str__(self):
        """
        String representation for the Order object.
        :return: formatted String
        """
        return (f"Order {self.orderNumber}, Item {self.factoryMapping[1]}, Product Id {self.productId},"
                f"Name {self.itemName}, Quantity {self.quantity} \n")

    def get_factoryMapping(self):
        """
        holds item and holiday objects to be mapped in the future.
        :return: tuple
        """
        return self.factoryMapping

    def getOrderNumber(self):
        """
        getter for order number.
        :return: an int
        """
        return self.orderNumber

    def getProductID(self):
        """
        getter for product identification.
        :return: a String
        """
        return self.productId

    def getItemName(self):
        """
        getter for item name.
        :return: a String
        """
        return self.itemName

    def getQuantity(self):
        """
        getter for quantity.
        :return: an int
        """
        return self.quantity

    def getDescription(self):
        """
        getter for product description.
        :return: a string
        """
        return self.description

    def getProductDetails(self):
        """
        getter for product details.
        :return: dict of product details.
        """
        return self.productDetails


class OrderProcessor:
    """
    OrderProcessor class that connects Orders to the factory.
    """

    def __init__(self):
        pass

    def processOrder(self):
        """
        Function that accesses orders from user inputted file using pandas.
        :return: list of orders
        """
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
