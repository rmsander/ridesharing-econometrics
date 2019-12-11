"""Script for importing different sources of data, combining them
intelligently, and creating a new dataset."""

# Native Python imports
import os
import sys
import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt
import math

plt.style.use('seaborn-deep')

f_urban_mobility = "umr_tti_2017.xlsx"
f_uber_lyft = "uber_lyft_entry.xlsx"

umr_df = pd.read_excel(f_urban_mobility)
uber_lyft_df = pd.read_excel(f_uber_lyft)

print(umr_df)
print(uber_lyft_df)


# Let's get some summary statistics on Uber and Lyft entry
def histogram(data, b=10):
    """Returns a histogram of data"""
    return np.histogram(data, bins=b)


# Uber data keys and values
keys_uber = list(uber_lyft_df.keys())
values_uber = uber_lyft_df.values[:, -2:-1].T[0]
values_lyft = uber_lyft_df.values[:, -1:].T[0]
print(values_lyft)
print(values_uber)

x = list(values_lyft)
y = list(values_uber)
bins = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]

plt.hist([x, y], bins, label=['Lyft', 'Uber'])
plt.legend(loc='upper right')
plt.xlabel("Year")
plt.ylabel("Number of cities entered")
plt.title("Uber and Lyft Entry into Urban Mobility Report Cities")
plt.clf()

years = umr_df["Year"][3:]
cities = umr_df["Urban Area"][3:]
locations = uber_lyft_df["City Expanded"]
states = uber_lyft_df["State(s)"]

uber_entry_dummies = [-1]*len(cities)
lyft_entry_dummies = [-1]*len(cities)
count = 0

for loc, state, uber_year, lyft_year in zip\
            (locations, states, values_uber, values_lyft):
    urban_area = str(loc+" "+state)
    print("Number of cities finished: {}".format(count))
    print(urban_area)
    index = 0
    for city, year in zip(cities, years):
        if urban_area == city:
            if not math.isnan(uber_year):
                if year >= uber_year:
                    uber_entry_dummies[index] = 1
                else:
                    uber_entry_dummies[index] = 0


            if not math.isnan(lyft_year):
                if year >= lyft_year:
                    lyft_entry_dummies[index] = 1
                else:
                    lyft_entry_dummies[index] = 0


        index += 1
    count += 1

umr_df["Uber Entry Dummies"] = [np.nan, np.nan,
                                          np.nan] + uber_entry_dummies
umr_df["Lyft Entry Dummies"] = [np.nan, np.nan,
                                          np.nan] + lyft_entry_dummies

umr_df.to_excel("umr_rideshare.xlsx")
