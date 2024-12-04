file_path = '/Users/chrisbarza/Desktop/Cleaned.csv'
import pandas as pd

# Use the absolute file path
file_path = '/Users/chrisbarza/Desktop/Cleaned.csv'  # Adjust if necessary

# Try reading the CSV file
try:
    chess_data = pd.read_csv(file_path)
    print("File loaded successfully!")
except FileNotFoundError:
    print(f"Error: The file at {file_path} was not found. Please check the path.")
    exit()  # Exit the program if file is not found

# Process the data (as before)
last_move = chess_data.notnull().idxmax(axis=1)
chess_data['game_duration'] = last_move.apply(lambda x: int(x.split('_')[1]) if x.startswith('Clock_ply') else 0)

for index, row in chess_data.iterrows():
    last_ply = row['game_duration']
    chess_data.loc[index, f'Clock_ply_{last_ply+1}':] = None  # Set columns after the last move to NaN

# Save the cleaned data
chess_data.to_csv('/Users/chrisbarza/Desktop/Cleaned_Trimmed.csv', index=False)

# Confirm the cleaned data
print(chess_data.head())
















