# Building Scoring System

This project implements a scoring system for evaluating materials used in a building layout. The system reads a building layout from a text file, calculates scores for various materials, and writes the results to a new file. The program is based on the board game Blueprints

## Features

- **Get Building Layout**: Reads a building layout from a text file and processes it into a 2D list format.
- **Calculate Material Scores**: Computes scores for different materials (Glass, Recycled, Stone, Wood) based on specific rules.
- **Output Results**: Writes the formatted building layout and the calculated scores to a new file.

## Installation

1. Clone the repository:
    git clone https://github.com/yourusername/building-scoring-system.git
   
2. Navigate to the project directory:
    cd building-scoring-system
    
3. Ensure you have Python installed (version 3.6+ recommended).

## Usage

1. Place the building layout file (`building.txt`) in the `datafiles` directory.

2. Run the main script to calculate the scores:
    python main.py

3. The results will be saved in `scoring-results.txt` in the `datafiles` directory.

## File Structure

- `building.txt`: Input file containing the building layout.
- `scoring-results.txt`: Output file with the formatted building layout and the scores.
- `main.py`: Main script that runs the scoring system.
- `README.md`: Documentation for the project.

## Scoring Rules

- **Glass (`G`)**: The score is the number attached to the `G`.
- **Recycled (`R`)**: Scoring based on the total count of `R` found.
- **Stone (`S`)**: Scores vary depending on the row position in the reversed layout.
- **Wood (`W`)**: Scores 2 points for each non-empty adjacent cell.

## Example

Given a `building.txt` file with the following content:

--|S1|--

--|R1|--

--|S5|--

W6|R1|S6

The output in `scoring-results.txt` will include the formatted building layout and the calculated scores for Glass, Recycled, Stone, and Wood, along with the total score.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue for any bugs or feature requests.

## Author

- Name: Diego Gonzalez Reyes
- Email: dgonz348@mtroyal.ca
- Course: COMP 1631
- Instructor: Eric Chalmers

## License

This project is for educational purposes under the supervision of the instructor Eric Chalmers as part of COMP 1631 at Mount Royal University.

