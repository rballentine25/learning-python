import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.patches as mpatches  # For custom legend

# Load the Excel file (update 'file.xlsx' and 'Sheet1' with the actual filename and sheet name)
file_path = '08ProjectData/mid-process-data-files/with_dict_files/test_00_with-data-dict.xlsx'
df = pd.read_excel(file_path, sheet_name='test_00')

# Assuming the binary data is in the first column
fireMask = df.iloc[:, 0].values
prevFireMask = df.iloc[:, 1].values

# Reshape into a 64x64 grid
grid1 = fireMask.reshape((64, 64))
grid2 = prevFireMask.reshape((64, 64))

# Define colors: 0 = light gray, 1 = red
cmap1 = mcolors.ListedColormap(["none", "red"])
cmap2 = mcolors.ListedColormap(["none", "blue"])


# Plot the grid with square pixels
plt.figure(figsize=(6,6))
plt.matshow(grid2, cmap=cmap2, fignum=1)  # `matshow` ensures square pixels
#plt.axis('off')  # Hide axes
plt.title("Test 00 FireMask")

plt.imshow(grid1, cmap=cmap1, alpha=0.7)  # Second grid (partially transparent)

# Create custom legend patches
legend_patches = [
    mpatches.Patch(color='white', label='0 (No Fire)'),
    mpatches.Patch(color='red', label='1 (FireMask at t=t+1 days)'),
    mpatches.Patch(color='blue', label='1 (PrevFireMask at t=t days)')
]

# Add the legend
plt.legend(handles=legend_patches, loc='lower left', fontsize=8, bbox_to_anchor=(0,0))


plt.show()


# ------------------------------------------------------
# plotting all 12 columns
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.colors as mcolors
# import matplotlib.patches as mpatches  # For custom legend

# # Load the Excel file (update 'file.xlsx' and 'Sheet1' with the actual filename and sheet name)
# file_path = '08ProjectData/mid-process-data-files/with_dict_files/train_00_with-data-dict.xlsx'
# df = pd.read_excel(file_path, sheet_name='train_00')

# # Assuming the binary data is in the first 12 columns
# # Adjust if the columns are different
# num_columns = 1
# fireMasks = df.iloc[:, :num_columns].values  # Extract the first 12 columns

# # Reshape each of the columns into 64x64 grid and prepare colormap
# grids = fireMasks.reshape(num_columns, 64, 64)  # Reshape to (12, 64, 64)
# # Define a standard colormap (e.g., "viridis", "plasma", etc.)
# cmap = plt.get_cmap('viridis')

# # Plot the stacked grids
# plt.figure(figsize=(6, 6))

# # Loop through each column/grid and plot it
# for i in range(num_columns):
#     grid = grids[i]
    
#     # Plot the grid (overlaying it on top of the previous ones)
#     plt.imshow(grid, cmap=cmap, alpha=0.7, interpolation='nearest')
    
# # Add custom legend (for the colormap values)
# # Add a colorbar to indicate the scale of values in the grids
# cbar = plt.colorbar(plt.imshow(grids[0], cmap=cmap, alpha=0.7))  # Use the first grid for colorbar reference
# cbar.set_label('Value Range')

# # Add title
# plt.title("Eval 00 Fire - Stacked Grids")

# plt.show()
