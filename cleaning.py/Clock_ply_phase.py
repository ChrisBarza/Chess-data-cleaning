import os
import pandas as pd
from datetime import datetime

# Function to convert time in hh:mm:ss format to seconds, handling invalid/NaN values
def time_to_seconds(time_str):
    if isinstance(time_str, str):
        try:
            time_obj = datetime.strptime(time_str, '%H:%M:%S')
            return time_obj.second + time_obj.minute * 60 + time_obj.hour * 3600
        except ValueError:
            return 0  # Return 0 if the value is not a valid time format
    else:
        return 0  # Return 0 if it's not a string or is NaN

# Define the file path
file_path = "/Users/chrisbarza/Desktop/200k_blitz_rapid_classical_bullet copy.csv"

# Check if the file exists
if not os.path.exists(file_path):
    print("The file was not found. Please verify the file path.")
else:
    # Load the dataset with low_memory=False to avoid dtype warnings
    df = pd.read_csv(file_path, low_memory=False)

    # Initialize lists to store the total time for each phase for each player
    total_white_opening_time = []
    total_black_opening_time = []
    total_white_middle_time = []
    total_black_middle_time = []
    total_white_endgame_time = []
    total_black_endgame_time = []

    # Loop over each row (each game)
    for index, row in df.iterrows():
        # Initialize total time counters for each player and phase
        white_opening_time = 0
        black_opening_time = 0
        white_middle_time = 0
        black_middle_time = 0
        white_endgame_time = 0
        black_endgame_time = 0
        
        # Handling the Opening Phase (1-20)
        if 'Clock_ply_1' in row and 'Clock_ply_19' in row:
            white_opening_time = abs(time_to_seconds(row['Clock_ply_19']) - time_to_seconds(row['Clock_ply_1']))

        if 'Clock_ply_2' in row and 'Clock_ply_20' in row:
            black_opening_time = abs(time_to_seconds(row['Clock_ply_20']) - time_to_seconds(row['Clock_ply_2']))

        # Handling the Middle Game Phase (21-40)
        if 'Clock_ply_21' in row and 'Clock_ply_39' in row:
            white_middle_time = abs(time_to_seconds(row['Clock_ply_39']) - time_to_seconds(row['Clock_ply_21']))

        if 'Clock_ply_22' in row and 'Clock_ply_40' in row:
            black_middle_time = abs(time_to_seconds(row['Clock_ply_40']) - time_to_seconds(row['Clock_ply_22']))

        # Handling the Endgame Phase (41 onward)
        if len(row) > 40:
            for ply_num in range(41, 201):  # From move 41 to 200
                clock_col = f"Clock_ply_{ply_num}"
                if clock_col in row and pd.notna(row[clock_col]):
                    time_spent = time_to_seconds(row[clock_col])
                    
                    # Assign to white or black based on odd/even move
                    if ply_num % 2 == 1:  # White's move (odd)
                        if white_endgame_time == 0:  # Start of the endgame phase
                            white_endgame_time += time_spent
                    else:  # Black's move (even)
                        if black_endgame_time == 0:  # Start of the endgame phase
                            black_endgame_time += time_spent

        # Append the total time spent in each phase to the lists
        total_white_opening_time.append(white_opening_time)
        total_black_opening_time.append(black_opening_time)
        total_white_middle_time.append(white_middle_time)
        total_black_middle_time.append(black_middle_time)
        total_white_endgame_time.append(white_endgame_time)
        total_black_endgame_time.append(black_endgame_time)

    # Add the total time columns to the dataframe
    df['total_white_opening_time'] = total_white_opening_time
    df['total_black_opening_time'] = total_black_opening_time
    df['total_white_middle_time'] = total_white_middle_time
    df['total_black_middle_time'] = total_black_middle_time
    df['total_white_endgame_time'] = total_white_endgame_time
    df['total_black_endgame_time'] = total_black_endgame_time

    # Save the result to a new CSV file on the desktop
    output_path = "/Users/chrisbarza/Desktop/total_thinking_time_per_phase.csv"
    df[['total_white_opening_time', 'total_black_opening_time', 
        'total_white_middle_time', 'total_black_middle_time', 
        'total_white_endgame_time', 'total_black_endgame_time']].to_csv(output_path, index=False)

    print("The file 'total_thinking_time_per_phase.csv' has been saved to your desktop.")




