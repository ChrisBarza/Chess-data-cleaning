import os
import pandas as pd

# Define the file path
file_path = "/Users/chrisbarza/Desktop/Cleaned.csv"

# Check if the file exists
if not os.path.exists(file_path):
    print("The file was not found. Please verify the file path.")
else:
    # Load the dataset
    df = pd.read_csv(file_path)

    # Initialize lists to store the total mistakes per phase for each game
    total_mistakes_opening = []
    total_mistakes_middle = []
    total_mistakes_endgame = []

    # Loop over each row (each game)
    for index, row in df.iterrows():
        # Identify columns with evaluation scores (starting with 'Eval_ply_')
        eval_cols = [col for col in df.columns if col.startswith('Eval_ply_') and pd.notna(row[col])]
        
        # Parse the eval values as floats for easier calculation
        eval_values = [float(row[col]) for col in eval_cols]

        # Cap values to be within the range of -10 to 10
        eval_values = [max(-10, min(10, value)) for value in eval_values]

        # Initialize counters for mistakes in each phase
        white_mistakes_opening = 0
        black_mistakes_opening = 0
        white_mistakes_middle = 0
        black_mistakes_middle = 0
        white_mistakes_endgame = 0
        black_mistakes_endgame = 0

        # Check for mistakes in white and black moves in each phase
        for i in range(1, len(eval_values)):
            diff = abs(eval_values[i] - eval_values[i - 1])
            
            # Only consider mistakes where the difference is >= 2.5
            if diff >= 2.5:
                if i % 2 == 0:  # Current eval is even-indexed, so it's black's move
                    # Check phase based on move number
                    if i <= 20:
                        black_mistakes_opening += 1
                    elif i <= 40:
                        black_mistakes_middle += 1
                    else:
                        black_mistakes_endgame += 1
                else:  # Current eval is odd-indexed, so it's white's move
                    # Check phase based on move number
                    if i <= 20:
                        white_mistakes_opening += 1
                    elif i <= 40:
                        white_mistakes_middle += 1
                    else:
                        white_mistakes_endgame += 1

        # Append the mistakes to the respective phase lists
        total_mistakes_opening.append(white_mistakes_opening + black_mistakes_opening)
        total_mistakes_middle.append(white_mistakes_middle + black_mistakes_middle)
        total_mistakes_endgame.append(white_mistakes_endgame + black_mistakes_endgame)

    # Add the mistake counts to the dataframe
    df['total_mistakes_opening'] = total_mistakes_opening
    df['total_mistakes_middle'] = total_mistakes_middle
    df['total_mistakes_endgame'] = total_mistakes_endgame

    # Calculate the total mistakes across all games for each phase
    total_mistakes_opening_all = sum(total_mistakes_opening)
    total_mistakes_middle_all = sum(total_mistakes_middle)
    total_mistakes_endgame_all = sum(total_mistakes_endgame)

    # Print the total mistakes for each phase
    print(f"Total mistakes in Opening phase: {total_mistakes_opening_all}")
    print(f"Total mistakes in Middle Game phase: {total_mistakes_middle_all}")
    print(f"Total mistakes in End Game phase: {total_mistakes_endgame_all}")

    # Save the result to a new CSV file on the desktop
    output_path = "/Users/chrisbarza/Desktop/mistakes_per_phase.csv"
    df[['total_mistakes_opening', 'total_mistakes_middle', 'total_mistakes_endgame']].to_csv(output_path, index=False)

    print("The file 'mistakes_per_phase.csv' has been saved to your desktop.")


