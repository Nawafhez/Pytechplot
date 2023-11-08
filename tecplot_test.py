import tecplot as tp
from tecplot.constant import SliceSource, SliceSurface, PlotType, AxisMode, TransientOperationMode

tp.macro.execute_command("""$!ReadDataSet  '\"/storage/home/nka5267/work/OneraM6_SU2_RANS.plt\" '
  ReadDataOption = New
  ResetStyle = No
  VarLoadMode = ByName
  AssignStrandIDs = Yes
  VarNameList = '\"x\" \"y\" \"z\" \"Density\" \"Momentum U (Density*U)\" \"Momentum V (Density*V)\" \"Momentum W (Density*W)\" \"Energy (Density*E)\" \"SA Turbulent Eddy Viscosity\" \"Pressure\" \"Temperature\" \"Pressure_Coefficient\" \"Mach\" \"Laminar_Viscosity\" \"Skin_Friction_Coefficient\" \"Heat_Flux\" \"Y_Plus\" \"Eddy_Viscosity\"'""")


# Connect to a running instance of Tecplot 360 if needed
# tp.session.connect()

# Get the active frame and its plot
frame = tp.active_frame()
plot = frame.plot()

# Set contour variables & colormap
plot.contour(0).variable_index = 1
plot.contour(0).colormap_name = 'Modern'

# Show contour and slices
plot.show_contour = True
plot.show_slices = True

# Set slices properties
y_positions = [0.0425727, 0.316254, 0.604532, 0.935383, 1.17379]
for i, y in enumerate(y_positions):
    slice_ = plot.slice(i)
    slice_.slice_source = SliceSource.SurfaceZones
    slice_.orientation = SliceSurface.YPlanes
    slice_.origin.y = y
    slice_.edge.show = True
    slice_.mesh.show = True
    slice_.mesh.color = plot.contour(0)
    slice_.mesh.line_thickness = 0.8
    slice_.edge.show = False


# Extract slices
plot.slices(0,1,2,3,4).extract(transient_mode=TransientOperationMode.AllSolutionTimes)

# Update the view of the plot
plot.view.position = (6.96919, plot.view.position[1], plot.view.position[2])
plot.view.width = 1.62394

# Update axes scales
x_axis_scale_factors = [1.1, 1.21, 1.331, 1.4641, 1.61051, 1.77156, 1.94872, 2.14359, 2.35795, 2.59374]
for scale in x_axis_scale_factors:
    plot.axes.x_axis.scale_factor = scale

# Redraw the plot
tp.macro.execute_command('$!RedrawAll')

# Additional settings for the x and z axes
plot.axes.x_axis.show = True
plot.axes.z_axis.show = True
plot.axes.axis_mode = AxisMode.Independent

# Define the variable indices for Cp and x
cp_var_index = 11  # replace with the actual index for Cp
x_var_index = 0   # replace with the actual index for x

# Get the dataset
dataset = tp.active_frame().dataset

# Loop to create a new frame and plot for each Cp graph
for i in range(number_of_graphs):  # Replace with the actual number of Cp graphs
    # Create a new frame
    frame = tp.active_frame().add_frame()
    
    # Set the frame mode to 2D
    frame.plot_type = PlotType.XYLine
    
    # Get the plot in the new frame
    plot = frame.plot()
    
    # Set up the axes for the plot
    plot.axes.x_axis.variable = dataset.variable(x_var_index)
    plot.axes.y_axis.variable = dataset.variable(cp_var_index)
    
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
    plot.title = f"Cp vs. x Graph {i+1}"
    
    # Redraw the frame
    frame.draw()

# Activate the first frame at the end
tp.active_page().frames[0].activate()


# Final redraw of the plot
tp.macro.execute_command('$!RedrawAll')

# End of script
