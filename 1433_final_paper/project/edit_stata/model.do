// Create log file
log using log.txt, text replace

// Import data
import excel ~/Documents/14.33/project/data/cleaned_data.xlsx, cellrange(A5:W3352)

// Pre-process any remaining data

// Summary statistics of our data
summarize

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
rename M hrs_delay_pop 		// population level
rename N hrs_delay_per_cap		// per capita level

// Travel time indices
rename O travel_index		// index corresponding to needed travel time
////////////////////////////////////////////////////////////////////////////////

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
////////////////////////////////////////////////////////////////////////////////


// Model 2: Fixed Effects with HAC estimators
////////////////////////////////////////////////////////////////////////////////

// First, let's make fixed effects for years and cities
xtset city_num  year // Sets cities and years to be our fixed effects


// Population regression models

// Excess fuel consumption: Approach [a]: OLS w/ Dummies
xi: reg excess_fuel_pop uber lyft uberXlyft i.city_num  i.year

// Excess fuel consuption: Approach [b]: Fixed Effects
xtreg excess_fuel_pop uber lyft uberXlyft, fe 

// Hours delay consumption: Approach [a]: OLS w/ Dummies
xi: reg hrs_delay_pop uber lyft uberXlyft i.city_num  i.year

// Hours delay consuption: Approach [b]: Fixed Effects
xtreg hrs_delay_pop  uber lyft uberXlyft, fe

// Per-capita regression models

// Excess fuel consumption: Approach [a]: OLS w/ Dummies
xi: reg excess_fuel_per_cap uber lyft uberXlyft i.city_num  i.year

// Excess fuel consuption: Approach [b]: Fixed Effects
xtreg excess_fuel_per_cap uber lyft uberXlyft, fe

// Hours delay consumption: Approach [a]: OLS w/ Dummies
xi: reg hrs_delay_per_cap uber lyft uberXlyft i.city_num  i.year

// Hours delay consuption: Approach [b]: Fixed Effects
xtreg hrs_delay_per_cap  uber lyft uberXlyft, fe

// Regress on time index

// Excess fuel consumption: Approach [a]: OLS w/ Dummies
xi: reg travel_index uber lyft uberXlyft i.city_num  i.year

// Excess fuel consuption: Approach [b]: Fixed Effects
xtreg travel_index  uber lyft uberXlyft, fe

////////////////////////////////////////////////////////////////////////////////


// Model 3: Fixed Effects and Controls with HAC estimators

// Population regression models

// Excess fuel consumption: Approach [a]: OLS w/ Dummies
xi: reg excess_fuel_pop uber lyft uberXlyft population pop_commuters free_travel arterial_street_travel time_value commercial_time_value avg_gas_cost avg_diesel_cost i.city_num  i.year

// Excess fuel consuption: Approach [b]: Fixed Effects
xtreg excess_fuel_pop uber lyft uberXlyft population pop_commuters free_travel arterial_street_travel time_value commercial_time_value avg_gas_cost avg_diesel_cost, fe

// Hours delay consumption: Approach [a]: OLS w/ Dummies
xi: reg hrs_delay_pop uber lyft uberXlyft population pop_commuters free_travel arterial_street_travel time_value commercial_time_value avg_gas_cost avg_diesel_cost i.city_num  i.year

// Hours delay consuption: Approach [b]: Fixed Effects
xtreg hrs_delay_pop  uber lyft uberXlyft population pop_commuters free_travel arterial_street_travel time_value commercial_time_value avg_gas_cost avg_diesel_cost, fe

// Per-capita regression models

// Excess fuel consumption: Approach [a]: OLS w/ Dummies
xi: reg excess_fuel_per_cap uber lyft uberXlyft population pop_commuters free_travel arterial_street_travel time_value commercial_time_value avg_gas_cost avg_diesel_cost i.city_num  i.year

// Excess fuel consuption: Approach [b]: Fixed Effects
xtreg excess_fuel_per_cap uber lyft uberXlyft population pop_commuters free_travel arterial_street_travel time_value commercial_time_value avg_gas_cost avg_diesel_cost, fe

// Hours delay consumption: Approach [a]: OLS w/ Dummies
xi: reg hrs_delay_per_cap uber lyft uberXlyft population pop_commuters free_travel arterial_street_travel time_value commercial_time_value avg_gas_cost avg_diesel_cost i.city_num  i.year

// Hours delay consuption: Approach [b]: Fixed Effects
xtreg hrs_delay_per_cap  uber lyft uberXlyft population pop_commuters free_travel arterial_street_travel time_value commercial_time_value avg_gas_cost avg_diesel_cost, fe

// Regress on time index

// Excess fuel consumption: Approach [a]: OLS w/ Dummies
xi: reg travel_index uber lyft uberXlyft population pop_commuters free_travel arterial_street_travel time_value commercial_time_value avg_gas_cost avg_diesel_cost i.city_num  i.year

// Excess fuel consuption: Approach [b]: Fixed Effects
xtreg travel_index  uber lyft uberXlyft population pop_commuters free_travel arterial_street_travel time_value commercial_time_value avg_gas_cost avg_diesel_cost, fe



// Model 4: Fixed Effects, Controls, and Instrumental Variables --> 2SLS

//TODO: Get unemployment data
gen unemp = 0

// Two-Stage Least Squares - population variables
ivregress 2sls excess_fuel_pop population pop_commuters free travel arterial_street_travel time_value commercial_time_value avg_gas_cost avg_diesel_cost i.city_num i.year (uber lyft uberXlyft=unemp), robust

ivregress 2sls hrs_delay_pop population pop_commuters free travel arterial_street_travel time_value commercial_time_value avg_gas_cost avg_diesel_cost i.city_num i.year (uber lyft uberXlyft=unemp), robust

// Two-Stage Least Squares - per capita variables
ivregress 2sls excess_fuel_per_cap population pop_commuters free travel arterial_street_travel time_value commercial_time_value avg_gas_cost avg_diesel_cost i.city_num i.year (uber lyft uberXlyft=unemp), robust

ivregress 2sls hrs_delay_per_cap population pop_commuters free travel arterial_street_travel time_value commercial_time_value avg_gas_cost avg_diesel_cost i.city_Num i.year (uber lyft uberXlyft=unemp), robust

// Time Index Regression
ivregress 2sls travel_index  population pop_commuters free travel arterial_street_travel time_value commercial_time_value avg_gas_cost avg_diesel_cost i.city_num i.year (uber lyft uberXlyft=unemp), robust

// Close log file
log close _all
clear
