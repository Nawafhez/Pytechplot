import tecplot as tp
from tecplot.constant import *
import pandas as pd
import numpy as np
import sys
import os
import logging

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

import sys
if '-c' in sys.argv:
    tp.session.connect()

tp.new_layout()

# Calling the file into Tecplot
tp.macro.execute_command("""$!ReadDataSet  '\"STANDARDSYNTAX\" \"1.0\" \"FILENAME_FILE\" \"/storage/home/nka5267/work/surface_flow.vtu\"'
  DataSetReader = 'VTK Data Loader'
  ReadDataOption = New
  ResetStyle = No
  AssignStrandIDs = Yes
  InitialPlotType = Automatic
  InitialPlotFirstZoneOnly = No
  AddZonesToExistingStrands = No
  VarLoadMode = ByName""")

# Get the active frame and its plot
page = tp.active_page()
page.name = 'Slices'
frame = page.active_frame()
tp.active_frame().plot_type=PlotType.Cartesian3D
plot = frame.plot()
ds = tp.active_frame().dataset

# Set contour variables & colormap
plot.contour(1).variable_index = 1
plot.contour(1).colormap_name = 'Small Rainbow'

# Show contour and slices
plot.show_contour = False
plot.show_slices = True

# Allow user to specify the number of slices
num_slices = int(input("Enter the number of slices: "))

# Calculate the slice positions
y = ds.zone(0).values(1)[:]
Y = pd.Series(y)
Ymin = Y.min() + 0.01
Ymax = Y.max() - 0.03
slice_positions = np.linspace(Ymin, Ymax, num_slices)


# Set slices properties and create slices
for i, y1 in enumerate(slice_positions):
    slice_ = plot.slice(i)
    slice_.show = True
    slice_.slice_source = tp.constant.SliceSource.SurfaceZones
    slice_.orientation = tp.constant.SliceSurface.YPlanes
    slice_.origin.y = y1
    slice_.edge.show = False
    slice_.mesh.show = True
    slice_.mesh.color = plot.contour(1)
    slice_.mesh.line_thickness = 0.8

# Extract slices
slice_indices = range(num_slices)
extracted_slices = plot.slices(*slice_indices).extract(transient_mode=tp.constant.TransientOperationMode.AllSolutionTimes)


all_slices_data = pd.DataFrame()

# Matplotlib plot
for i, extracted_slice in enumerate(extracted_slices):

    zone = ds.zone(i+1)

    extracted_Cp = zone.values(11)[:]
    extracted_x = zone.values(0)[:]
    extracted_y = zone.values(1)[:]

    X  = pd.Series(extracted_x)
    Y  = pd.Series(extracted_y)
    Cp = pd.Series(extracted_Cp)

    # normalize x
    xc = (X - X.min()) / (X.max() - X.min())
    extracted_x[:] = xc


    # Append to a single DataFrame
    slice_data = pd.DataFrame({'Slice': i+1, 'xc': xc, 'Cp': Cp})
    all_slices_data = all_slices_data.append(slice_data, ignore_index=True)

# Save the combined data to one CSV file
all_slices_data.to_csv('all_slices_data.csv', index=False)
