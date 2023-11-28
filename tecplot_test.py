import tecplot as tp
import pandas as pd
import os 
import argparse

#Argparse

# Connect to a running instance of Tecplot 360 if needed
tp.session.connect()


#trying to define the path
path = os.getcwd()
print(path)

datafile = os.path.join(path,'work','data_oneram6wing', 'OneraM6_SU2_RANS.plt')
dataset= tp.data.load_tecplot(datafile)
print(dataset)


# Get the active frame and its plot
frame = tp.active_frame()
frame.plot_type = tp.constant.PlotType.Cartesian3D
plot = frame.plot()

Pressure_Coefficient = dataset.zone(1).values(11)[:]
x = dataset.zone(1).values(0)[:]
y = dataset.zone(1).values(1)[:]

Cp= pd.Series(Pressure_Coefficient)
X = pd.Series(x)
Y = pd.Series(y)
Ymax = Y.max()-0.03
print(Ymax)


# Set contour variables & colormap
plot.contour(0).variable_index = 1
plot.contour(0).colormap_name = 'Modern'

# Show contour and slices
plot.show_contour = False
plot.show_slices = True

# Set slices properties
y_positions = [0, Ymax/4, Ymax/2, 3*Ymax/4, Ymax]

for i, y1 in enumerate(y_positions):
    slice_ = plot.slice(i)
    slice_.show = True
    slice_.slice_source = tp.constant.SliceSource.SurfaceZones
    slice_.orientation = tp.constant.SliceSurface.YPlanes
    slice_.origin.y = y1
    slice_.edge.show = False
    slice_.mesh.show = True
    slice_.mesh.color = plot.contour(0)
    slice_.mesh.line_thickness = 0.8

# Extract slices
extracted_slices = plot.slices(0, 1, 2, 3, 4).extract(transient_mode=tp.constant.TransientOperationMode.AllSolutionTimes)

# Update the view of the plot
plot.view.position = (6.96919, plot.view.position[1], plot.view.position[2])
plot.view.width = 1.62394

# Redraw the plot
tp.macro.execute_command('$!RedrawAll')

# Additional settings for the x and z axes
plot.axes.x_axis.show = True
plot.axes.z_axis.show = True
plot.axes.axis_mode = tp.constant.AxisMode.Independent

# Define the variable indices for Cp and x
cp_var_index = 11  
x_var_index = 0   



# Loop to create a new frame and plot for each Cp graph

for i in range(5):

    # Create a new frame
    frame = tp.active_page().add_frame()
    
    # Set the frame mode to 2D
    frame.plot_type = tp.constant.PlotType.XYLine
    
    # Get the plot in the new frame
    plot = frame.plot()
    
    # Set up the axes for the plot
    plot.axes.x_axis.variable.set_variable()
    plot.axes.x_axis.variable.set_variable(cp)
    
    # Create an XY line from the slice zone data
    slice_zone = extracted_slices.zone(i)
    x_vals = slice_zone.values('x')[:]
    cp_vals = slice_zone.values('Pressure_Coefficient')[:]

    # Add a new XY line plot with the extracted Cp vs. x data
    line = plot.add_xy_line(x_vals,cp_vals)
    
    # Set the line properties, such as color and line thickness
    line.line.color = tp.constant.Color.Blue
    line.line.line_thickness = 0.8
    
    # Optionally, set the title of the graph to something descriptive
    plot.title = f" y{i}"
    
    # Redraw the frame
    frame.draw()

tp.active_page().frames[0].activate()

# Final redraw of the plot
plot.view.fit()
tp.macro.execute_command('$!RedrawAll')

# End of script
