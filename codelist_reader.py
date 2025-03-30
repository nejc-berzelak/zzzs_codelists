import pandas as pd

def read_xls_codelist(file, filename_metadata=True, sheets=None):
    """
    Read a codelist from Excel file and return a dataframe.
    filename_metadata: if True, the function attempts to read metadata from filename.
    """
    
    # Try to get metadata from filename.
    if filename_metadata:
        pattern = r'_([0-9]{2})_([0-9]{4})'
        match = re.search(pattern, file)
        if match:
            month, year = match.groups()
            month = int(month)
            year = int(year)
        else:
            raise ValueError("Filename does not contain valid year and month metadata.")

    for sheet in sheets:
        # Read the sheet into a DataFrame
        df = pd.read_excel(file, sheet_name=sheet, header=None)
        
        # Find the header in a codelist Excel sheet. Code lists start on different rows in different sheets. 
        for i, row in enumerate(df.values):
            if row[0] == "Šifra":
                header_row = i
                break
            
        if header_row is not None:
            # Set the header row as the column names
            df.columns = df.iloc[header_row]
            df = df[header_row + 1:]
            return df
        else:
            raise ValueError(f"Naslovne vrstice ni bilo mogoče najti na listu {sheet}.")



