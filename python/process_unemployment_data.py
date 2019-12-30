# Native Python imports
import os
import itertools

# External package imports
import pandas as pd


def average_unemployment_data():
    """Scripting function for averaging unemployment data using the
    directories below."""

    # Get directories and files
    data_dir = "../../unemployment_data/"
    unemp_files = os.listdir(data_dir)
    N = len(unemp_files)  # Number of cities

    # Get city names
    city_names = [unemp_files[i][:-5] for i in range(N)]
    city_names.sort()
    avg_unp_per_year = {unemp_files[i][:-5]: {} for i in range(N)}

    # Iterate through files
    for file in unemp_files:  # Read each file in iteratively
        df = pd.read_excel(os.path.join(data_dir, file), skiprows=11)
        # Iterate through years in each file
        for year, value in zip(df["Year"], df["Observation Value"]):
            if int(year) == 2017:
                if year in list(avg_unp_per_year[file[:-5]].keys()):
                    avg_unp_per_year[file[:-5]][year] += value / 11
                else:
                    avg_unp_per_year[file[:-5]][year] = value / 11

    # Now we can write these results to a new excel file
    out_df = pd.DataFrame()
    out_df["CITY"] = list(
        itertools.chain(*[[city_names[i]] * 11 for i in range(N)]))

    # Get years and sort
    years = list(avg_unp_per_year[city_names[0]].keys())
    years.sort()

    # Append to output dataframe
    out_df["YEAR"] = list(itertools.chain(*[years for i in range(N)]))
    out_df["VALUE"] = list(itertools.chain(*[list(avg_unp_per_year[city_names[
        i]].values()) for i in range(N)]))

    # Save to excel file
    out_df.to_excel("unemployment_data.xlsx")
    print("Excel written to file")


def main():
    """Main function call"""
    average_unemployment_data()


if __name__ == "__main__":
    main()
