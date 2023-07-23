import unittest

from project.truck_driver import TruckDriver

class TestTruckDriver(unittest.TestCase):
    def setUp(self):
        self.driver = TruckDriver("Mat", 1)

    def test_driver_is_broke(self):
        with self.assertRaises(ValueError) as error:
            self.driver.earned_money = -1
        self.assertEqual(str(error.exception), f"{self.driver.name} went bankrupt.")


    def test_offer_already_exist(self):
        self.driver.available_cargos = {"Varna"}
        with self.assertRaises(Exception) as error:
            self.driver.add_cargo_offer("Varna", 1000)
        self.assertEqual(str(error.exception), "Cargo offer is already added.")

    def test_if_adds_to_avaible_cargos(self):
        self.driver.add_cargo_offer("Varna", 1000)
        self.assertEqual(self.driver.available_cargos["Varna"], 1000)

    def test_if_it_returns_correctly(self):
        result = self.driver.add_cargo_offer("Varna", 1000)
        self.assertEqual(result ,"Cargo for 1000 to Varna was added as an offer.")

    def test_driver_best_cargo_offer(self):
        self.driver.add_cargo_offer("A", 2)
        self.driver.add_cargo_offer("B", 1)
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual(result, "Mat is driving 2 to A.")

    def test_drive_best_cargo_offer_no_offers_available(self):
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual(result, "There are no offers available.")

    def test_eating(self):
        self.driver.earned_money = 100
        self.driver.eat(250)
        self.assertEqual(self.driver.earned_money, 80)

    def test_sleeping(self):
        self.driver.earned_money = 1000
        self.driver.sleep(1000)
        self.assertEqual(self.driver.earned_money, 955)

    def test_pump_gas(self):
        self.driver.earned_money = 1000
        self.driver.pump_gas(1500)
        self.assertEqual(self.driver.earned_money, 500)

    def test_repair_truck(self):
        self.driver.earned_money = 10000
        self.driver.repair_truck(10000)
        self.assertEqual(self.driver.earned_money, 2500)

    def test_repr(self):
        self.assertEqual(str(self.driver), "Mat has 0 miles behind his back.")


    if __name__ == "__main__":
        unittest.main()
