import tensorflow as tf

import numpy as np
import pandas as pd

filename = 'C:/Users/rball/OneDrive/Documents/school/24-25 fall/Git Repos f24/learning-python/08ProjectData/next-day-wildfire-spread/next_day_wildfire_spread_eval_00.tfrecord'
filenames = [filename]
raw_dataset = tf.data.TFRecordDataset(filenames)
name = 'eval_00'

count = sum(1 for _ in raw_dataset)

print(f'Total number of entries: {count}')

for raw_record in raw_dataset.take(1000):
  example = tf.train.Example()
  example.ParseFromString(raw_record.numpy())
  #print(example)

result = {}
# example.features.feature is the dictionary
for key, feature in example.features.feature.items():
  # The values are the Feature objects which contain a `kind` which contains:
  # one of three fields: bytes_list, float_list, int64_list

  kind = feature.WhichOneof('kind')
  result[key] = np.array(getattr(feature, kind).value)

print(result)

print("\n")
print(result['tmmx'])

df = pd.DataFrame(result)
print(df.head())

#df.to_pickle(name + '_pickle.pk1')
df.to_csv('C:/Users/rball/OneDrive/Documents/school/24-25 fall/Git Repos f24/learning-python/08ProjectData/'+ name + '.csv', index=False)