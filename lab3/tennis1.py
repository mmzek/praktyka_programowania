class TennisGame1:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.p1points += 1
        else:
            self.p2points += 1

    # created function for equal score to make if statements look less nested
    def score_equal(self):
        result = {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All",
        }.get(self.p1points, "Deuce")
        return result

    #created another function
    def score_advantage_or_win(self):
        minus_result = self.p1points - self.p2points
        #if statements changed to shorter version
        if abs(minus_result) == 1:
            result = f"Advantage player{'1' if minus_result > 0 else '2'}"
        else:
            result = f"Win for player{'1' if minus_result > 0 else '2'}"
        return result


    def score(self):
        result = ""

        # deleted redundant variable
        #temp_score = 0
        if self.p1points == self.p2points:
            return self.score_equal()
        elif self.p1points >= 4 or self.p2points >= 4:
            return self.score_advantage_or_win()
        else:
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.p1points
                else:
                    result += "-"
                    temp_score = self.p2points
                result += {
                    0: "Love",
                    1: "Fifteen",
                    2: "Thirty",
                    3: "Forty",
                }[temp_score]
        return result
