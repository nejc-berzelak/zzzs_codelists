# Just some change
import pandas as pd

def read_xls_codelist(file, sheets=None):
    """
    Read a codelist from Excel file and return a dataframe.
    filename_metadata: if True, the function attempts to read metadata from filename.
    """
    result = {}
    
    # Try to get metadata from filename.
    for sheet in sheets:
        # Read the sheet into a DataFrame
        df = pd.read_excel(file, sheet_name=sheet, header=None)
        
        # Find the header in a codelist Excel sheet. Code lists start on different rows in different sheets. 
        header_row = None
        for i, row in enumerate(df.values):
            if row[0] == "Šifra":
                header_row = i
                break
            
        if header_row is not None:
            # Set the header row as the column names
            df.columns = df.iloc[header_row]
            df = df[header_row + 1:]
            result[sheet] = df
        else:
            raise ValueError(f"Naslovne vrstice ni bilo mogoče najti na listu {sheet}.")
    
    return result

sifrant_2019_1 = read_xls_codelist(file="/Users/nejcb/WD/Šifranti/Sifranti_Cistopis_objava_1_2019.xlsx", 
                      sheets=["Š 15.7a", "Š 15.105"])
sifrant_2019_16 = read_xls_codelist(file="/Users/nejcb/WD/Šifranti/Sifranti_Cistopis_objava_16_2019.xlsx", 
                      sheets=["Š 15.7a", "Š 15.105"])

sifrant_2020_1 = read_xls_codelist(file="/Users/nejcb/WD/Šifranti/Sifranti_Cistopis_objava_1_2020.xlsx", 
                      sheets=["Š 15.7a", "Š 15.105"])
sifrant_2020_22 = read_xls_codelist(file="/Users/nejcb/WD/Šifranti/Sifranti_Cistopis_objava_22_2020.xlsx", 
                      sheets=["Š 15.7a", "Š 15.105"])

sifrant_2021_1 = read_xls_codelist(file="/Users/nejcb/WD/Šifranti/Sifranti_Cistopis_objava_1_2021.xlsx", 
                      sheets=["Š 15.7a", "Š 15.105"])
sifrant_2021_28 = read_xls_codelist(file="/Users/nejcb/WD/Šifranti/Sifranti_Cistopis_objava_28_2021.xlsx", 
                      sheets=["Š 15.7a", "Š 15.105"])

sifrant_2022_1 = read_xls_codelist(file="/Users/nejcb/WD/Šifranti/Sifranti_Cistopis_objava_1_2022.xlsx", 
                      sheets=["Š 15.7a", "Š 15.105"])
sifrant_2022_23 = read_xls_codelist(file="/Users/nejcb/WD/Šifranti/Sifranti_Cistopis_objava_23_2022.xlsx", 
                      sheets=["Š 15.7a", "Š 15.105"])

sifrant_2023_1 = read_xls_codelist(file="/Users/nejcb/WD/Šifranti/Sifranti_Cistopis_objava_1_2023.xlsx", 
                      sheets=["Š 15.7a", "Š 15.105"])
sifrant_2023_27 = read_xls_codelist(file="/Users/nejcb/WD/Šifranti/Sifranti_Cistopis_objava_27_2023.xlsx", 
                      sheets=["Š 15.7a", "Š 15.105"])

krneki