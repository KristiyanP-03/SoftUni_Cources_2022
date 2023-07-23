from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    TYPES_DELICACY = {"Gingerbread": Gingerbread,"Stolen": Stolen}
    TYPES_BOOTH = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        list_with_repeating_delicacies = [d for d in self.delicacies if d.name == name]
        if list_with_repeating_delicacies:
            raise Exception(f"{name} already exists!")

        if type_delicacy not in ChristmasPastryShopApp.TYPES_DELICACY.keys():
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        current_delicacy = ChristmasPastryShopApp.TYPES_DELICACY[type_delicacy](name, price)
        self.delicacies.append(current_delicacy)

        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."


    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        list_with_repeating_booth_numbers = [num for num in self.booths if num.booth_number == num]
        if list_with_repeating_booth_numbers:
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in ChristmasPastryShopApp.TYPES_BOOTH.keys():
            raise Exception(f"{type_booth} is not a valid booth!")

        current_booth = ChristmasPastryShopApp.TYPES_BOOTH[type_booth](booth_number, capacity)
        self.booths.append(current_booth)

        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        not_reserved_booths = [booth for booth in self.booths \
                               if booth.is_reserved == False and number_of_people <= booth.capacity]

        if not_reserved_booths == False:
            raise Exception(f"No available booth for {number_of_people} people!")

        not_reserved_booths[0].reserve(number_of_people)

        return f"Booth {not_reserved_booths[0].booth_number} ordered {number_of_people}."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        all_booth_numbers = [num.booth_number for num in self.booths]
        if booth_number not in all_booth_numbers:
            raise Exception(f"Could not find booth {booth_number}!")

        all_delicacies_names = [deli.name for deli in self.delicacies]
        if delicacy_name not in all_delicacies_names:
            raise Exception(f"No {delicacy_name} in the pastry shop!")


        booth = [x for x in self.booths if x.booth_number == booth_number][0]
        delicacy = [x for x in self.delicacies if x.name == delicacy_name][0]
        booth.delicacy_orders.append(delicacy)

        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = [booth for booth in self.booths if booth.booth_number == booth_number][0]
        bill = booth.price_for_reservation + sum([delicacy.price for delicacy in booth.delicacy_orders])

        booth.delicacy_orders = []
        booth.is_reserved = False
        booth.price_for_reservation = 0

        self.income += bill

        return f"Booth {booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."



shop = ChristmasPastryShopApp()
print(shop.add_delicacy("Gingerbread", "Gingy", 5.20))
print(shop.delicacies[0].details())
print(shop.add_booth("Open Booth", 1, 30))
print(shop.add_booth("Private Booth", 10, 5))
print(shop.reserve_booth(30))
print(shop.order_delicacy(1, "Gingy"))
print(shop.leave_booth(1))
print(shop.reserve_booth(5))
print(shop.order_delicacy(1, "Gingy"))
print(shop.order_delicacy(1, "Gingy"))
print(shop.order_delicacy(1, "Gingy"))
print(shop.leave_booth(1))
print(shop.get_income())