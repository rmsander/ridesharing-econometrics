# Native Python imports
import copy

# External package imports
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def main():
    """Main scripting function for plotting our data."""

    # Get dataset and create pandas dataframe
    f_data = "../data/dataset.xlsx"
    df = pd.read_excel(f_data)

    # Get variables for indices
    years = list(set(df["Year"][3:]))
    years_arr = df["Year"][3:]

    # Get values from dataset
    population = df["Population.1"][3:]
    auto_commuters = df["Auto"][3:]
    free_traffic = df["Freeway"][3:]
    arterial_traffic = df["Arterial Street"][3:]
    general_time_value = df["Cost Components"][3:]
    commercial_time_value = df["Unnamed: 12"][3:]
    gasoline_cost = df["Unnamed: 13"][3:]
    diesel_cost = df["Unnamed: 14"][3:]
    excess_fuel_per_commuter = df["Unnamed: 20"][3:]
    annual_hrs_of_delay = df["Unnamed: 24"][3:]
    travel_time_index = df["Travel Time Index"][3:]
    cost_per_autocommuter = df["Unnamed: 34"][3:]
    uber = df["Uber Entry Dummies"][3:]
    lyft = df["Lyft Entry Dummies"][3:]
    both = df["UberXlyft"][3:]
    unemployment = df["Unemployment Rate (%)"][3:]

    # Get covariances
    filled_ump = copy.deepcopy(unemployment).fillna(value=0)
    print("Correlation of uber and ump: {}".format(np.corrcoef(filled_ump, uber)))
    print("Correlation of lyft and ump: {}".format(np.corrcoef(filled_ump, lyft)))
    print("Covariance of tti and ump: {}".format(np.corrcoef(filled_ump,
                                travel_time_index.astype(np.float32))))
    print("Covariance of cost and ump: {}".format(np.corrcoef(filled_ump,
                                cost_per_autocommuter.astype(np.float32))))
    print("Covariance of excess and ump: {}".format(np.corrcoef(filled_ump,
                                excess_fuel_per_commuter.astype(np.float32))))
    print("Covariance of delay and ump: {}".format(np.corrcoef(filled_ump,
                                annual_hrs_of_delay.astype(np.float32))))

    # Create output data structure
    year_dict = {years[i]: {"pop": [], "auto": [], "free": [], "art": [],
                            "gen_time": [], "comm_time": [], "gas": [], "diesel":
                            [], "ann_delay": [], "travel_index": [], "cost":
                            [], "ub": [], "ly": [], "bo": [], "ump": [],
                            "excess_gas": []} for i in range(len(years))}

    # Counter variable
    i = 0

    # Iterate through everything for plots
    for year, pop, auto, free, art, gen_time, comm_time, gas, diesel, excess_gas, \
        ann_delay, travel_index, cost, ub, ly, bo, ump in \
            zip(years_arr, population, auto_commuters, free_traffic,
                arterial_traffic, general_time_value, commercial_time_value,
                gasoline_cost, diesel_cost, excess_fuel_per_commuter,
                annual_hrs_of_delay, travel_time_index, cost_per_autocommuter,
                uber, lyft, both, unemployment):

        # Append values to dictionary for plotting
        year_dict[year]["pop"].append(pop)
        year_dict[year]["auto"].append(auto)
        year_dict[year]["free"].append(free)
        year_dict[year]["art"].append(art)
        year_dict[year]["gen_time"].append(gen_time)
        year_dict[year]["comm_time"].append(comm_time)
        year_dict[year]["gas"].append(gas)
        year_dict[year]["diesel"].append(diesel)
        year_dict[year]["ann_delay"].append(ann_delay)
        year_dict[year]["travel_index"].append(travel_index)
        year_dict[year]["cost"].append(cost)
        year_dict[year]["ub"].append(ub)
        year_dict[year]["ly"].append(ly)
        year_dict[year]["bo"].append(bo)
        year_dict[year]["ump"].append(ump)
        year_dict[year]["excess_gas"].append(excess_gas)

    # Average values according to year
    for key_i in list(year_dict.keys()):
        for key_j in list(year_dict[key_i].keys()):
            vals = copy.deepcopy(year_dict[key_i][key_j])
            year_dict[key_i][key_j] = np.mean(vals)

    # Now make arrays for time series data
    pop_by_year = [year_dict[years[i]]["pop"] for i in range(len(years))]
    auto_by_year = [year_dict[years[i]]["auto"] for i in range(len(years))]
    free_by_year = [year_dict[years[i]]["free"] for i in range(len(years))]
    art_by_year = [year_dict[years[i]]["art"] for i in range(len(years))]
    gen_time_by_year = [year_dict[years[i]]["gen_time"] for i in range(len(years))]
    comm_time_by_year = [year_dict[years[i]]["comm_time"] for i in range(len(
        years))]
    gas_by_year = [year_dict[years[i]]["gas"] for i in range(len(years))]
    diesel_by_year = [year_dict[years[i]]["diesel"] for i in range(len(years))]
    ann_delay_by_year = [year_dict[years[i]]["ann_delay"] for i in range(len(
        years))]
    travel_index_by_year = [year_dict[years[i]]["travel_index"] for i in
                            range(len(years))]
    cost_by_year = [year_dict[years[i]]["cost"] for i in range(len(years))]
    ub_by_year = [year_dict[years[i]]["ub"] for i in range(len(years))]
    ly_by_year = [year_dict[years[i]]["ly"] for i in range(len(years))]
    bo_by_year = [year_dict[years[i]]["bo"] for i in range(len(years))]
    ump_by_year = [year_dict[years[i]]["ump"] for i in range(len(years))]
    excess_gas_per_year = [year_dict[years[i]]["excess_gas"] for i in range(len(
        years))]


    # Make plots
    plt.plot(years, pop_by_year)
    plt.xlabel("Year")
    plt.ylabel("Average Population of UMR Urban Centers (1000s)")
    plt.title("Average Population of Urban Mobility Report Urban Centers over Time")
    plt.savefig("../graphs/pop_vs_time.png")
    plt.clf()

    plt.plot(years, auto_by_year)
    plt.xlabel("Year")
    plt.ylabel("Autocommuters (1000s)")
    plt.title("Average Number of Autocommuters in UMI Urban Centers (1000s)")
    plt.savefig("../graphs/auto_vs_time.png")
    plt.clf()

    plt.plot(years, free_by_year, color="b", label="Freeways")
    plt.plot(years, art_by_year, color="r", label="Arterial Roads")
    plt.legend()
    plt.xlabel("Year")
    plt.ylabel("Driving Distance (miles)")
    plt.title("Average Net Freeway/Arterial Road Driving over Time ("
              "1000s of miles)")
    plt.savefig("../graphs/dist_vs_time.png")
    plt.clf()

    plt.plot(years, gen_time_by_year, color="b", label="General Value")
    plt.plot(years, comm_time_by_year, color="r", label="Commercial Value")
    plt.legend()
    plt.xlabel("Year")
    plt.ylabel("Value ($/hr)")
    plt.title("Average General and Commercial Values of Time over Time")
    plt.savefig("../graphs/val_of_time_vs_time.png")
    plt.clf()

    plt.plot(years, gas_by_year, color="b", label="Gasoline")
    plt.plot(years, diesel_by_year, color="r", label="Diesel")
    plt.legend()
    plt.xlabel("Year")
    plt.ylabel("Cost ($/gallon)")
    plt.title("Average Cost of Gasoline and Diesel Fuel over Time")
    plt.savefig("../graphs/gas_vs_time.png")
    plt.clf()

    plt.plot(years, ann_delay_by_year)
    plt.xlabel("Year")
    plt.ylabel("Annual per-Commuter Traffic Delays (hrs)")
    plt.title("Average Annual per-Commuter Traffic Delays over Time")
    plt.savefig("../graphs/delay_vs_time.png")
    plt.clf()

    plt.plot(years, travel_index_by_year)
    plt.xlabel("Year")
    plt.ylabel("Travel Index")
    plt.title("Average Travel Index over Time")
    plt.savefig("../graphs/index_vs_time.png")
    plt.clf()

    plt.plot(years, ump_by_year)
    plt.xlabel("Year")
    plt.ylabel("Unemployment Rate (%)")
    plt.title("Average Unemployment Rate over Time")
    plt.savefig("../graphs/ump_vs_time.png")
    plt.clf()

    plt.plot(years, cost_by_year)
    plt.xlabel("Year")
    plt.ylabel("Cost ($)")
    plt.title("Average Annual per-Capita Cost of Traffic Congestion over Time")
    plt.savefig("../graphs/cost_vs_time.png")
    plt.clf()

    plt.plot(years, excess_gas_per_year)
    plt.xlabel("Year")
    plt.ylabel("Excess Fuel Consumed (Gallons)")
    plt.title("Average Annual per-Capita Excess Fuel Consumed over Time")
    plt.savefig("../graphs/extra_fuel_vs_time.png")
    plt.clf()

    x = list(lyft)  # Lyft data
    y = list(uber)  # Uber data
    bins = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]

    plt.hist([x, y], bins, label=['Lyft', 'Uber'])
    plt.legend(loc='upper right')
    plt.xlabel("Year")
    plt.ylabel("Number of cities entered")
    plt.title("Uber and Lyft Entry into Urban Mobility Report Cities")
    plt.clf()

if __name__=="__main":
    main()