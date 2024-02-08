"""
author: Niklaus Parcell
date Thursday 08 February 2024

"""

from run_barnacle import run_barnacle


"""
Config file example
"""

config = {    # PGA Tour Success
	"uid": "uid123123",  # a valid uid
	"barnacle_depth": {
		"main": 10
	},  # main is for every column, specify different depths for different columns 
	"cols_to_drop" :[
		"Player Name", 
		"Rounds", 
		"Wins", 
		"Points", 
		"Top 10", 
		"Year"
	],
	"comments": [
		"Testing Psychic Barnacle on new datasets"
	],
	"data_type": ".csv",  # Either .csv or .parquet 
	"path": "data/pga_engineered.csv",  # Path on your file system to .csv 
	"save_name": "api-runs/pga_tour.html",  # Save name for output files
	"target": "Money",  # Target column to be analyzed
	"partition_by": "Year",  # A way to partition, and prevent data leakage
	"wait_time": 60,
	"displays": {
		"target": "PGA Tour Season Earnings",
		"success_metric": "Higher earnings is good and relative to the average player",
		"green_is_top": True,  # False == Green is bottom, Red is Top
	}
}

run_barnacle(config)