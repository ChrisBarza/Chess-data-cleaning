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

    # Initialize lists to store the total inaccuracies per phase for each game
    total_inaccuracies_opening = []
    total_inaccuracies_middle = []
    total_inaccuracies_endgame = []

    # Loop over each row (each game)
    for index, row in df.iterrows():
        # Identify columns with evaluation scores (starting with 'Eval_ply_')
        eval_cols = [col for col in df.columns if col.startswith('Eval_ply_') and pd.notna(row[col])]
        
        # Parse the eval values as floats for easier calculation
        eval_values = [float(row[col]) for col in eval_cols]

        # Cap values to be within the range of -10 to 10
        eval_values = [max(-10, min(10, value)) for value in eval_values]

        # Initialize counters for inaccuracies in each phase
        white_inaccuracies_opening = 0
        black_inaccuracies_opening = 0
        white_inaccuracies_middle = 0
        black_inaccuracies_middle = 0
        white_inaccuracies_endgame = 0
        black_inaccuracies_endgame = 0

        # Check for inaccuracies in white and black moves in each phase
        for i in range(1, len(eval_values)):
            diff = abs(eval_values[i] - eval_values[i - 1])
            
            # Only consider inaccuracies where the difference is between 1.5 and 2.5
            if 1.5 <= diff < 2.5:
                if i % 2 == 0:  # Current eval is even-indexed, so it's black's move
                    # Check phase based on move number
                    if i <= 20:
                        black_inaccuracies_opening += 1
                    elif i <= 40:
                        black_inaccuracies_middle += 1
                    else:
                        black_inaccuracies_endgame += 1
                else:  # Current eval is odd-indexed, so it's white's move
                    # Check phase based on move number
                    if i <= 20:
                        white_inaccuracies_opening += 1
                    elif i <= 40:
                        white_inaccuracies_middle += 1
                    else:
                        white_inaccuracies_endgame += 1

        # Append the inaccuracies to the respective phase lists
        total_inaccuracies_opening.append(white_inaccuracies_opening + black_inaccuracies_opening)
        total_inaccuracies_middle.append(white_inaccuracies_middle + black_inaccuracies_middle)
        total_inaccuracies_endgame.append(white_inaccuracies_endgame + black_inaccuracies_endgame)

    # Add the inaccuracies counts to the dataframe
    df['total_inaccuracies_opening'] = total_inaccuracies_opening
    df['total_inaccuracies_middle'] = total_inaccuracies_middle
    df['total_inaccuracies_endgame'] = total_inaccuracies_endgame

    # Calculate the total inaccuracies across all games for each phase
    total_inaccuracies_opening_all = sum(total_inaccuracies_opening)
    total_inaccuracies_middle_all = sum(total_inaccuracies_middle)
    total_inaccuracies_endgame_all = sum(total_inaccuracies_endgame)

    # Print the total inaccuracies for each phase
    print(f"Total inaccuracies in Opening phase: {total_inaccuracies_opening_all}")
    print(f"Total inaccuracies in Middle Game phase: {total_inaccuracies_middle_all}")
    print(f"Total inaccuracies in End Game phase: {total_inaccuracies_endgame_all}")

    # Save the result to a new CSV file on the desktop
    output_path = "/Users/chrisbarza/Desktop/inaccuracies_per_phase.csv"
    df[['total_inaccuracies_opening', 'total_inaccuracies_middle', 'total_inaccuracies_endgame']].to_csv(output_path, index=False)

    print("The file 'inaccuracies_per_phase.csv' has been saved to your desktop.")
