import os
import pandas as pd
import itertools


def average_unemployment_data():
    data_dir = "../../unemployment_data/"
    unemp_files = os.listdir(data_dir)
    N = len(unemp_files)  # Number of cities
    city_names = [unemp_files[i][:-5] for i in range(N)]  # City names
    city_names.sort()
    avg_unp_per_year = {unemp_files[i][:-5]: {} for i in range(N)}
    print(avg_unp_per_year)

    for file in unemp_files:  # Read each file in iteratively
        df = pd.read_excel(os.path.join(data_dir, file), skiprows=11)
        for year, value in zip(df["Year"], df["Observation Value"]):
            if int(year) == 2017:
                print(file)
            if year in list(avg_unp_per_year[file[:-5]].keys()):
                avg_unp_per_year[file[:-5]][year] += value/11
            else:
                avg_unp_per_year[file[:-5]][year] = value/11

    # Now we can write these results to a new excel file
    out_df = pd.DataFrame()
    out_df["CITY"] = list(itertools.chain(*[[city_names[i]]*11 for i in range(N)]))

    years = list(avg_unp_per_year[city_names[0]].keys())
    years.sort()
    out_df["YEAR"] = list(itertools.chain(*[years for i in range(N)]))
    out_df["VALUE"] = list(itertools.chain(*[list(avg_unp_per_year[city_names[
        i]].values()) for i in range(N)]))

    out_df.to_excel("unemployment_data.xlsx")
    print("Excel written to file")

def main():
    average_unemployment_data()

if __name__ == "__main__":
    main()
