import os
import pandas as pd
import itertools
import scipy
from scipy.stats import linregress
import numpy as np


def make_age_data():
    # Read in input dataframe
    dataset = pd.read_excel(os.path.join("..", "data", "dataset.xlsx"))
    print("LENGTH {}".format(len(dataset['Year'])))
    age_percents = []

    # Read in dataframe for age
    age_data = pd.read_excel(os.path.join("..", "data", "age_stats.xlsx"))
    print(age_data)

    # Now iterate through and append each column to our aggregate dataset
    percent_vals = age_data['Percent']
    counter = 0
    city_counter = 0
    for percent_val in percent_vals:
        city_counter += 1
        vals_estimate = fit_exp_reg(percent_val)
        print(vals_estimate)
        for year in range(1982, 2018):
            counter += 1
            if year < 2008:
                age_percents.append(np.nan)
            else:
                age_percents.append(vals_estimate[year-2008])
    
    # Write output to dataset
    new_list = ["", "", "", ""]+age_percents
    print(len(new_list))
    print("COUNTER IS {}".format(counter))
    print("CITY COUNTER IS {}".format(city_counter))
    dataset['age_65_perc'] = new_list
    dataset.to_excel(os.path.join("..", "data",
                                  "dataset_with_age_sigma002.xlsx"))
    
def fix_lin(data):
    return linregress(data[0], data[1])

def fix_exp():
    x = np.array([10, 9, 8, 7, 6, 5])
    y = np.array([.154, .149, .145, .142, .139, .134])
    print(scipy.optimize.curve_fit(lambda t,a,b: a*np.exp(b*t), x, y))


def fit_exp_reg(est):
    x = [i for i in range(1, 11)]
    preds = [(0.11784032*est/0.154)*np.exp(0.02644067*x[
        i]) for i in range(10)]
    for pred in preds[:-2]:
        print("HERE", pred)
        pred += np.random.normal(loc=pred, scale=0.01)
    return preds

def no_fit(est):
    return [est for i in range(5)]


def fit_lin_reg(est, a):
    return [est - a * (9 - i) for i in range(10)]


def main():
    fix_exp()
    # Yields .386
    make_age_data()



if __name__ == "__main__":
    main()
