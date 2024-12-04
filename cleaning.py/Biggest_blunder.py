import pandas as pd

# Step 1: Load your dataset (update the path to your CSV file on the Desktop)
df = pd.read_csv('/Users/chrisbarza/Desktop/longest_moment.csv')

# Step 2: Process Eval_ply according to the specified rules
def process_eval_ply(eval_ply):
    if pd.isna(eval_ply):  # Check for NaN values
        return eval_ply
    if eval_ply > 10:
        return 10
    elif eval_ply < -10:
        return -10
    elif eval_ply >= 0:  # Positive values
        return 10
    else:  # Negative values
        return -10

# Apply the function to all Eval_ply columns
eval_columns = [col for col in df.columns if col.startswith('Eval_ply_')]
for eval_col in eval_columns:
    df[eval_col] = df[eval_col].apply(process_eval_ply)

# Step 3: Calculate the differences between consecutive Eval_ply entries
blunder_results = []

# Loop through the evaluation columns in pairs
for i in range(len(eval_columns) - 1):
    eval_white = df[eval_columns[i]]
    eval_black = df[eval_columns[i + 1]]
    
    # Calculate the differences
    white_diff = eval_black - eval_white
    black_diff = eval_white - eval_black
    
    # Identify biggest blunders
    white_blunders = white_diff[white_diff < 0].abs()  # White's blunders when black improves
    black_blunders = black_diff[black_diff < 0].abs()  # Black's blunders when white improves
    
    if not white_blunders.empty:
        max_white_blunder = white_blunders.max()
        moment_white = white_blunders.idxmax()
        blunder_results.append({'Moment': moment_white, 'Player': 'White', 'Blunder': max_white_blunder})

    if not black_blunders.empty:
        max_black_blunder = black_blunders.max()
        moment_black = black_blunders.idxmax()
        blunder_results.append({'Moment': moment_black, 'Player': 'Black', 'Blunder': max_black_blunder})

# Step 4: Convert results to a DataFrame
blunder_df = pd.DataFrame(blunder_results)

# Step 5: Add blunder results to the original DataFrame
# Create new columns for blunders
df['Moment'] = None
df['Player'] = None
df['Blunder'] = None

# Fill in the blunder data
for idx, row in blunder_df.iterrows():
    df.loc[df.shape[0] - len(blunder_df) + idx, ['Moment', 'Player', 'Blunder']] = row

# Step 6: Save the updated DataFrame to a new CSV file
df.to_csv('/Users/chrisbarza/Desktop/longest_moment_with_blunders.csv', index=False)

print("Blunders added to longest_moment_with_blunders.csv on Desktop")
















