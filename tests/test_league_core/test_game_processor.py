import unittest
from src.league_core.game_processor import GameProcessor

class TestGameProcessor(unittest.TestCase):
    def setUp(self):
        self.game_processor = GameProcessor()

    def test_process_games(self):
        # Test processing game results
        game_results = [('TeamA', 3, 'TeamB', 2), ('TeamB', 1, 'TeamC', 1), ('TeamC', 0, 'TeamA', 0)]
        expected_team_points = {'TeamA': 4, 'TeamB': 4, 'TeamC': 1}
        self.assertEqual(self.game_processor.process_games(game_results), expected_team_points)

    def test_process_games(self):
        # Test processing game results
        game_results = [('TeamA', 3, 'TeamB', 2), ('TeamA', 1, 'TeamB', 1), ('TeamA', 0, 'TeamB', 1)]
        expected_team_points = {'TeamA': 4, 'TeamB': 4}
        self.assertEqual(self.game_processor.process_games(game_results), expected_team_points)

    def test_calculate_points(self):
        # Test calculating points for different score scenarios
        self.assertEqual(self.game_processor.calculate_points(3, 2), 3)  # Win
        self.assertEqual(self.game_processor.calculate_points(1, 1), 1)  # Draw
        self.assertEqual(self.game_processor.calculate_points(0, 1), 0)  # Loss

    def test_sorted_by_points(self):
        # Test sorting team points by points and alphabetically
        team_points = {'TeamA': 4, 'TeamB': 1, 'TeamC': 3, 'TeamE': 3, 'TeamD': 3}
        expected_sorted_by_points = [('TeamA', 4), ('TeamC', 3), ('TeamD', 3), ('TeamE', 3), ('TeamB', 1)]
        self.assertEqual(self.game_processor.sorted_by_points(team_points), expected_sorted_by_points)

if __name__ == '__main__':
    unittest.main()
