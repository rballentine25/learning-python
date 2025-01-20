import pandas as pd
import numpy as np

name = 'test_00'
filepath = 'C:/Users/rball/OneDrive/Documents/school/24-25 fall/Git Repos f24/learning-python/08ProjectData/csv-files/'+ name + '.xlsx'

df_dict = pd.read_excel(filepath)
print(df_dict)

minimum = []
maximum = []
means = []
medians = []

for field in df_dict:
    minimum.append(min(df_dict[field]))
    maximum.append(max(df_dict[field]))
    means.append(df_dict[field].mean())
    medians.append(df_dict[field].median())

fields = df_dict.columns.to_numpy()
print(fields)

#desc = ['Precipitation amount', 'Palmer severity drought index', 'Population amount', 'Maxmimum temperature',
#        'Wind velocity at 10m', 'Fire mask at time t +1 day', 'Specific humidity', 'Wind direction', 'Fire mask at time t',
#       'Elevation above sea level', 'Normalized difference vegetation index', 'Minimum temperature', 'Energy release component']

df_sheet2 = pd.DataFrame({
    'Fields' : fields,
    #'Description' : desc,
    'Minimim' : minimum,
    'Maximum' : maximum,
    'Mean' : means,
    'Median' : medians
})

print(df_sheet2)

with pd.ExcelWriter(filepath, engine='openpyxl', mode='a', if_sheet_exists='new') as writer:
    df_sheet2.to_excel(writer, sheet_name='DataDict', index=False)