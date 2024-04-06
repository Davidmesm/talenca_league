import unittest
from src.league_core.output_handler import OutputHandler

class TestOutputHandler(unittest.TestCase):
    def setUp(self):
        self.output_handler = OutputHandler()

    def test_format_output(self):
        # Test output
        sorted_teams = [('TeamA', 4), ('TeamC', 3), ('TeamB', 1)]
        expected_output = "1. TeamA, 4 pts\n2. TeamC, 3 pts\n3. TeamB, 1 pt\n"
        self.assertEqual(self.output_handler.format_output(sorted_teams), expected_output)

if __name__ == '__main__':
    unittest.main()
