# Author: Abrielle Nyei
# Date: 2026-04-09
# Title: Car Class Example (From Video/Image)

class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year


def main():
    # Create a Car object
    car1 = Car("Toyota", "Camry", 2022)

    # Display initial values
    print("Original Car Info:")
    print(car1.get_year(), car1.get_make(), car1.get_model())

    # Modify values using setters
    car1.set_make("Honda")
    car1.set_model("Civic")
    car1.set_year(2023)

    # Display updated values
    print("\nUpdated Car Info:")
    print(car1.get_year(), car1.get_make(), car1.get_model())


if __name__ == "__main__":
    main()