class OutputHandler:
    def format_output(self, sorted_teams):
        """
        Format the sorted teams into the output format.
        :param sorted_teams: A list of tuples representing the team-points in order.
        :return: A string containing the formatted output.
        """
        output = ""
        current_rank = 1
        for team, points in sorted_teams:
            pt_or_pts = "pts" if points > 1 else "pt"
            output += f"{current_rank}. {team}, {points} {pt_or_pts}\n"
            current_rank += 1
        return output