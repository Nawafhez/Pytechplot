import tecplot as tp
from tecplot.exception import *
from tecplot.constant import *
import numpy as np 

# Uncomment the following line to connect to a running instance of Tecplot 360:
tp.session.connect()

tp.macro.execute_command("""$!ReadDataSet  '\"/storage/home/nka5267/work/OneraM6_SU2_RANS.plt\" '
  ReadDataOption = New
  ResetStyle = No
  VarLoadMode = ByName
  AssignStrandIDs = Yes
  VarNameList = '\"x\" \"y\" \"z\" \"Density\" \"Momentum U (Density*U)\" \"Momentum V (Density*V)\" \"Momentum W (Density*W)\" \"Energy (Density*E)\" \"SA Turbulent Eddy Viscosity\" \"Pressure\" \"Temperature\" \"Pressure_Coefficient\" \"Mach\" \"Laminar_Viscosity\" \"Skin_Friction_Coefficient\" \"Heat_Flux\" \"Y_Plus\" \"Eddy_Viscosity\"'""")

frame = tp.active_frame()
frame.plot_type = PlotType.Cartesian3D

plot= frame.plot()

#Setup the Contour
cont = plot.contour(0)
cont.variable = frame.dataset.variable('y')
cont.levels.reset_levels(np.linspace(0,1.2,13))
cont.legend.show = True
tp.macro.execute_command('$!RedrawAll')

#Setup the Slices
frame.plot(PlotType.Cartesian3D).show_slices=True
slices = plot.slice(0)

slices.slice_source = SliceSource.SurfaceZones
slices.orientation = SliceSurface.YPlanes

slices.show_primary_slice=False
slices.show_start_and_end_slices=True
slices.show_intermediate_slices=True
slices.num_intermediate_slices=5
slices.start_position.y=0
slices.end_position.y=1.19

#Adjust slices settings & Extracting it  
slices.contour.show = False
slices.mesh.show = True
slices.mesh.color = cont
slices.mesh.line_thickness = 0.6
slices.edge.show = False

extracted_slices = slices.extract(transient_mode=TransientOperationMode.AllSolutionTimes)


#Introducing a new page for Prussure Coeffecient plot
tp.active_page().add_frame(position=(0.69203,5.1888), size=(6.3385,2.606))


#Redefinig the varibles
frame= tp.active_page()
plot= frame.plot()

#Plotting the Cp plots
frame.plot_type = tp.constant.PlotType.XYLine
plot.delete_linemaps()

cp_linemap = plot.add_linemap(
    name=extracted_slice.name=='&Cp&',
    zone=extracted_slices,
    x=dataset.variable('x'),
    y=dataset.variable('Pressure_Coefficient'))


plot.view.fit()
tp.active_frame().plot().axes.y_axis(0).reverse=True

tp.macro.execute_command('$!RedrawAll')

# export image of pressure coefficient as a function of x/c
tecplot.export.save_png('wing_pressure_coefficient.png', 600, supersample=3)

# End Macro.