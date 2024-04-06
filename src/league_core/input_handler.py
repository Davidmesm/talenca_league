class InputHandler:
    def read_input_from_file(self, filename):
        """
        Read file and parse information to return a list of games.
        :param filename: file path.
        :return: A list of game results (team1, score1, team2, score2).
        """
        game_results = []
        try:
            with open(filename, 'r') as file:
                for line in file:
                    game_result = line.strip()
                    team_a_info, team_b_info = game_result.split(", ")

                    team_a_info = team_a_info.split(" ")
                    team_b_info = team_b_info.split(" ")

                    team_a, score_a = " ".join(team_a_info[:-1]), int(team_a_info[-1])
                    team_b, score_b = " ".join(team_b_info[:-1]), int(team_b_info[-1])
                    game_results.append((team_a, score_a, team_b, score_b))
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except Exception as e:
            print(f"Error reading file '{filename}': {e}")
        return game_results
