import pandas as pd
import os

# Load the data
file_path = "/Users/chrisbarza/Desktop/Actual data.csv"  # Update to your actual file path
df = pd.read_csv(file_path)

# Function to calculate longest thinking time for white and black
def calculate_longest_thinking(df):
    # Identify the Clock_ply columns for white (even) and black (odd)
    white_columns = [col for col in df.columns if col.startswith('Clock_ply_') and int(col.split('_')[-1]) % 2 == 0]
    black_columns = [col for col in df.columns if col.startswith('Clock_ply_') and int(col.split('_')[-1]) % 2 == 1]

    # Initialize lists to store longest thinking times and corresponding Clock_ply
    longest_white = []
    longest_black = []
    white_clock_ply = []
    black_clock_ply = []

    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        # Calculate differences for white
        white_times = [pd.to_timedelta(row[col]) for col in white_columns if pd.notna(row[col])]
        white_differences = [abs((white_times[i + 1] - white_times[i]).total_seconds()) for i in range(len(white_times) - 1)]
        
        if white_differences:
            max_white_diff = max(white_differences)
            longest_white.append(max_white_diff)
            max_index = white_differences.index(max_white_diff)
            white_clock_ply.append(int(white_columns[max_index + 1].split('_')[-1]))  # +1 for the next ply
        else:
            longest_white.append(0)
            white_clock_ply.append(None)

        # Calculate differences for black
        black_times = [pd.to_timedelta(row[col]) for col in black_columns if pd.notna(row[col])]
        black_differences = [abs((black_times[i + 1] - black_times[i]).total_seconds()) for i in range(len(black_times) - 1)]
        
        if black_differences:
            max_black_diff = max(black_differences)
            longest_black.append(max_black_diff)
            max_index = black_differences.index(max_black_diff)
            black_clock_ply.append(int(black_columns[max_index + 1].split('_')[-1]))  # +1 for the next ply
        else:
            longest_black.append(0)
            black_clock_ply.append(None)

    # Add the longest thinking times and corresponding Clock_ply to the DataFrame
    df['Longest_White_Thinking'] = longest_white
    df['White_Clock_Ply'] = white_clock_ply
    df['Longest_Black_Thinking'] = longest_black
    df['Black_Clock_Ply'] = black_clock_ply

# Calculate longest thinking times
calculate_longest_thinking(df)

# Save the updated DataFrame to a new CSV file
output_file_path = "/Users/chrisbarza/Desktop/longest_moment.csv"  # Specify your output path
df.to_csv(output_file_path, index=False)

print("Processing complete. The longest thinking times and their respective Clock_ply have been saved to 'longest_moment.csv'.")




























