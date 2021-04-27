import csv
import glob
import os
path=os.getcwd() # Path of directory containing data files.
extension = 'csv'
fieldnames = 'slider.response', 'slider.rt', 'next_trial.rt', 'estimatedurations' , 'participant' # look up the meanings of fieldnames in cheat sheet.
#output_folder = os.makesdirs (os.path.join(path," output", "")) # create a folder for output files.
output_filename = 'sort_ZT.csv'  # Output filename.
output_filepath = os.path.join(path, output_filename)  # Output in same directory.

csvlist = [filename for filename in glob.glob(os.path.join(path, f'*.{extension}'))
            if filename != output_filepath]  # Avoid reading any existing output file.
#print(csvlist) # Print out the list of csv file names.
import pandas as pd
import numpy as np
li = []
for file in csvlist:
    df = pd.read_csv(file, usecols = fieldnames, delimiter =',', header = 0)
    li.append(df) 
dfall = pd.concat(li, axis=0, ignore_index=True) 

cleandf = dfall.dropna(subset=['slider.response', 'slider.rt', 'next_trial.rt', 'estimatedurations'], how='all') # removed empty cells.
cleandf.to_csv(output_filepath, sep=',', index=False)

print('Done')