import pandas as pd

# Step 1: Read the CSV file
data = pd.read_csv('/Users/chrisbarza/Desktop/Actual data.csv', low_memory=False)

# Step 2: Add columns for each possible outcome based on the 'Result' column
data['white_won'] = (data['Result'] == '1-0').astype(int)
data['black_won'] = (data['Result'] == '0-1').astype(int)
data['draw'] = (data['Result'] == '1/2-1/2').astype(int)

# Save the updated DataFrame back to the same CSV file
data.to_csv('/Users/chrisbarza/Desktop/Actual data.csv', index=False)

print("Added 'white_won', 'black_won', and 'draw' columns to 'Actual data.csv'.")


