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

    # Initialize lists to store the total thinking times per game for white and black
    total_white_time = []
    total_black_time = []

    # Loop over each row (each game)
    for index, row in df.iterrows():
        # Identify columns with clock times (starting with 'Clock_ply_')
        clock_cols = [col for col in df.columns if col.startswith('Clock_ply_') and pd.notna(row[col])]
        
        # Convert available clock times to timedeltas
        times = [pd.to_timedelta(row[col]) for col in clock_cols]
        
        # Separate times into white and black based on odd/even indices
        white_times = [times[i] for i in range(len(times)) if i % 2 == 0]  # Odd plies (white)
        black_times = [times[i] for i in range(len(times)) if i % 2 != 0]  # Even plies (black)
        
        # Calculate total thinking time for white and black
        white_time = (white_times[-1] - white_times[0]) if white_times else pd.to_timedelta("0:00:00")
        black_time = (black_times[-1] - black_times[0]) if black_times else pd.to_timedelta("0:00:00")
        
        # Append to the lists
        total_white_time.append(white_time)
        total_black_time.append(black_time)

    # Add calculated times to the dataframe (in seconds for clarity)
    df['total_white_time_seconds'] = [time.total_seconds() for time in total_white_time]
    df['total_black_time_seconds'] = [time.total_seconds() for time in total_black_time]

    # Save the result to a new CSV file on the desktop
    output_path = "/Users/chrisbarza/Desktop/avg_time.csv"
    df[['total_white_time_seconds', 'total_black_time_seconds']].to_csv(output_path, index=False)

    print("The file 'avg_time.csv' has been saved to your desktop.")



