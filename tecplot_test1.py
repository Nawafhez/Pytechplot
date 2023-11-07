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
cont.legend.show = False

#Setup the Slices
plot.show_slices=True
slices = plot.slices(0)
slices.slice_source = SliceSource.SurfaceZones
slices.orientation = SliceSource.YPlanes
slices.show_primary_slice=False
slices.show_start_and_end_slices=True
slices.show_intermediate_slices=True
slices.num_intermediate_slices=5
slices.start_position.y=0
slices.start_position.y=1.19

#Adjust slices settings 
slices.contour.show = False
slices.mesh.show = True
slices.mesh.color = cont
slices.mesh.line_thickness = 0.6
slices.edge.show = False

slices.extract(transient_mode=TransientOperationMode.AllSolutionTimes)


frame.add_frame(position=(0.69203,5.1888), size=(6.3385,2.606))

tp.macro.execute_extended_command(command_processor_id='Multi Frame Manager',
    command='TILEFRAMESHORIZ')

frame.plot_type = tecplot.constant.PlotType.XYLine

plot.delete_linemaps()


for i in range(7): 
  

  plot.linemaps(i).name='&ZN&'
  plot.linemaps(i).y_variable_index=12
  plot.linemaps(i).zone_index=i+1
  plot.linemaps(i).show=True
  


tp.active_frame().plot().view.fit()

tp.active_frame().plot().axes.y_axis(0).reverse=True
tp.macro.execute_command('$!RedrawAll')
# End Macro.