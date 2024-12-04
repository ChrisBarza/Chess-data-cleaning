import pandas as pd

# Step 1: Read the CSV file
data = pd.read_csv('/Users/chrisbarza/Desktop/longest_moment.csv', low_memory=False)

# Step 2: Identify the columns that start with 'Eval_ply_'
eval_columns = [col for col in data.columns if col.startswith('Eval_ply_')]

# Step 3: Define a function to transform the values
def transform_value(x):
    if isinstance(x, str):
        if x.startswith('#'):
            return 10
        elif x.startswith('#-'):
            return -10
    if isinstance(x, (int, float)):
        if x > 10:
            return 10
        elif x < -10:
            return -10
    return x  # Keep the value if it's between -10 and 10

# Apply the transformation to the relevant columns
for col in eval_columns:
    data[col] = data[col].apply(transform_value)

# Convert the columns to numeric, forcing errors to NaN
data[eval_columns] = data[eval_columns].apply(pd.to_numeric, errors='coerce')

# Step 4: Initialize lists to store maximum differences and eval ply moments
max_diff_white = []
eval_ply_moment_white = []
max_diff_black = []
eval_ply_moment_black = []

# Step 5: Calculate maximum differences for each game
for index, row in data.iterrows():
    max_diff_w = None
    eval_ply_m_w = None
    max_diff_b = None
    eval_ply_m_b = None

    for i in range(1, len(eval_columns)):
        if pd.api.types.is_numeric_dtype(row[eval_columns[i]]) and pd.api.types.is_numeric_dtype(row[eval_columns[i - 1]]):
            # Calculate the shifts
            white_diff = row[eval_columns[i]] - row[eval_columns[i - 1]]  # n+1 - n (White)
            black_diff = row[eval_columns[i - 1]] - row[eval_columns[i]]  # n - (n-1) (Black)

            # Track maximum differences for White (odd indices)
            if i % 2 == 1:  # Odd index for White
                if max_diff_w is None or abs(white_diff) > abs(max_diff_w):
                    max_diff_w = white_diff
                    eval_ply_m_w = eval_columns[i]

            # Track maximum differences for Black (even indices)
            if i % 2 == 0:  # Even index for Black
                if max_diff_b is None or abs(black_diff) > abs(max_diff_b):
                    max_diff_b = black_diff
                    eval_ply_m_b = eval_columns[i - 1]

    # Append the maximum differences and their moments for each game
    max_diff_white.append(max_diff_w)
    eval_ply_moment_white.append(eval_ply_m_w)
    max_diff_black.append(max_diff_b)
    eval_ply_moment_black.append(eval_ply_m_b)

# Step 6: Add new columns to the DataFrame in one go
data['Max_Diff_White'] = max_diff_white
data['Eval_Ply_Moment_White'] = eval_ply_moment_white
data['Max_Diff_Black'] = max_diff_black
data['Eval_Ply_Moment_Black'] = eval_ply_moment_black

# Step 7: Save the updated DataFrame to a new CSV file
data.to_csv('/Users/chrisbarza/Desktop/complete.csv', index=False)

print("Maximum differences for White and Black with eval ply moments saved to complete.csv")

































































