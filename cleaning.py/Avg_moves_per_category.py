import pandas as pd

# Load the CSV file
df = pd.read_csv('/Users/chrisbarza/Desktop/200k_blitz_rapid_classical_bullet copy.csv')

# Clean the column names by stripping extra spaces (if any)
df.columns = df.columns.str.strip()

# Initialize a list to store the move length for each game
game_move_length = []

# Iterate through each game (row)
for i in range(len(df)):
    # Loop over the columns for moves (Move_ply_1 to Move_ply_200)
    for move_num in range(1, 201):  # Checking for moves 1 through 200
        move_col = f"Move_ply_{move_num}"
        if pd.notnull(df.loc[i, move_col]):
            last_move = move_num  # Update the last move number
    game_move_length.append(last_move)

# Add the move length as a new column in the dataframe
df['game_move_length'] = game_move_length

# Save the result to a new CSV file
df[['game_move_length']].to_csv('/Users/chrisbarza/Desktop/game_move_length.csv', index=False)

# Calculate the overall average game length
average_game_length = df['game_move_length'].mean()

# Print the overall average game length
print(f"Average Game Length: {average_game_length:.2f} moves")

# Assuming there is a 'Category' column in the dataset that indicates the game type
# Calculate the average game length per category
average_game_length_by_category = df.groupby('Category')['game_move_length'].mean()

# Print the average game length per category
print("\nAverage Game Length by Category:")
print(average_game_length_by_category)
