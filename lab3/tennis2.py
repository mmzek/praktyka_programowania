class TennisGame2:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.p1_score()
        else:
            self.p2_score()

    def score_points(self, player_points):
        if player_points == 0:
            return "Love"
        if player_points == 1:
            return "Fifteen"
        if player_points == 2:
            return "Thirty"
        if player_points == 3:
            return "Forty"

    def score(self):
        # result = ""
        # if self.p1points == self.p2points and self.p1points < 3:
        #     if self.p1points == 0:
        #         result = "Love"
        #     if self.p1points == 1:
        #         result = "Fifteen"
        #     if self.p1points == 2:
        #         result = "Thirty"
        #     result += "-All"
        # if self.p1points == self.p2points and self.p1points > 2:
        #     result = "Deuce"

        #removed redundant variables
        # p1res = ""
        # p2res = ""

        if self.p1points == self.p2points:
            if self.p1points < 3:
                return self.score_points(self.p1points) + "-All"
            return "Deuce"

        if self.p1points >= 4 or self.p2points >= 4:
            diff = self.p1points - self.p2points
            if diff == 1:
                return "Advantage player1"
            if diff == -1:
                return "Advantage player2"
            if diff >= 2:
                return "Win for player1"
            return "Win for player2"

        # p1res = ""
        # p2res = ""
        # if self.p1points > 0 and self.p2points == 0:
        #     if self.p1points == 1:
        #         p1res = "Fifteen"
        #     if self.p1points == 2:
        #         p1res = "Thirty"
        #     if self.p1points == 3:
        #         p1res = "Forty"
        #
        #     p2res = "Love"
        #     result = p1res + "-" + p2res
        # if self.p2points > 0 and self.p1points == 0:
        #     if self.p2points == 1:
        #         p2res = "Fifteen"
        #     if self.p2points == 2:
        #         p2res = "Thirty"
        #     if self.p2points == 3:
        #         p2res = "Forty"
        #
        #     p1res = "Love"
        #     result = p1res + "-" + p2res
        # if self.p1points > self.p2points and self.p1points < 4:
        #     if self.p1points == 2:
        #         p1res = "Thirty"
        #     if self.p1points == 3:
        #         p1res = "Forty"
        #     if self.p2points == 1:
        #         p2res = "Fifteen"
        #     if self.p2points == 2:
        #         p2res = "Thirty"
        #     result = p1res + "-" + p2res
        # if self.p2points > self.p1points and self.p2points < 4:
        #     if self.p2points == 2:
        #         p2res = "Thirty"
        #     if self.p2points == 3:
        #         p2res = "Forty"
        #     if self.p1points == 1:
        #         p1res = "Fifteen"
        #     if self.p1points == 2:
        #         p1res = "Thirty"
        #     result = p1res + "-" + p2res
        #
        # if self.p1points > self.p2points and self.p2points >= 3:
        #     result = "Advantage player1"
        #
        # if self.p2points > self.p1points and self.p1points >= 3:
        #     result = "Advantage player2"
        #
        # if (
        #     self.p1points >= 4
        #     and self.p2points >= 0
        #     and (self.p1points - self.p2points) >= 2
        # ):
        #     result = "Win for player1"
        # if (
        #     self.p2points >= 4
        #     and self.p1points >= 0
        #     and (self.p2points - self.p1points) >= 2
        # ):
        #     result = "Win for player2"
        # return result
        return self.score_points(self.p1points) + "-" +self.score_points(self.p2points)

    def p1_score(self):
        self.p1points += 1

    def p2_score(self):
        self.p2points += 1
