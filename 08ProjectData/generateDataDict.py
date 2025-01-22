import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from openpyxl import load_workbook
from openpyxl.drawing.image import Image
import os
import warnings

warnings.filterwarnings("ignore", message="use_inf_as_na option is deprecated")

name = 'eval_COMBINED_20250121.xlsx'
filedest = 'C:/Users/rball/OneDrive/Documents/school/24-25 fall/Git Repos f24/learning-python/08ProjectData/'
filepath = filedest + name

if filepath.endswith('.xlsx'):
    df_dict = pd.read_excel(filepath)
elif filepath.endswith('.csv'):
    df_dict = pd.read_csv(filepath)

new_order = ['FireMask', 'PrevFireMask', 'tmmn', 'tmmx', 'vs', 'th', 'pr', 'sph', 'pdsi', 'elevation', 'NDVI', 'erc', 'population']
df_dict = df_dict[new_order]

#print(df_dict.isnull().sum())

minimum = []
maximum = []
means = []
medians = []
descs = []
zero_vals = []
zero_percent = []
numentries = df_dict.shape[0]

descriptions = {
    'pr' : 'Precipitation amount',
    'pdsi' : 'Palmer severity drought index',
    'tmmx' : 'Maxmimum temperature',
    'vs' : 'Wind velocity at 10m',
    'FireMask' : 'Fire mask at time t +1 day',
    'sph' : 'Specific humidity',
    'th' : 'Wind direction',
    'PrevFireMask' : 'Fire mask at time t',
    'elevation' : 'Elevation above sea level',
    'NDVI' : 'Normalized difference vegetation index',
    'tmmn' : 'Minimum temperature',
    'erc' : 'Energy release component',
    'population' : 'Population'
}

for field in df_dict:
    minimum.append(min(df_dict[field]))
    maximum.append(max(df_dict[field]))
    means.append(df_dict[field].mean())
    medians.append(df_dict[field].median())
    descs.append(descriptions[field])

    num_zeros = 0
    for value in df_dict[field]:
        if value == 0:
            num_zeros += 1

    zero_vals.append(num_zeros)
    zero_percent.append(num_zeros/numentries * 100)


# num_entries = [None] * len(minimum)
# num_entries[0] = df_dict.shape[0]

fields = df_dict.columns.to_numpy()

df_sheet2 = pd.DataFrame({
    'Fields' : fields,
    'Description' : descs,
    'Minimim' : minimum,
    'Maximum' : maximum,
    'Mean' : means,
    'Median' : medians,
    '# of 0 values' : zero_vals,
    'Percentage of 0 values' : zero_percent
    #'Total entries in file' : num_entries
})

df_sheet3 = pd.DataFrame({
    'Fields' : fields
})

folder = 'with_dict_files/'
if filepath.endswith('.csv'):
    new_excel = filedest + folder + name + '_with-data-dict' + '.xlsx'
    with pd.ExcelWriter(new_excel, engine='openpyxl') as writer:
        df_dict.to_excel(writer, sheet_name=(name + ' data'), index=False)
        df_sheet2.to_excel(writer, sheet_name='data dictionary', index=False)
        #df_sheet3.to_excel(writer, sheet_name='distributions', index=False)
if filepath.endswith('.xlsx'):
     with pd.ExcelWriter(filepath, engine='openpyxl', mode='a', if_sheet_exists="new") as writer:
        df_sheet2.to_excel(writer, sheet_name='data dictionary', index=False)
        df_sheet3.to_excel(writer, sheet_name='distributions', index=False)


############# DISTRIBUTION PLOTS WITH SEABORN ###############
row = 2
dim = 300
for field in df_dict:
    imgname = field + '.png'
    sns.histplot(df_dict[field], kde=True)
    plt.savefig(imgname, format='png')
    plt.close()  
    
    wb = load_workbook(filepath); ws = wb['distributions']
    ws.column_dimensions['B'].width = dim/6; ws.row_dimensions[row].height = dim*(5/6)

    img = Image(imgname)
    img.width=dim+50; img.height=dim
    cell = 'B' + str(row)
    ws.add_image(img, cell)
    row += 1
    wb.save(filepath)

for field in df_dict:
    os.remove(field + '.png')

