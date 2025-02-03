import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt 
import pandas as pd
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
import time

start = time.time()

#leave at this one to show dr raymer (this was weirdest). takes about 46s
df2 = pd.read_excel("mid-process-data-files/TO-COMBINE/train_07_rearranged.xlsx")
df2.head()

# for tSNE, X is the features and Y is the labels (here just firemask)
X2 = df2.iloc[:, 1:]
Y2 = df2.iloc[:,0]

n_dims = 3      # dimensions of the embedded space
tsne = TSNE(n_dims)
result2 = tsne.fit_transform(X2)
#print(result.shape)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

result2_df = pd.DataFrame({'TSNE_col1': result2[:,0], 'TSNE_col2': result2[:,1], 'TSNE_col3': result2[:,2], 'label' : Y2})
ax.scatter3D(result2_df['TSNE_col1'], result2_df['TSNE_col2'], result2_df['TSNE_col3'], c=Y2, cmap='viridis')
end = time.time()
totaltime = end-start
print(totaltime)

plt.show(block=True)

