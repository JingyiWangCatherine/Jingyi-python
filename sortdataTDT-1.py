import csv
import glob
import os
path=os.getcwd() # Path of directory containing data files.
extension = 'csv'
fieldnames = 'SS', 'STIME', 'LL', 'LTIME', 'key_resp_2.keys', 'participant' # look up the meanings of fieldnames in cheat sheet.
#output_folder = os.makesdirs (os.path.join(path," output", "")) # create a folder for output files.
output_filename = 'sort_allparticipants.csv'  # Output filename.
output_filepath = os.path.join(path, output_filename)  # Output in same directory.

csvlist = [filename for filename in glob.glob(os.path.join(path, f'*.{extension}'))
            if filename != output_filepath]  # Avoid reading any existing output file.
print(csvlist) # Print out the list of csv file names.

with open(output_filepath, 'w', newline='') as sortfile:
    csv_writer = csv.DictWriter(sortfile, fieldnames=fieldnames, delimiter=',',
                                extrasaction='ignore')
    csv_writer.writeheader()
    for file in csvlist:
        with open(file, 'r', newline='') as csvfile:
            csv_writer.writerows(csv.DictReader(csvfile))

import pandas as pd
import numpy as np
df = pd.read_csv(output_filepath, sep=',')
df.head()
df.rename(columns = {'SS' : 'A', 'STIME' : 'DA', 'LL' : 'B', 'LTIME' : 'DB', 'key_resp_2.keys' : 'R'}, inplace = True) #chnage header names.
df.loc[(df.R == 'left'),'R']='A'
df.loc[(df.R == 'right'),'R']='B'
df.loc[(df.DA == 'today'),'DA']='0'
df.loc[(df.DA == 'in 2 weeks'),'DA']='14'
df.loc[(df.DA == 'in 1 month'),'DA']='30'
df.loc[(df.DB == 'in 2 weeks'),'DB']='14'
df.loc[(df.DB == 'in 1 month'),'DB']='30'
df.loc[(df.DB == 'in 2 months'),'DB']='60'
df.loc[(df.DB == 'in 6 months'),'DB']='180'
pd.to_numeric(df.DA, downcast='integer')
pd.to_numeric(df.DB, downcast='integer') #convert to integer.

cleandf = df.dropna(subset=['A', 'B'], how='all') #data_1 dataframe that removed empty cells.

#print(df)
#split df into individual participants txt files. 
ID = cleandf.participant.unique()
for i in ID:
    suffix = '.txt'
    outputtxt = os.path.join(str(i) + suffix)
    header = "A\tDA\tB\tDB\tR"
    sortID1 = cleandf.loc[cleandf.participant == i] #get data for each participant.
    #print("The type is : ",type(sortID))
    sortID2 = sortID1.drop(columns=sortID1.columns[(sortID1 == i).any()]) #Delete the column of participant
    np.savetxt(outputtxt, sortID2, fmt='%s', delimiter="\t", header= header, comments='')

print('Done')