class Tennis():
    def __init__(self):
        self.firstPlayerScoreTimes = 0
        self.secondPlayerScoreTimes = 0

    def first_player_score(self):
        self.firstPlayerScoreTimes = self.firstPlayerScoreTimes + 1

    def second_player_score(self):
        self.secondPlayerScoreTimes = self.secondPlayerScoreTimes + 1

    def score(self):
        if self.firstPlayerScoreTimes == 0 and self.secondPlayerScoreTimes == 0:
            return "Love All"
        if self.firstPlayerScoreTimes == 1 and self.secondPlayerScoreTimes == 1:
            return "Fifteen All"
        if self.firstPlayerScoreTimes == 2 and self.secondPlayerScoreTimes == 2:
            return "Thirty All"
        if self.firstPlayerScoreTimes == 3 and self.secondPlayerScoreTimes == 3:
            return "Deuce"

        if self.firstPlayerScoreTimes == 1 and self.secondPlayerScoreTimes == 0:
            return "Fifteen Love"
        if self.firstPlayerScoreTimes == 2 and self.secondPlayerScoreTimes == 0:
            return "Thirty Love"
        if self.firstPlayerScoreTimes == 3 and self.secondPlayerScoreTimes == 0:
            return "Forty Love"

        if self.firstPlayerScoreTimes == 0 and self.secondPlayerScoreTimes == 1:
            return "Love Fifteen"
        if self.firstPlayerScoreTimes == 0 and self.secondPlayerScoreTimes == 2:
            return "Love Thirty"

        if self.firstPlayerScoreTimes == 4 and self.secondPlayerScoreTimes == 3:
            return "Joey Adv"
        if self.firstPlayerScoreTimes == 3 and self.secondPlayerScoreTimes == 4:
            return "Tom Adv"
        if self.firstPlayerScoreTimes == 5 and self.secondPlayerScoreTimes == 3:
            return "Joey Win"

