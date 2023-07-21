
# Create a class that can be called to fix the formatting of the csv in this dir (sample.csv) and return it as a df. 
# BONUS: Return the data grouped in the best manner you see fit.
import pandas as pd

class CSVFormatter:
    def __init__(self, file_path):
        self.file_path = file_path

    def fix_formatting(self):
        try:
            # Read the CSV file into a DataFrame
            df = pd.read_csv(self.file_path)

            # Perform any necessary data formatting or cleaning here
            # For example, you can use the pandas functions to remove duplicates, handle missing values, etc.

            # Return the fixed DataFrame
            return df
        except Exception as e:
            print("An error occurred while formatting the CSV:", e)
            return None

# Example usage
if __name__ == "__main__":
    csv_file_path = "sample.csv"
    formatter = CSVFormatter(csv_file_path)
    formatted_df = formatter.fix_formatting()

    if formatted_df is not None:
        print("Formatted DataFrame:")
        print(formatted_df)
