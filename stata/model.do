// Create log file
log using log_with_age_sig002.txt, text replace

// Import data
import excel ~/Documents/14.33/project/data/dataset_with_age_sigma002.xlsx, cellrange(A5:Y3316)

// Pre-process any remaining data

////////////////////////////////////////////////////////////////////////////////

// Define variables for our panel regression, FE, and 2SLS models


// [1] Fixed Effects
rename A cities			 // Create spatial fixed effects with
encode cities, gen(city_num) 	// Encode as numbers for dummies
rename B year   			// Create temporal fixed effects with

// [2] Controls
rename C population          // in 1000s
rename D pop_commuters      // in 1000s
rename E free_travel
rename F arterial_street_travel
rename G time_value
rename H commercial_time_value
rename I avg_gas_cost
rename J avg_diesel_cost

// [3] Regressors
rename U uber 	// panel data for uber indicators
rename V lyft 	// panel data for lyft indicators
rename W uberXlyft   // panel data for product of indicators

// [4] Regressands

// Excess fuel consumed
rename K excess_fuel_pop		// population level
rename L excess_fuel_per_cap		// per capita level

// Annual delays
rename M hrs_delay_pop 			// population level
rename N hrs_delay_per_cap		// per capita level

// Travel time indices
rename O travel_index		// index corresponding to needed travel time

// Congestion cost
rename Q congestion_cost_per_cap

// Unemployment rate instrument
rename X unemp 		// Panel data from 2007-2017 for local unemployment rates

// Age instrument
rename Y age65      // Cross-sectional data with panel data estimate

////////////////////////////////////////////////////////////////////////////////

// Summary statistics of our data
summarize

// Now we can go ahead and define some different models

// Model 1: Pooled OLS with HAC estimators
////////////////////////////////////////////////////////////////////////////////
// Population regressions
reg excess_fuel_pop uber lyft uberXlyft, robust
reg hrs_delay_pop uber lyft uberXlyft, robust

// Individual regressions
reg excess_fuel_per_cap uber lyft uberXlyft, robust
reg hrs_delay_per_cap  uber lyft uberXlyft, robust

// Regress on time index
reg travel_index uber lyft uberXlyft, robust

// Regress on congestion cost
reg congestion_cost_per_cap uber lyft uberXlyft, robust

////////////////////////////////////////////////////////////////////////////////


// Model 2: Fixed Effects with HAC estimators
////////////////////////////////////////////////////////////////////////////////

// First, let's make fixed effects for years and cities
xtset city_num  year // Sets cities and years to be our fixed effects


// Population regression models

// Excess fuel consumption: Approach [a]: OLS w/ Dummies
xi: reg excess_fuel_pop uber lyft uberXlyft i.city_num  i.year

// Excess fuel consuption: Approach [b]: Fixed Effects
xtreg excess_fuel_pop uber lyft uberXlyft i.year, fe 

// Hours delay consumption: Approach [a]: OLS w/ Dummies
xi: reg hrs_delay_pop uber lyft uberXlyft i.city_num  i.year

// Hours delay consuption: Approach [b]: Fixed Effects
xtreg hrs_delay_pop  uber lyft uberXlyft i.year, fe

// Per-capita regression models

// Excess fuel consumption: Approach [a]: OLS w/ Dummies
xi: reg excess_fuel_per_cap uber lyft uberXlyft i.city_num  i.year

// Excess fuel consuption: Approach [b]: Fixed Effects
xtreg excess_fuel_per_cap uber lyft uberXlyft i.year, fe

// Hours delay consumption: Approach [a]: OLS w/ Dummies
xi: reg hrs_delay_per_cap uber lyft uberXlyft i.city_num  i.year

// Hours delay consuption: Approach [b]: Fixed Effects
xtreg hrs_delay_per_cap  uber lyft uberXlyft i.year, fe

// Regress on time index

// Travel time index: Approach [a]: OLS w/ Dummies
xi: reg travel_index uber lyft uberXlyft i.city_num  i.year

// Travel time index: Approach [b]: Fixed Effects
xtreg travel_index  uber lyft uberXlyft i.year, fe


// Regress on congestion cost

// Congestion cost: Approach [a]: OLS w/ Dummies
xi: reg congestion_cost_per_cap uber lyft uberXlyft i.city_num  i.year

// Congestion cost: Approach [b]: Fixed Effects
xtreg congestion_cost_per_cap  uber lyft uberXlyft i.year, fe


////////////////////////////////////////////////////////////////////////////////


// Model 3: Fixed Effects and Controls with HAC estimators

// Population regression models

// Excess fuel consumption: Approach [a]: OLS w/ Dummies
xi: reg excess_fuel_pop uber lyft uberXlyft population pop_commuters free_travel arterial_street_travel time_value commercial_time_value avg_gas_cost avg_diesel_cost i.city_num  i.year

