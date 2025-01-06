import pandas as pd

def remove_duplicate_titles_and_reset_sno(filename):
    # Read the Excel file
    df = pd.read_excel(filename)
    
    # Print the original DataFrame size
    print(f"Original DataFrame size: {df.shape}")
    
    # Remove duplicates based on the 'Title' column, keeping the first occurrence
    df_unique = df.drop_duplicates(subset='Title', keep='first')
    
    # Reset the 'Sno' column to range from 1 up to the length of the DataFrame
    df_unique['Sno'] = range(1, len(df_unique) + 1)
    
    # Print the new DataFrame size to compare
    print(f"New DataFrame size after removing duplicates and resetting Sno: {df_unique.shape}")
    
    # Save the cleaned DataFrame back to Excel
    df_unique.to_excel('cleaned_file.xlsx', index=False)
    print("Cleaned file has been saved as 'cleaned_file.xlsx'.")

remove_duplicate_titles_and_reset_sno('merged_file.xlsx')
