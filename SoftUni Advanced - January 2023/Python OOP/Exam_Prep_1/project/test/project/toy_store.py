class ToyStore:
    def __init__(self):
        self.toy_shelf = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }

    def add_toy(self, shelf: str, toy_name: str):
        if shelf not in self.toy_shelf.keys():
            raise Exception("Shelf doesn't exist!")

        if self.toy_shelf[shelf] == toy_name:
            raise Exception("Toy is already in shelf!")

        if self.toy_shelf[shelf] is not None:
            raise Exception("Shelf is already taken!")

        self.toy_shelf[shelf] = toy_name
        return f"Toy:{toy_name} placed successfully!"

    def remove_toy(self, shelf: str, toy_name: str):
        if shelf not in self.toy_shelf.keys():
            raise Exception("Shelf doesn't exist!")

        if self.toy_shelf[shelf] != toy_name:
            raise Exception("Toy in that shelf doesn't exists!")

        self.toy_shelf[shelf] = None
        return f"Remove toy:{toy_name} successfully!"




import unittest


class Test_toy_shop(unittest.TestCase):
    def setUp(self) -> None:
        self.store = ToyStore()

    def test_init(self):
        self.assertEqual(self.store.toy_shelf, {"A": None, "B": None, "C": None, "D": None, "E": None, "F": None, "G": None})

    def test_add_toy(self):
        # Test adding a toy to an empty shelf
        self.assertEqual(self.store.add_toy("A", "Teddy Bear"), "Toy:Teddy Bear placed successfully!")
        self.assertEqual(self.store.toy_shelf, {"A": "Teddy Bear", "B": None, "C": None, "D": None, "E": None, "F": None, "G": None})

        # Test adding a toy to a non-empty shelf
        with self.assertRaises(Exception):
            self.store.add_toy("A", "Barbie Doll")

        # Test adding a toy to a non-existent shelf
        with self.assertRaises(Exception):
            self.store.add_toy("H", "Lego Set")

    def test_remove_toy(self):
        # Test removing a toy from an occupied shelf
        self.store.add_toy("B", "Remote Control Car")
        self.assertEqual(self.store.remove_toy("B", "Remote Control Car"), "Remove toy:Remote Control Car successfully!")
        self.assertEqual(self.store.toy_shelf, {"A": None, "B": None, "C": None, "D": None, "E": None, "F": None, "G": None})

        # Test removing a toy from an empty shelf
        with self.assertRaises(Exception):
            self.store.remove_toy("C", "Action Figure")

        # Test removing a non-existent toy from a shelf
        self.store.add_toy("D", "Jigsaw Puzzle")
        with self.assertRaises(Exception):
            self.store.remove_toy("D", "Board Game")

    if __name__ == "__main__":
        unittest.main()