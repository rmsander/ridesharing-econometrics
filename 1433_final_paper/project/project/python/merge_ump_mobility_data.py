"""Script for merging unemployment data into the urban mobility report
dataset with Uber and Lyft indicator variables."""

import os
import pandas as pd

def main():
    f_umr = "../data/cleaned_data.xlsx"
    df_umr = pd.read_excel(f_umr)

    f_ump = "../data/unemployment_data.xlsx"
    df_ump = pd.read_excel(f_ump)

    ump_years = df_ump["YEAR"]
    ump_cities = df_ump["CITY"]
    ump_values = df_ump["VALUE"]
    N = len(ump_years)
    dict_ump = {(ump_years[i], ump_cities[i]): ump_values[i] for i in range(N)}

    # Now read in data from mobility dataset
    umr_years = df_umr["Year"][3:]
    umr_city = df_umr["Urban Area"][3:]


    unemp_col = []
    for city, year in zip(umr_city, umr_years):
        print(city, year)
        if int(year) >= 2007 and int(year) <= 2017:
            print(city, year)
            unemp_col.append(dict_ump[(year, city)])
        else:
            unemp_col.append("")

    print(len(unemp_col))
    print(len(umr_years))
    df_umr["Unemployment Rate (%)"] = ["", "", ""] + unemp_col
    df_umr.to_excel("dataset.xlsx")

if __name__ == "__main__":
    main()