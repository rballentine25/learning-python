import pandas as pd
import tensorflow as tf

# next-day-wildfire dataset is made up of tensorflow TFRecord files
data = pd.read_csv('next-day-wildfire-spread.csv')
print(data.head())