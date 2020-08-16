# Open the election results and read the file.
import csv
import os
file_to_load = os.path.join("/Users/shalisahills/Desktop/GW Data Analytics Bootcamp/Election_Analysis/analysis/election_results.csv")
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

# Create a filename variable to a direct path to the text file.
file_to_save = os.path.join("/Users/shalisahills/Desktop/GW Data Analytics Bootcamp/Election_Analysis/analysis/election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    # Write three counties to the file.
     txt_file.write("Counties in the Election\n --------------------\nArapahoe\nDenver\nJefferson")







# Close the file       