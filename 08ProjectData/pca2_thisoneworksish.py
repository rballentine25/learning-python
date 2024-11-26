import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

filename1 = 'C:/Users/rball/OneDrive/Documents/school/24-25 fall/Git Repos f24/learning-python/08ProjectData/eval_00_pickle.pk1'
df_eval00 = pd.read_pickle(filename1)

# target is FireMask which is first column so exclude it from feature array 
features = df_eval00.columns[1:]
print(features)

# start with 3 dimensions for 3d plot
pca = PCA(n_components = 3) # initialize pca object
pca_result = pca.fit_transform(df_eval00[features].values) # calculate principal components and project data

#pca_result is now numpy array w/three columns, one for each component
# append columns with reduced rep 
df_eval00['pca-1'] = pca_result[:,0]
df_eval00['pca-2'] = pca_result[:,1]
df_eval00['pca-3'] = pca_result[:,2]

# print variation:
print('variation per princ comp: {}'.format(pca.explained_variance_ratio_))

# graphs
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16,10))


# printing in 2d:
sns.scatterplot(
    x="pca-1", y='pca-2',
    hue="FireMask",
    palette=sns.color_palette("hls", 2),
    data=df_eval00,
    legend="full",
    ax=ax1
)

# printing in 3d:
ax2 = fig.add_subplot(122, projection ='3d')
ax2.scatter(
    xs=df_eval00["pca-1"], 
    ys=df_eval00["pca-2"], 
    zs=df_eval00["pca-3"], 
    c=df_eval00["FireMask"], 
)
ax2.set_xlabel('pca-1')
ax2.set_ylabel('pca-2')
ax2.set_zlabel('pca-3')

plt.show()
