import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the CSV file
file_path = 'path_to_your_csv_file.csv'  # Replace with your CSV file path
data = pd.read_csv(file_path)

# Step 2: Plotting each slice separately
unique_slices = data['Slice'].unique()
plt.figure()

for slice_number in unique_slices:
    slice_data = data[data['Slice'] == slice_number]
    plt.plot(slice_data['xc'], slice_data['Cp'], label=f'Slice {slice_number}')

plt.title('Plot of Cp vs xc for Each Slice')
plt.xlabel('Normalized x-coordinate (xc)')
plt.ylabel('Pressure Coefficient (Cp)')
plt.legend()
plt.show()
