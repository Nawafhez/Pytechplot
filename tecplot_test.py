import tecplot as tp
from tecplot.exception import *
from tecplot.constant import *

# Uncomment the following line to connect to a running instance of Tecplot 360:
tp.session.connect()

tp.macro.execute_command("""$!ReadDataSet  '\"STANDARDSYNTAX\" \"1.0\" \"FILENAME_FILE\" \"/storage/home/dba5321/RoarCollab/data/surface_flow.vtu\"'
  DataSetReader = 'VTK Data Loader'
  ReadDataOption = New
  ResetStyle = No
  AssignStrandIDs = Yes
  InitialPlotType = Automatic
  InitialPlotFirstZoneOnly = No
  AddZonesToExistingStrands = No
  VarLoadMode = ByName""")
tp.active_frame().plot_type=PlotType.Cartesian3D
tp.macro.execute_command('$!RedrawAll')
tp.active_frame().plot().rgb_coloring.red_variable_index=3
tp.active_frame().plot().rgb_coloring.green_variable_index=3
tp.active_frame().plot().rgb_coloring.blue_variable_index=3
tp.active_frame().plot().slice(0).edge.show=True
tp.active_frame().plot().slice(0).slice_source=SliceSource.SurfaceZones
tp.active_frame().plot().contour(0).variable_index=3
tp.active_frame().plot().contour(1).variable_index=4
tp.active_frame().plot().contour(2).variable_index=5
tp.active_frame().plot().contour(3).variable_index=6
tp.active_frame().plot().contour(4).variable_index=7
tp.active_frame().plot().contour(5).variable_index=8
tp.active_frame().plot().contour(6).variable_index=9
tp.active_frame().plot().contour(7).variable_index=10
tp.active_frame().plot(PlotType.Cartesian3D).show_slices=True
tp.active_frame().plot().slice(0).show_primary_slice=False
tp.active_frame().plot().slice(0).show_start_and_end_slices=True
tp.active_frame().plot().slice(0).start_position.x=0
tp.active_frame().plot().slice(0).show_intermediate_slices=True
tp.active_frame().plot().slice(0).num_intermediate_slices=5
tp.active_frame().plot().slice(0).orientation=SliceSurface.YPlanes
tp.active_frame().plot().slice(0).start_position.y=0
tp.active_frame().plot().slices(0).extract(transient_mode=TransientOperationMode.AllSolutionTimes)
tp.macro.execute_command('$!RedrawAll')
tp.active_page().add_frame(position=(0.69203,5.1888),
    size=(6.3385,2.606))
tp.macro.execute_extended_command(command_processor_id='Multi Frame Manager',
    command='TILEFRAMESHORIZ')
tp.macro.execute_command('$!RedrawAll')
tp.macro.execute_command('''$!Pick SetMouseMode
  MouseMode = Select''')

tp.active_frame().plot_type=PlotType.XYLine
tp.active_frame().plot().delete_linemaps()
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(0).name='&ZN&'
tp.active_frame().plot().linemaps(0).y_variable_index=12
tp.active_frame().plot().linemaps(0).zone_index=1
tp.active_frame().plot().linemaps(0).show=True
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(1).name='&ZN&'
tp.active_frame().plot().linemaps(1).y_variable_index=12
tp.active_frame().plot().linemaps(1).zone_index=2
tp.active_frame().plot().linemaps(1).show=True
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(2).name='&ZN&'
tp.active_frame().plot().linemaps(2).y_variable_index=12
tp.active_frame().plot().linemaps(2).zone_index=3
tp.active_frame().plot().linemaps(2).show=True
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(3).name='&ZN&'
tp.active_frame().plot().linemaps(3).y_variable_index=12
tp.active_frame().plot().linemaps(3).zone_index=4
tp.active_frame().plot().linemaps(3).show=True
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(4).name='&ZN&'
tp.active_frame().plot().linemaps(4).y_variable_index=12
tp.active_frame().plot().linemaps(4).zone_index=5
tp.active_frame().plot().linemaps(4).show=True
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(5).name='&ZN&'
tp.active_frame().plot().linemaps(5).y_variable_index=12
tp.active_frame().plot().linemaps(5).zone_index=6
tp.active_frame().plot().linemaps(5).show=True
tp.active_frame().plot().add_linemap()
tp.active_frame().plot().linemaps(6).name='&ZN&'
tp.active_frame().plot().linemaps(6).y_variable_index=12
tp.active_frame().plot().linemaps(6).zone_index=7
tp.active_frame().plot().linemaps(6).show=True
tp.active_frame().plot().view.fit()

tp.active_frame().plot().axes.y_axis(0).reverse=True
tp.macro.execute_command('$!RedrawAll')
# End Macro.

