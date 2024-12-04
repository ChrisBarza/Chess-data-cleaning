import pandas as pd
import os

# Define the file path
file_path = '/Users/chrisbarza/Desktop/Cleaned.csv'

# Check if the file exists
if not os.path.isfile(file_path):
    print(f"File not found: {file_path}")
else:
    # Load the dataset
    data = pd.read_csv(file_path)

    # Define the function to categorize Elo with the 1600-1800 range
    def categorize_elo(elo):
        if elo < 1000:
            return '<1000'
        elif 1000 <= elo < 1200:
            return '1000-1200'
        elif 1200 <= elo < 1400:
            return '1200-1400'
        elif 1400 <= elo < 1600:
            return '1400-1600'
        elif 1600 <= elo < 1800:
            return '1600-1800'
        elif 1800 <= elo < 2000:
            return '1800-2000'
        elif 2000 <= elo < 2200:
            return '2000-2200'
        else:
            return '2200>'

    # Update the WhiteEloCategory column
    data['WhiteEloCategory'] = data['WhiteElo'].apply(categorize_elo)

    # Remove any existing binary columns for WhiteElo categories to avoid conflicts
    binary_columns = [col for col in data.columns if col.startswith('WhiteElo_')]
    data = data.drop(columns=binary_columns, errors='ignore')

    # Define categories and create new binary columns
    categories = ['<1000', '1000-1200', '1200-1400', '1400-1600', '1600-1800', '1800-2000', '2000-2200', '2200>']
    for category in categories:
        col_name = f'WhiteElo_{category.replace(">", "greater_than").replace("-", "_to_")}'
        data[col_name] = (data['WhiteEloCategory'] == category).astype(int)

    # Save the updated DataFrame back to the original CSV file
    data.to_csv(file_path, index=False)

    print("White Elo categories and binary columns have been updated with the 1600-1800 range and saved to 'Cleaned.csv'.")







