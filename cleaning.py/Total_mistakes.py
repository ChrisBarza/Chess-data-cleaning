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

    # Initialize lists to store the counts of differences between 1 and 2 (inclusive) for each game
    total_diffs_white = []
    total_diffs_black = []

    # Loop over each row (each game)
    for index, row in df.iterrows():
        # Identify columns with evaluation scores (starting with 'Eval_ply_')
        eval_cols = [col for col in df.columns if col.startswith('Eval_ply_') and pd.notna(row[col])]
        
        # Parse the eval values as floats for easier calculation
        eval_values = [float(row[col]) for col in eval_cols]

        # Initialize counters for 1-2 differences
        white_diffs = 0
        black_diffs = 0

        # Check for differences in white and black moves between 1 and 2, inclusive
        for i in range(1, len(eval_values)):
            diff = abs(eval_values[i] - eval_values[i - 1])
            
            # Count differences (1 <= difference <= 2)
            if 1 <= diff <= 2:
                if i % 2 == 0:  # Black move (even-indexed)
                    black_diffs += 1  # Increment black_diffs by 1 for each occurrence
                else:  # White move (odd-indexed)
                    white_diffs += 1  # Increment white_diffs by 1 for each occurrence

        # Append the counts to the lists
        total_diffs_white.append(white_diffs)
        total_diffs_black.append(black_diffs)

    # Add the counts to the dataframe
    df['total_diffs_white'] = total_diffs_white
    df['total_diffs_black'] = total_diffs_black

    # Save the result to a new CSV file on the desktop
    output_path = "/Users/chrisbarza/Desktop/diffs_1_to_2_per_game.csv"
    df[['total_diffs_white', 'total_diffs_black']].to_csv(output_path, index=False)

    print("The file 'diffs_1_to_2_per_game.csv' has been saved to your desktop.")



