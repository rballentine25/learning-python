import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler


filename1 = 'C:/Users/rball/OneDrive/Documents/school/24-25 fall/Git Repos f24/learning-python/08ProjectData/eval_00_pickle.pk1'
df_eval00 = pd.read_pickle(filename1)

#print(df_eval00.head())

print('Size of the dataframe: {}'.format(df_eval00.shape))

features = df_eval00.columns
#print(features)

X = df_eval00[features]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# t-SNE application in 3D
tsne = TSNE(n_components=3, perplexity=30, random_state=42)
X_tsne_3d = tsne.fit_transform(X_scaled)

# Visualization
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot in 3D
ax.scatter(X_tsne_3d[:, 0], X_tsne_3d[:, 1], X_tsne_3d[:, 2], c='blue', s=50, edgecolor='k')

# Setting titles and labels
ax.set_title("3D t-SNE Visualization")
ax.set_xlabel("t-SNE Dimension 1")
ax.set_ylabel("t-SNE Dimension 2")
ax.set_zlabel("t-SNE Dimension 3")
plt.show()