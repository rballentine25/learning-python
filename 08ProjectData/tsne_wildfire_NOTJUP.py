import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt 
import pandas as pd
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import time
import matplotlib.colors as mcolors

start = time.time()

#leave at this one to show dr raymer (this was weirdest). takes about 46s
df2 = pd.read_excel("mid-process-data-files/TO-COMBINE/eval_00_rearranged.xlsx")
df2.head()

# for tSNE, X is the features and Y is the labels (here just firemask)
X = df2.iloc[:, 2:] # start inclusive: this excludes firemask AND prev fire mask
Y = df2.iloc[:,0]

scaler = StandardScaler()
Xs = scaler.fit_transform(X)

n_dims = 3      # dimensions of the embedded space
tsne = TSNE(n_dims)
result = tsne.fit_transform(Xs)
#print(result.shape)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

result_df = pd.DataFrame({'TSNE_col1': result[:,0], 'TSNE_col2': result[:,1], 'TSNE_col3': result[:,2], 'label' : Y})

color_map = {-1:'cyan', 0:'gray', 1:'orange'}
color_num = result_df['label'].map(color_map)

ax.scatter3D(result_df['TSNE_col1'], result_df['TSNE_col2'], result_df['TSNE_col3'], c=color_num, cmap=mcolors.ListedColormap(list(color_map.values())))
end = time.time()
totaltime = end-start
print(totaltime)

plt.show(block=True)

