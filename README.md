# Econometrics for Ridesharing

## Overview
This repository details the work completed for my capstone Economics Class, 14.33.  In this class, I used different econometric techniques to estimate the causal effects of ridesharing technologies on traffic congestion and traffic-related emissions.  The main techniques I compared (in order of increasing complexity) for this paper were:

* Panel Regression
* Spatial and Temporal Fixed Effects
* Fixed Effects with Controls
* Fixed Effects, Controls, and Instrumental Variables

 ## Installation
 You can install the Python packages necessary for this project using pip, a Python package manager:
 
 `pip install -r requirements.txt`
 
 **Note**: To run the Stata code for econometric analysis, you will need access to a Stata interpreter.

## Datasets
For this project, I used data from the **Texas Transportation Institute 2019 Urban Mobility Report, Uber and Lyft entry data, U.S. Bureau of Labor Statistics, and the U.S. Census Bureau**.  The data for this project can be found in the `data/` sub-directory.

## Pre-Processing
A majority of the pre-processing for this project was completed in Python, using the `numpy` and `scipy` libraries for processing our data, and the `pandas` library for loading and saving our input and output DataFrame objects to be saved as .xlsx files.  The Python scripts used for pre-processing and merging our data can be found in the `python/` sub-directory.

## Analysis
Once our data was pre-processed and merged, we used the Stata language for econometric processing.  The Stata scripts used for econometric analysis can be found in the `stata/` sub-directory.

## Main Results
Our analysis finds that substantial **omitted variables bias** and **endogeneity** exists when estimating the causal effects of ride-hailing technologies on traffic congestion and congestion-related emissions.  We find a **negative, statistically-significant regression coefficient** for the effect of ride-hailing technologies on congestion costs per auto-commuter.  We also find that ride-hailing technologies have negative effects when we use the percentage of a population aged 65 or older as an instrumental variable, though because these coefficients are not statistically-significant and because we had to estimate some of our data for this instrument, we cannot conclude with complete confidence that these ride-hailing technologies decrease traffic congestion.  With more data, however, we can likely conclude that ride-hailing technologies decrease traffic congestion and congestion-related emissions.
