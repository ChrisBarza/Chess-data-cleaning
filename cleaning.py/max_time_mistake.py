import pandas as pd
import os

# Define the path to the CSV file on your Desktop
file_path = os.path.expanduser('~/Desktop/Cleaned.csv')

# Load the data from Cleaned.csv
df = pd.read_csv(file_path)

# Initialize the new column
df['Eval_longest_think'] = None

# Loop through the rows of the DataFrame
for index, row in df.iterrows():
    current_clock = row['Black_Clock_Ply']
    
    # Check if current_clock is greater than or equal to 2
    if current_clock >= 2:
        # Get values of Eval_ply for n-1 and n-2
        eval_n_minus_1 = df.loc[df['Black_Clock_Ply'] == current_clock - 1, f'Eval_ply_{current_clock - 1}']
        eval_n_minus_2 = df.loc[df['Black_Clock_Ply'] == current_clock - 2, f'Eval_ply_{current_clock - 2}']
        
        # Check if both evaluations exist
        if not eval_n_minus_1.empty and not eval_n_minus_2.empty:
            eval_diff = abs(eval_n_minus_1.values[0] - eval_n_minus_2.values[0])
            # Update the Eval_longest_think in the original DataFrame
            df.at[index, 'Eval_longest_think'] = eval_diff

# Define the path for the new CSV file
new_file_path = os.path.expanduser('~/Desktop/Updated_Cleaned.csv')

# Save the modified DataFrame to a new CSV file
df.to_csv(new_file_path, index=False)

# Confirm that the file has been saved
print(f'Modified data has been saved to {new_file_path}')






