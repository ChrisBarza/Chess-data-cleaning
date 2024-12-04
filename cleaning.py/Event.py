import pandas as pd

# Load your CSV file
df = pd.read_csv('/Users/chrisbarza/Desktop/Cleaned.csv')

# Clean the column names if necessary
df.columns = df.columns.str.strip()

# Initialize a new column 'event', setting it to 0 by default
df['event'] = df['Event'].apply(lambda x: 1 if 'tournament' in str(x).lower() else 0)

# Save the updated DataFrame to a new CSV file
df.to_csv('/Users/chrisbarza/Desktop/Cleaned_with_event.csv', index=False)

# Optionally, display the first few rows to confirm the new column was added
print(df[['Event', 'event']].head())
