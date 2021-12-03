from pathlib import Path
from enum import Enum

RESTAURANT_TXT = Path("restaurants.txt")
FOODS_TXT = Path("foods.txt")
OUTPUT_FILE = Path("info_about_restaurant.txt")


class Main:
    def __init__(self):
        self.restaurants = []
        self.get_restaurants()

    def get_restaurants(self):
        with open(RESTAURANT_TXT, encoding="UTF-8") as file:
            restaurants_strs = [line.strip().split("*") for line in file.readlines()]
            for restaurant_str in restaurants_strs:
                self.restaurants.append(
                    DeliveryRest(
                        restaurant_str[0],
                        restaurant_str[1],
                        restaurant_str[2],
                        restaurant_str[3],
                        restaurant_str[4]))

    def etterem_valasztas(self):
        for rest in self.restaurants:
            rest.get_info()

    def input_restaurants_by_type(self, type: str):
        maganhangzok = ["a", "e", "i", "o"]
        if type[0] in maganhangzok:
            print(f"Az {type} típúsú éttermek:\n")
            print("Kérem vállasszon a felsorolt éttermek közül egyet:\n")
        else:
            print(f"A {type} típúsú éttermek:\n")
            print("Kérem vállasszon a felsorolt éttermek közül egyet:\n")

        ettermek = set()
        for rest in self.restaurants:
            if rest.type == type:
                ettermek.add(rest.name)
                print("\t", rest.name)

        choosed_rest = input()

        if choosed_rest not in ettermek:
            print("A választása nem megfelelő.")
            return self.input_restaurants_by_type(type)
        else:
            return choosed_rest

    def input_rest_type(self):
        types = set()
        for rest in self.restaurants:
            types.add(rest.type)
        print("Válassz egy étterem típust!")
        for type in types:
            print("\t", type)
        print("Válasz helye: ")

        choosed_type = input()

        if choosed_type not in types:
            print("A választása nem megfelelő.")
            return self.input_rest_type()
        else:
            return choosed_type

    def get_info_by_inputs(self):
        choosed_rest_name = self.input_restaurants_by_type(self.input_rest_type())
        for rest in self.restaurants:
            if choosed_rest_name == rest.name:
                print(rest.get_info())
                print("Kiírtuk önnek egy dokumentumba, az étterem adatait. A fájl neve: info_about_restaurant.txt")
                rest.write_to_file_infos()

    def felhozatal_eldontes(self):
        print("Kérem döntse el milyen volt a felhozatal:")
        print("\t", felhozatal.f_t.value)
        print("\t", felhozatal.f_n.value)
        print("\t", felhozatal.f_s.value)
        get_input = input()
        print("Köszönjük a válaszát!")
        if felhozatal.f_t.value == get_input:
            return felhozatal.f_t
        elif felhozatal.f_n.value == get_input:
            return felhozatal.f_n
        elif felhozatal.f_s.value == get_input:
            return felhozatal.f_s
        else:
            return None

    def run(self):
        self.get_info_by_inputs()
        valasz = self.felhozatal_eldontes()
        # print(valasz.value)
        # Itt lehetne folyatni a programot, hogy mit kezdünk a felhasználó válaszával...


class Food:
    def __init__(self, name, price, extra):
        self.name = name
        self.price = int(price)
        self.extra = extra

    def __eq__(self, other):
        if self.name == other.name:
            return True


class Restaurant:
    def __init__(self, id, name, address, type):
        self.id = int(id)
        self.name = name
        self.address = address
        self.type = type
        self.foods = []
        self.get_foods()

    def get_foods(self):
        with open(FOODS_TXT, encoding="UTF-8") as file:
            foods_strs = [line.strip().split("*") for line in file.readlines()]
            for food_str in foods_strs:
                if int(food_str[0]) == self.id:
                    self.foods.append(Food(food_str[1], food_str[2], food_str[3]))

    def print_foods(self):
        output_string = "Kaják:\n"
        for food in self.foods:
            output_string += str("\n\t" + food.name + " " + str(food.price) + "Ft " + "  extra: " + food.extra)
        print("\n")

        return output_string

    def get_info(self):
        return self.print_foods() + "\n" + "\n" + "Étterem címe: " + self.address

    def write_to_file_infos(self):
        with open(OUTPUT_FILE, "w", encoding="UTF-8") as file:
            file.write(self.get_info())


class DeliveryRest(Restaurant):
    def __init__(self, id, name, address, type, delivery):
        super().__init__(id, name, address, type)
        self.delivery = delivery

    def have_delivery(self):
        if self.delivery == 1:
            return "Van házhozszállítás!\n"
        return "Nincs házhozszállítás!\n"

    def get_info(self):
        return self.have_delivery() + "\n" + self.print_foods() + "\n" + "\n" + "Étterem címe: " + self.address


class felhozatal(Enum):
    f_t = "Tetszett"
    f_n = "Nem tetszett"
    f_s = "Semleges"


if __name__ == '__main__':
    app = Main()
    app.run()
