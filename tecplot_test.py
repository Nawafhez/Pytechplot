import tecplot as tp
from tecplot.constant import*
import pandas as pd
import sys
import os

import logging

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

import sys
if '-c' in sys.argv:
    tp.session.connect()

#import argparse
#Argparse

tp.new_layout()

#trying to define the path
path = os.getcwd()
datafile = os.path.join(path,'work','surface_flow.vtu')
dataset= tp.data.load_tecplot(datafile)

# Get the active frame and its plot
page = tp.active_page()
page.name = 'Density Contour'
frame = page.active_frame()
frame.plot_type = tp.constant.PlotType.Cartesian3D
plot = frame.plot()

Pressure_Coefficient = dataset.zone(1).values(11)[:]
x = dataset.zone(1).values(0)[:]
y = dataset.zone(1).values(1)[:]

Y = pd.Series(y)
Ymin = Y.min()+0.01
Ymax = Y.max()-0.03
yc= (Y-Y.min())/(Y.max()-Y.min())

# Set contour variables & colormap
plot.contour(0).variable_index = 3
plot.contour(0).colormap_name = 'Modern'

# Set contour variables & colormap
plot.contour(1).variable_index = 1
plot.contour(1).colormap_name = 'Small Rainbow'

# Show contour and slices
plot.show_contour = True
plot.show_slices = False

# Set slices properties
y_positions = [Ymin, Ymax/4, Ymax/2, 3*Ymax/4, Ymax]
slices_num=0

for i, y1 in enumerate(y_positions):
    slice_ = plot.slice(i)
    slice_.show = False
    slice_.slice_source = tp.constant.SliceSource.SurfaceZones
    slice_.orientation = tp.constant.SliceSurface.YPlanes
    slice_.origin.y = y1
    slice_.edge.show = False
    slice_.mesh.show = False
    slice_.mesh.color = plot.contour(1)
    slice_.mesh.line_thickness = 0.8
    slices_num=slices_num+1

# Extract slices
extracted_slices = plot.slices(0, 1, 2, 3, 4).extract(transient_mode=tp.constant.TransientOperationMode.AllSolutionTimes)


# Define the variable indices for Cp and x
cp_var_index = 11
x_var_index = 0

page2 = tp.add_page()
page2.name = 'Cp vs x'
frame2 = page2.active_frame()
assert not (frame.active and page.active)
assert frame2.active and page2.active

for i in range(slices_num):

    page2.add_frame

    # copy of data as a numpy array
    zone = dataset.zone(i+2)
    extracted_Cp = zone.values(11)[:]
    extracted_x = zone.values(0)[:]

    X = pd.Series(extracted_x)
    Cp = pd.Series(extracted_x)

    # normalize x
    xc = (X - X.min()) / (X.max() - X.min())
    extracted_x[:] = xc

    # switch plot type in current frame
    frame2.plot_type = tp.constant.PlotType.XYLine
    plot1 = frame2.plot()

    # clear plot
    plot1.delete_linemaps()

    # create line plot from extracted zone data
    cp_linemap = plot1.add_linemap('Slice', zone, dataset.variable('x'),
                            dataset.variable('Pressure_Coefficient'))

    # set style of linemap plot
    cp_linemap.line.line_thickness = 0.8
    cp_linemap.y_axis.reverse = True

    # update axes limits to show data
    plot1.view.fit()

    # export image of pressure coefficient as a function of x/c
    tp.export.save_png('wing_pressure_coefficient_Slice:'f'{i}''.png', 600, supersample=3)



tp.macro.execute_extended_command(command_processor_id='Multi Frame Manager',
    command='TILEFRAMESSQUARE')
