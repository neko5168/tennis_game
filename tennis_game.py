class Tennis():
    def __init__(self):
        self.firstPlayerScoreTimes = 0
        self.secondPlayerScoreTimes = 0

    def first_player_score(self):
        self.firstPlayerScoreTimes = self.firstPlayerScoreTimes + 1

    def second_player_score(self):
        self.secondPlayerScoreTimes = self.secondPlayerScoreTimes + 1

    def score_all(self):
        list = ["Love", "Fifteen", "Thirty"]
        if self.firstPlayerScoreTimes < 3:
            return list[self.firstPlayerScoreTimes] + " All"
        else:
            return "Deuce"

    def score(self):
        if self.firstPlayerScoreTimes == self.secondPlayerScoreTimes:
            return self.score_all()

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
        if self.firstPlayerScoreTimes == 4 and self.secondPlayerScoreTimes == 4:
            return "Deuce"

