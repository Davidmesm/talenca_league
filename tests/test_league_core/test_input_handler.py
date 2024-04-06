import unittest
from src.league_core.input_handler import InputHandler

class TestInputHandler(unittest.TestCase):
    def setUp(self):
        self.input_handler = InputHandler()

    def test_read_input_from_file(self):
        # Create a temporary file with sample input data
        sample_input = "Lions 3, Snakes 3\nTarantulas 1, FC Awesome 0\n"
        with open("test_input.txt", "w") as file:
            file.write(sample_input)

        # Test file processed games
        expected_output = [('Lions', 3, 'Snakes', 3), ('Tarantulas', 1, 'FC Awesome', 0)]
        actual_output = self.input_handler.read_input_from_file("test_input.txt")
        self.assertEqual(actual_output, expected_output)

        #Remove the temporary file
        import os
        os.remove("test_input.txt")

    def test_read_input_from_file_non_existing_file(self):
        # Test empty result
        expected_output = []
        actual_output = self.input_handler.read_input_from_file("non_existing_file.txt")
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()
