import unittest
from tennis_game import Tennis


class tennisTestCase(unittest.TestCase):
    def test_FifteenAll(self):
        tennis = Tennis()
        tennis.first_player_score()
        tennis.second_player_score()
        actual = tennis.score()
        self.assertEqual(actual, 'Fifteen All')

    def test_ThirtyAll(self):
        tennis = Tennis()
        tennis.first_player_score()
        tennis.second_player_score()
        tennis.first_player_score()
        tennis.second_player_score()
        actual = tennis.score()
        self.assertEqual(actual, 'Thirty All')

    def test_Deuce(self):
        tennis = Tennis()
        tennis.first_player_score()
        tennis.second_player_score()
        tennis.first_player_score()
        tennis.second_player_score()
        tennis.first_player_score()
        tennis.second_player_score()
        actual = tennis.score()
        self.assertEqual(actual, 'Deuce')




if __name__ == '__main__':
    unittest.main()
