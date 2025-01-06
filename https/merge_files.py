import pandas as pd

# List of file names to merge
files = ['file_1.xlsx', 'file_2.xlsx', 'file_3.xlsx', 'file_4.xlsx']

# Read each Excel file and store them in a list
dataframes = [pd.read_excel(file) for file in files]

# Concatenate all DataFrames into a single DataFrame
merged_df = pd.concat(dataframes, ignore_index=True)

# Reset the 'Sno' column to a new sequence from 1 to the length of the DataFrame
merged_df['Sno'] = range(1, len(merged_df) + 1)

# Save the merged DataFrame to a new Excel file
merged_df.to_excel('merged_file.xlsx', index=False)

