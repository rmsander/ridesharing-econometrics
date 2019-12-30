# Native Python packages
import os

# External python packages
import pandas as pd
import scipy
from scipy.stats import linregress
import numpy as np


def make_age_data():
    """Function for reading in our full dataset, creating estimates for each
    city-time pair, and writing these estimates to a new dataset in addition
    to our old dataset."""

    # Read in input dataframe
    dataset = pd.read_excel(os.path.join("..", "data", "dataset.xlsx"))
    age_percents = []

    # Read in dataframe for age
    age_data = pd.read_excel(os.path.join("..", "data", "age_stats.xlsx"))

    # Now iterate through and append each column to our aggregate dataset
    percent_vals = age_data['Percent']
    counter = 0
    city_counter = 0
    for percent_val in percent_vals:
        city_counter += 1
        vals_estimate = fit_exp_reg(percent_val)  # Fit exponential model
        for year in range(1982, 2018):  # Iterate through years
            counter += 1
            if year < 2008:  # Don't add significant value before 2008
                age_percents.append(np.nan)
            else:  # Add for significant values
                age_percents.append(vals_estimate[year - 2008])

    # Write output to dataset
    new_list = ["", "", "", ""] + age_percents
    dataset['age_65_perc'] = new_list
    dataset.to_excel(os.path.join("..", "data",
                                  "dataset_with_age_sigma002.xlsx"))


def fix_lin(data):
    """Linear regression of input data argument.  Assumes data is an array
    of length two, with x = data[0], and y = data[1]."""
    return linregress(data[0], data[1])


def fix_exp(data):
    """Exponential regression of input data argument.  Assumes data is an array
    of length two, with x = data[0], and y = data[1]."""
    x = np.array(data[0])
    y = np.array(data[1])
    print(scipy.optimize.curve_fit(lambda t, a, b: a * np.exp(b * t), x, y))


def fit_exp_reg(est, a=0.11784032 / 0.154, b=0.02644067, sigma=0.01):
    """Exponential regression of input data argument.  Assumes est is a value
    corresponding to the sole observation for a specific city."""
    x = [i for i in range(1, 11)]
    preds = [(a * est) * np.exp(b * x[i]) for i in range(10)]
    for pred in preds[:-1]:  # Now add noise, except to observed value
        pred += np.random.normal(loc=0, scale=sigma)
    return preds


def main():
    """Main argument for script."""
    make_age_data()


if __name__ == "__main__":
    main()
