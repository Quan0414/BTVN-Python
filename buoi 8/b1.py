class Manufacturer:
    def __init__(self, indentity: int, location: str):
        self.__indentity = indentity
        self.__location = location

    def get_indentity(self):
        return self.__indentity
    
    def get_location(self):
        return self.__location
    
    def set_indentity(self, indentity):
        self.__indentity = indentity
    
    def set_location(self, location):
        self.__location = location

    def describe(self):
        print("Identity:", self.__indentity)
        print("Location:", self.__location)


class Device:
    def __init__(self, name: str, price: float, manufacturer: Manufacturer):
        self.__name = name
        self.__price = price
        self.__manufacturer = manufacturer

    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price
    
    def get_manufacturer(self):
        return self.__manufacturer
    
    def set_name(self, name):
        self.__name = name
    
    def set_price(self, price):
        self.__price = price

    def set_manufacturer(self, manufacturer: Manufacturer):
        self.__manufacturer = manufacturer

    def describe(self):
        print(f"Name: {self.__name}")
        print(f"Price: {self.__price}")
        self.__manufacturer.describe()