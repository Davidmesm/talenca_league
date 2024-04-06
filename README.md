# League Ranking Application

This a application that calculates the ranking table for a league.

## Features

- Reads game results from a text file.
- Calculates points for each team based on wins, draws, and losses.
- Generates a ranking table ordered by points and team names.


## Installation

You can install the application by following these steps:

1. Clone this repository to your local machine

2. Navigate to the directory of the project:

    ```bash
    cd league-ranking

3. Install the application:

    ```bash
    pip install .
This will install the application along with its dependencies.


## Usage

1. Create a text file containing game results, with each line representing a game in the format: `<team1> <score1>, <team2> <score2>`. For example:

    ```
    Lions 3, Snakes 3
    Tarantulas 1, FC Awesome 0
    ```

2. Run the main script with the input file as an argument:

    ```
    league-ranking input.txt
    ```

3. The ranking table will be printed to the console.

## Running Tests

To run tests for this application:

1. Navigate to the root directory of the project.

2. Run the tests using the following command:

    ```bash
    python -m unittest discover tests
    ```

This will execute all tests within the `tests` directory and its subdirectories.