class Tennis():
    def __init__(self):
        self.firstPlayerScoreTimes = 0
        self.secondPlayerScoreTimes = 0
        self.list = ["Love", "Fifteen", "Thirty", "Forty"]

    def first_player_score(self):
        self.firstPlayerScoreTimes = self.firstPlayerScoreTimes + 1

    def second_player_score(self):
        self.secondPlayerScoreTimes = self.secondPlayerScoreTimes + 1

    def score_all(self):
        if self.firstPlayerScoreTimes < 3:
            return self.list[self.firstPlayerScoreTimes] + " All"
        else:
            return "Deuce"

    def score_love(self):
        return self.list[self.firstPlayerScoreTimes] + " Love"

    def love_score(self):
        return "Love " + self.list[self.secondPlayerScoreTimes]

    def score(self):
        if self.firstPlayerScoreTimes == self.secondPlayerScoreTimes:
            return self.score_all()

        if self.secondPlayerScoreTimes == 0:
            return self.score_love()

        if self.firstPlayerScoreTimes == 0:
            return self.love_score()

        if self.firstPlayerScoreTimes == 4 and self.secondPlayerScoreTimes == 3:
            return "Joey Adv"
        if self.firstPlayerScoreTimes == 3 and self.secondPlayerScoreTimes == 4:
            return "Tom Adv"
        if self.firstPlayerScoreTimes == 5 and self.secondPlayerScoreTimes == 3:
            return "Joey Win"
        if self.firstPlayerScoreTimes == 4 and self.secondPlayerScoreTimes == 4:
            return "Deuce"