// Excess fuel consuption: Approach [b]: Fixed Effects
xtreg excess_fuel_pop uber lyft uberXlyft population pop_commuters free_travel arterial_street_travel time_value commercial_time_value avg_gas_cost avg_diesel_cost i.year, fe

// Hours delay consumption: Approach [a]: OLS w/ Dummies
xi: reg hrs_delay_pop uber lyft uberXlyft population pop_commuters free_travel arterial_street_travel time_value commercial_time_value avg_gas_cost avg_diesel_cost i.city_num  i.year

// Hours delay consuption: Approach [b]: Fixed Effects
xtreg hrs_delay_pop  uber lyft uberXlyft population pop_commuters free_travel arterial_street_travel time_value commercial_time_value avg_gas_cost avg_diesel_cost i.year, fe

// Per-capita regression models

// Excess fuel consumption: Approach [a]: OLS w/ Dummies
xi: reg excess_fuel_per_cap uber lyft uberXlyft population pop_commuters free_travel arterial_street_travel time_value commercial_time_value avg_gas_cost avg_diesel_cost i.city_num  i.year

// Excess fuel consuption: Approach [b]: Fixed Effects
xtreg excess_fuel_per_cap uber lyft uberXlyft population pop_commuters free_travel arterial_street_travel time_value commercial_time_value avg_gas_cost avg_diesel_cost i.year, fe

// Hours delay consumption: Approach [a]: OLS w/ Dummies
xi: reg hrs_delay_per_cap uber lyft uberXlyft population pop_commuters free_travel arterial_street_travel time_value commercial_time_value avg_gas_cost avg_diesel_cost i.city_num  i.year

// Hours delay consuption: Approach [b]: Fixed Effects
xtreg hrs_delay_per_cap  uber lyft uberXlyft population pop_commuters free_travel arterial_street_travel time_value commercial_time_value avg_gas_cost avg_diesel_cost i.year, fe

// Regress on time index

// Excess travel time index: Approach [a]: OLS w/ Dummies
xi: reg travel_index uber lyft uberXlyft population pop_commuters free_travel arterial_street_travel time_value commercial_time_value avg_gas_cost avg_diesel_cost i.city_num  i.year

// Excess travel time index: Approach [b]: Fixed Effects
xtreg travel_index uber lyft uberXlyft population pop_commuters free_travel arterial_street_travel time_value commercial_time_value avg_gas_cost avg_diesel_cost i.year, fe

// Regress on congestion cost

// Congestion cost: Approach [a]: OLS w/ Dummies
xi: reg congestion_cost_per_cap uber lyft uberXlyft population pop_commuters free_travel arterial_street_travel time_value commercial_time_value avg_gas_cost avg_diesel_cost i.city_num  i.year

// Congestion cost: Approach [b]: Fixed Effects
xtreg congestion_cost_per_cap uber lyft uberXlyft population pop_commuters free_travel arterial_street_travel time_value commercial_time_value avg_gas_cost avg_diesel_cost i.year, fe


// Model 4: Fixed Effects, Controls, and Instrumental Variables --> 2SLS

// Since we only have one instrument, take sum of uber+lyft
gen sum_rideshare = uber + lyft

// Two-Stage Least Squares - population variables
ivregress 2sls excess_fuel_pop population pop_commuters free_travel arterial_street_travel time_value commercial_time_value avg_gas_cost avg_diesel_cost i.city_num i.year (sum_rideshare=age65), robust

ivregress 2sls hrs_delay_pop population pop_commuters free_travel arterial_street_travel time_value commercial_time_value avg_gas_cost avg_diesel_cost i.city_num i.year (sum_rideshare=age65), robust

// Two-Stage Least Squares - per capita variables
ivregress 2sls excess_fuel_per_cap population pop_commuters free_travel arterial_street_travel time_value commercial_time_value avg_gas_cost avg_diesel_cost i.city_num i.year (sum_rideshare=age65), robust

ivregress 2sls hrs_delay_per_cap population pop_commuters free_travel arterial_street_travel time_value commercial_time_value avg_gas_cost avg_diesel_cost i.city_num i.year (sum_rideshare=age65), robust

// Time Index Regression
ivregress 2sls travel_index population pop_commuters free_travel arterial_street_travel time_value commercial_time_value avg_gas_cost avg_diesel_cost i.city_num i.year (sum_rideshare=age65), robust

// Congestion Cost Regression
ivregress 2sls congestion_cost_per_cap population pop_commuters free_travel arterial_street_travel time_value commercial_time_value avg_gas_cost avg_diesel_cost i.city_num i.year (sum_rideshare=age65), robust



// Close log file
log close _all
clear
