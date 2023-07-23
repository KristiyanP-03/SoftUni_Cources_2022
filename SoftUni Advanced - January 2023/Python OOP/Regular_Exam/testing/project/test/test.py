import unittest

from testing.project.tennis_player import TennisPlayer


class TestTenisPlayer(unittest.TestCase):

    def test_init(self):
        player = TennisPlayer("andi", 20, 100)
        self.assertEqual(player.name, "andi")
        self.assertEqual(player.age, 20)
        self.assertEqual(player.points, 100)

    def test_name(self):
        with self.assertRaises(ValueError) as error:
            player = TennisPlayer("a", 20, 100)
        self.assertEqual(str(error.exception), "Name should be more than 2 symbols!")

    def test_age(self):
        with self.assertRaises(ValueError) as error:
            player = TennisPlayer("gadar", 15, 100)
        self.assertEqual(str(error.exception), "Players must be at least 18 years of age!")

    def test_win(self):
        player = TennisPlayer("gadar", 20, 100)
        player.add_new_win("Varna Cup")
        self.assertEqual(player.wins, ["Varna Cup"])

    def test_repeating_win(self):
        player = TennisPlayer("gadar", 20, 100)
        result = player.add_new_win("Varna Cup")
        result = player.add_new_win("Varna Cup")
        self.assertEqual(result, f"Varna Cup has been already added to the list of wins!")

    def test_str(self):
        player = TennisPlayer("gadar", 20, 100)
        player.add_new_win("Varna Cup")
        result = player.__str__()
        self.assertEqual(result, f"Tennis Player: gadar\nAge: 20\nPoints: 100.0\nTournaments won: Varna Cup")

    def test_lt(self):
        player1 = TennisPlayer("John", 25, 100)
        player2 = TennisPlayer("Jane", 23, 150)
        result2 = player1.__lt__(player2)
        self.assertEqual(result2, "Jane is a top seeded player and he/she is better than John")

    def test_lt(self):
        player2 = TennisPlayer("John", 25, 100)
        player1 = TennisPlayer("Jane", 23, 150)
        result2 = player1.__lt__(player2)
        self.assertEqual(result2, "Jane is a better player than John")

    if __name__ == "__main__":
        unittest.main()