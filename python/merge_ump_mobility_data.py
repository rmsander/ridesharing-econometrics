# External package imports
import pandas as pd

def main():
    """Script for merging unemployment data into the urban mobility report
    dataset with Uber and Lyft indicator variables."""

    # Get data and create pandas dataframes
    f_umr = "../data/cleaned_data.xlsx"
    df_umr = pd.read_excel(f_umr)
    f_ump = "../data/unemployment_data.xlsx"
    df_ump = pd.read_excel(f_ump)

    # Get data from dataframe
    ump_years = df_ump["YEAR"]
    ump_cities = df_ump["CITY"]
    ump_values = df_ump["VALUE"]
    N = len(ump_years)
    dict_ump = {(ump_years[i], ump_cities[i]): ump_values[i] for i in range(N)}

    # Now read in data from mobility dataset
    umr_years = df_umr["Year"][3:]
    umr_city = df_umr["Urban Area"][3:]

    # Output data structure
    unemp_col = []

    # Iterate through (city, year) tuples
    for city, year in zip(umr_city, umr_years):
        if int(year) >= 2007 and int(year) <= 2017:
            unemp_col.append(dict_ump[(year, city)])
        else:
            unemp_col.append("")

    # Write to output dataframe
    df_umr["Unemployment Rate (%)"] = ["", "", ""] + unemp_col
    df_umr.to_excel("dataset.xlsx")

if __name__ == "__main__":
    main()