import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt 
import pandas as pd
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import time

start = time.time()

#leave at this one to show dr raymer (this was weirdest). takes about 46s
df = pd.read_excel("mid-process-data-files/TO-COMBINE/eval_00_rearranged.xlsx")
df.head()

# for tSNE, X is the features and Y is the labels (here just firemask)
X = df.iloc[:, 2:]
Y = df.iloc[:,0]

scaler = StandardScaler()
Xs = scaler.fit_transform(X)

n_dims = 3      # dimensions of the embedded space
tsne = TSNE(n_dims)
result = tsne.fit_transform(Xs)
#print(result.shape)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

color_map = {-1:'cyan', 0:'gray', 1:'orange'}
colors = [color_map[label] for label in Y]

result_df = pd.DataFrame({'TSNE_col1': result[:,0], 'TSNE_col2': result[:,1], 'TSNE_col3': result[:,2], 'label' : Y})
ax.scatter3D(result_df['TSNE_col1'], result_df['TSNE_col2'], result_df['TSNE_col3'], c=colors)
end = time.time()
totaltime = end-start
print(totaltime)

plt.show(block=True)

