import unittest
from tennis_game import Tennis


class tennisTestCase(unittest.TestCase):
    def test_LoveAll(self):
        tennis = Tennis()
        actual = tennis.score()
        self.assertEqual(actual, 'Love All')

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

    def test_Deuce2(self):
        tennis = Tennis()
        tennis.first_player_score()
        tennis.second_player_score()
        tennis.first_player_score()
        tennis.second_player_score()
        tennis.first_player_score()
        tennis.second_player_score()
        tennis.first_player_score()
        tennis.second_player_score()
        actual = tennis.score()
        self.assertEqual(actual, 'Deuce')



    def test_LoveFifteen(self):
        tennis = Tennis()
        tennis.second_player_score()
        actual = tennis.score()
        self.assertEqual(actual, 'Love Fifteen')

    def test_LoveThirty(self):
        tennis = Tennis()
        tennis.second_player_score()
        tennis.second_player_score()
        actual = tennis.score()
        self.assertEqual(actual, 'Love Thirty')

    def test_FifteenLove(self):
        tennis = Tennis()
        tennis.first_player_score()
        actual = tennis.score()
        self.assertEqual(actual, 'Fifteen Love')

    def test_ThirtyLove(self):
        tennis = Tennis()
        tennis.first_player_score()
        tennis.first_player_score()
        actual = tennis.score()
        self.assertEqual(actual, 'Thirty Love')

    def test_FortyLove(self):
        tennis = Tennis()
        tennis.first_player_score()
        tennis.first_player_score()
        tennis.first_player_score()
        actual = tennis.score()
        self.assertEqual(actual, 'Forty Love')

    def test_JoeyAdv(self):
        tennis = Tennis()
        tennis.first_player_score()
        tennis.first_player_score()
        tennis.first_player_score()
        tennis.first_player_score()
        tennis.second_player_score()
        tennis.second_player_score()
        tennis.second_player_score()
        actual = tennis.score()
        self.assertEqual(actual, 'Joey Adv')

    def test_TomAdv(self):
        tennis = Tennis()
        tennis.first_player_score()
        tennis.first_player_score()
        tennis.first_player_score()
        tennis.second_player_score()
        tennis.second_player_score()
        tennis.second_player_score()
        tennis.second_player_score()
        actual = tennis.score()
        self.assertEqual(actual, 'Tom Adv')

    def test_JoeyWin(self):
        tennis = Tennis()
        tennis.first_player_score()
        tennis.first_player_score()
        tennis.first_player_score()
        tennis.first_player_score()
        tennis.first_player_score()
        tennis.second_player_score()
        tennis.second_player_score()
        tennis.second_player_score()
        actual = tennis.score()
        self.assertEqual(actual, 'Joey Win')


if __name__ == '__main__':
    unittest.main()
