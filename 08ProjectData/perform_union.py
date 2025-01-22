import pandas as pd
import os
from datetime import date



namepatt = ['eval', 'test', 'train']
dataframes = {}

folder = '08ProjectData/mid-process-data-files/TO-COMBINE/'
for name in namepatt: 
    count=0
    for filename in os.listdir(folder):
        if filename.startswith(name):
            df_name = ('df_' + name + '_' + str(count))
            dataframes[df_name] = pd.read_excel(os.path.join(folder, filename))
            count+=1       
        
    combined_df = pd.concat(dataframes.values(), ignore_index=True)

    combName = name + '_COMBINED_' + date.today().strftime("%Y%m%d") 
    with pd.ExcelWriter(('08ProjectData/' + combName + '.xlsx'), engine='openpyxl') as writer:
        combined_df.to_excel(writer, sheet_name=(name + ' data (ALL)'), index=False)

    combined_df.to_pickle('08ProjectData/pickle-files/' + combName + '.pkl')
    print('done with ' + name + ' group')
    dataframes.clear()

print('done')
