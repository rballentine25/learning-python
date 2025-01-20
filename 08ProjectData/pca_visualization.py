import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

filename1 = 'C:/Users/rball/OneDrive/Documents/school/24-25 fall/Git Repos f24/learning-python/08ProjectData/eval_00_pickle.pk1'
df_eval00 = pd.read_pickle(filename1)

# Normalize the data (optional but recommended for PCA)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df_eval00)

# Apply PCA
pca = PCA(n_components=3)  # Reduce to 2 dimensions for visualization
pca_result = pca.fit_transform(scaled_data)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot
ax.scatter(pca_result[:, 0], pca_result[:, 1], pca_result[:, 2], c='green', s=50, edgecolor='k')

# Add titles and labels
ax.set_title('3D PCA Visualization')
ax.set_xlabel('Principal Component 1')
ax.set_ylabel('Principal Component 2')
ax.set_zlabel('Principal Component 3')

plt.show()

# Explained variance ratio
print("Explained Variance Ratio:", pca.explained_variance_ratio_)

print(df_eval00["FireMask"])
