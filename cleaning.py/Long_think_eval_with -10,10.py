import pandas as pd

# Load the CSV file
df = pd.read_csv('/Users/chrisbarza/Desktop/Cleaned.csv')

# Clean the column names by stripping extra spaces (if any)
df.columns = df.columns.str.strip()

# Initialize the new columns for the differences
df['black_long_eval'] = None
df['white_long_eval'] = None

# Iterate through the rows to apply the logic
for i in range(len(df)):
    # For Black_Clock_Ply
    if pd.notnull(df.loc[i, 'Black_Clock_Ply']):
        ply_number = int(df.loc[i, 'Black_Clock_Ply'])  # Get Black_Clock_Ply value
        
        # Calculate the difference if the ply number is valid
        eval_ply_col1 = f"Eval_ply_{ply_number}"
        eval_ply_col2 = f"Eval_ply_{ply_number - 1}"
        
        if eval_ply_col1 in df.columns and eval_ply_col2 in df.columns:
            if pd.notnull(df.loc[i, eval_ply_col1]) and pd.notnull(df.loc[i, eval_ply_col2]):
                # Cap the values of Eval_ply_ columns before calculating the difference
                eval_ply_1 = df.loc[i, eval_ply_col1]
                eval_ply_2 = df.loc[i, eval_ply_col2]
                
                # Apply the cap for each evaluation value
                eval_ply_1 = max(-10, min(10, eval_ply_1))
                eval_ply_2 = max(-10, min(10, eval_ply_2))
                
                # Calculate the absolute difference for black
                eval_diff = abs(eval_ply_1 - eval_ply_2)
                
                # Cap the value to be between -10 and 10 (if needed)
                eval_diff = max(-10, min(10, eval_diff))
                df.loc[i, 'black_long_eval'] = eval_diff

    # For White_Clock_Ply
    if pd.notnull(df.loc[i, 'White_Clock_Ply']):
        ply_number = int(df.loc[i, 'White_Clock_Ply'])  # Get White_Clock_Ply value
        
        # Calculate the difference if the ply number is valid
        eval_ply_col1 = f"Eval_ply_{ply_number}"
        eval_ply_col2 = f"Eval_ply_{ply_number - 1}"
        
        if eval_ply_col1 in df.columns and eval_ply_col2 in df.columns:
            if pd.notnull(df.loc[i, eval_ply_col1]) and pd.notnull(df.loc[i, eval_ply_col2]):
                # Cap the values of Eval_ply_ columns before calculating the difference
                eval_ply_1 = df.loc[i, eval_ply_col1]
                eval_ply_2 = df.loc[i, eval_ply_col2]
                
                # Apply the cap for each evaluation value
                eval_ply_1 = max(-10, min(10, eval_ply_1))
                eval_ply_2 = max(-10, min(10, eval_ply_2))
                
                # Calculate the absolute difference for white
                eval_diff = abs(eval_ply_1 - eval_ply_2)
                
                # Cap the value to be between -10 and 10 (if needed)
                eval_diff = max(-10, min(10, eval_diff))
                df.loc[i, 'white_long_eval'] = eval_diff

# Save the cleaned DataFrame to a new CSV called 'long_eval.csv'
df.to_csv('/Users/chrisbarza/Desktop/long_eval.csv', index=False)

# Optional: Display the cleaned data (if you want to check the first few rows)
print(df[['Black_Clock_Ply', 'White_Clock_Ply', 'black_long_eval', 'white_long_eval']].head())

