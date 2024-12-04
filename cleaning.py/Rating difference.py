import pandas as pd

# Step 1: Read the CSV file
data = pd.read_csv('/Users/chrisbarza/Desktop/Actual data.csv', low_memory=False)

# Step 2: Calculate the difference and add it as a new column
data['EloDifference'] = data['WhiteElo'] - data['BlackElo']

# Save the updated DataFrame back to the same CSV file
data.to_csv('/Users/chrisbarza/Desktop/Actual data.csv', index=False)

print("Added 'EloDifference' column to 'Actual data.csv'.")
