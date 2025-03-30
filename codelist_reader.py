import pandas as pd

def read_xls_codelist(file, filename_metadata=True, sheets=None):
    """
    Read a codelist from Excel file and return a dataframe.
    filename_metadata: if True, the function attempts to read metadata from filename.
    """
    
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


read_xls_codelist("/Users/nejcb/WD/Sifranti_Cistopis_objava_11_2025 (1).xlsx", sheets=["Š 6"])




def extract_metadata_from_filename(filename):
    """
    Extract year and month metadata from the filename.
    Assumes the filename contains the pattern '_MM_YYYY'.
    """
    pattern = r'_([0-9]{2})_([0-9]{4})'
    match = re.search(pattern, filename)
    if match:
        month, year = match.groups()
        return int(year), int(month)
    else:
        raise ValueError("Filename does not contain valid year and month metadata.")

# Example usage
filename = "Sifranti_Cistopis_objava_11_2025 (1).xlsx"
year, month = extract_metadata_from_filename(filename)
print(f"Year: {year}, Month: {month}")




# df = pd.read_excel("/Users/nejcb/WD/Sifranti_Cistopis_objava_11_2025 (1).xlsx", 
#                    sheet_name="Š 4", header=None)

# for i, row in  enumerate(df.values):
#     if row[0] == "Šifra":
#         print(i)
    