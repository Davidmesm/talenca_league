import sys
from league_core.input_handler import InputHandler
from league_core.game_processor import GameProcessor
from league_core.output_handler import OutputHandler

def main():
    # Check if input file is being sent as an argument
    if len(sys.argv) != 2:
        print("Usage: league-ranking <input_file>")
        return

    # Extract the input file name
    input_file = sys.argv[1]

    # Initialize objects
    input_handler = InputHandler()
    game_processor = GameProcessor()
    output_handler = OutputHandler()

    # Read input data and retrieve games
    input_games = input_handler.read_input_from_file(input_file)

    # return if no games
    if input_games.count == 0:
        print("No game data")
        return

    # Process games
    team_points_map = game_processor.process_games(input_games)

    # Sort by points
    team_points_sorted = game_processor.sorted_by_points(team_points_map)

    # Format and print output
    output = output_handler.format_output(team_points_sorted)
    print(output)


if __name__ == "__main__":
    main()
