class GameProcessor:
    def process_games(self, game_results):
        """
        Process the game results data into a dictionary with the teams and its points.
        :param game_results: A list of game results (team1, score1, team2, score2).
        :return: A dictionary mapping each team to its total points.
        """
        team_points = {}
        for team1, score1, team2, score2 in game_results:
            # Update points for team 1
            team_points[team1] = team_points.get(team1, 0) + self.calculate_points(score1, score2)
            # Update points for team 2
            team_points[team2] = team_points.get(team2, 0) + self.calculate_points(score2, score1)
        return team_points

    def calculate_points(self, own_score, opponent_score):
        """
        Calculate points based on scores.
        :param own_score: The score of the team.
        :param opponent_score: The score of the opponent team.
        :return: Own points.
        """
        if own_score > opponent_score:
            return 3  # Win
        elif own_score == opponent_score:
            return 1  # Draw
        else:
            return 0  # Loss
        
    def sorted_by_points(self, team_points):
        """
        Calculate rankings based on total points and alphabetically.
        :param team_points: A dictionary mapping each team to its total points.
        :return: A list order by rank.
        """
        sorted_by_points = sorted(team_points.items(), key=lambda x: (-x[1], x[0]))

        return sorted_by_points
