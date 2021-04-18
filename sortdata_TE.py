import csv
import glob
import os
path=os.getcwd()
#path = r'C:\Users\cat\Desktop\lab work\Regina Lapate lab\works\Anorexia project\Time estimates task\modified psychopy\reading data-2'  # Path of directory containing data files.
extension = 'csv'
fieldnames = 'key_resp.rt', 'key_resp_4.rt', 'participant'
output_filename = 'sort.csv'  # Output filename.
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
#remove rows if both key_resp.rt and key_resp_4.rt are empty
import pandas as pd
import numpy as np
df = pd.read_csv(output_filepath, sep=',')
df.head()
data_1 = df.dropna(subset=['key_resp.rt', 'key_resp_4.rt'], how='all') #data_1 dataframe that removed empty cells.
#add target number
s=np.array([20,30,40,50,15,20,25,30])
n=int((data_1.shape[0])/8)
conditionvec=np.tile(s,n)
data_1.insert(3,"target number", conditionvec,True)
print(data_1) #help to check the data before put it into a new excel file
with pd.ExcelWriter('sortfinal.xlsx') as writer:  
    df.to_excel(writer, sheet_name='noncleaned')
    data_1.to_excel(writer, sheet_name='cleaned')
print('Done')