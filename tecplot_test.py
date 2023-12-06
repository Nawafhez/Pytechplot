import tecplot as tp
from tecplot.constant import *
import pandas as pd
import sys
import os
import logging
import matplotlib.pyplot as plt

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

import sys
if '-c' in sys.argv:
    tp.session.connect()

tp.new_layout()

# trying to define the path
path = os.getcwd()
datafile = os.path.join(path,'work', 'data_oneram6wing', 'OneraM6_SU2_RANS.plt')
dataset = tp.data.load_tecplot(datafile)

# Get the active frame and its plot
page = tp.active_page()
page.name = 'Slices'
frame = page.active_frame()
frame.plot_type = tp.constant.PlotType.Cartesian3D
plot = frame.plot()

Pressure_Coefficient = dataset.zone(1).values(11)[:]
x = dataset.zone(1).values(0)[:]
y = dataset.zone(1).values(1)[:]

Y = pd.Series(y)
Ymin = Y.min() + 0.01
Ymax = Y.max() - 0.03
yc = (Y - Y.min()) / (Y.max() - Y.min())

# Set contour variables & colormap
plot.contour(1).variable_index = 1
plot.contour(1).colormap_name = 'Small Rainbow'

# Show contour and slices
plot.show_contour = False
plot.show_slices = True

# Set slices properties
y_positions = [Ymin, Ymax / 4, Ymax / 2, 3 * Ymax / 4, Ymax]
slices_num = 0

for i, y1 in enumerate(y_positions):
    slice_ = plot.slice(i)
    slice_.show = True
    slice_.slice_source = tp.constant.SliceSource.SurfaceZones
    slice_.orientation = tp.constant.SliceSurface.YPlanes
    slice_.origin.y = y1
    slice_.edge.show = False
    slice_.mesh.show = True
    slice_.mesh.color = plot.contour(1)
    slice_.mesh.line_thickness = 0.8
    slices_num = slices_num + 1

# Extract slices
extracted_slices = plot.slices(0, 1, 2, 3, 4).extract(transient_mode=tp.constant.TransientOperationMode.AllSolutionTimes)

all_slices_data = pd.DataFrame()

# Matplotlib plot
for i, extracted_slice in enumerate(extracted_slices):

    zone = dataset.zone(i+2)

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
