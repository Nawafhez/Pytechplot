import tecplot as tp
from tecplot.exception import *
from tecplot.constant import *

# Uncomment the following line to connect to a running instance of Tecplot 360:
# tp.session.connect()

tp.active_frame().plot().contour(0).variable_index=3
tp.active_frame().plot().contour(0).variable_index=1
tp.active_frame().plot().contour(0).colormap_name='Modern'
tp.macro.execute_command('$!RedrawAll')
tp.active_frame().plot().rgb_coloring.red_variable_index=3
tp.active_frame().plot().rgb_coloring.green_variable_index=3
tp.active_frame().plot().rgb_coloring.blue_variable_index=3
tp.active_frame().plot().contour(1).variable_index=3
tp.active_frame().plot().contour(2).variable_index=4
tp.active_frame().plot().contour(3).variable_index=5
tp.active_frame().plot().contour(4).variable_index=6
tp.active_frame().plot().contour(5).variable_index=7
tp.active_frame().plot().contour(6).variable_index=8
tp.active_frame().plot().contour(7).variable_index=9
tp.active_frame().plot().show_contour=True
tp.macro.execute_command('$!RedrawAll')
tp.active_frame().plot().show_contour=False
tp.active_frame().plot().slice(0).edge.show=True
tp.active_frame().plot().slice(0).slice_source=SliceSource.SurfaceZones
tp.active_frame().plot(PlotType.Cartesian3D).show_slices=True
tp.active_frame().plot().slice(0).orientation=SliceSurface.YPlanes
tp.active_frame().plot().slice(0).origin.y=0.0425727
tp.active_frame().plot().slice(1).show=True
tp.active_frame().plot().slice(1).show_primary_slice=False
tp.active_frame().plot().slice(1).show_primary_slice=True
tp.active_frame().plot().slice(1).origin.y=0.316254
tp.active_frame().plot().slice(1).edge.show=True
tp.active_frame().plot().slice(1).slice_source=SliceSource.SurfaceZones
tp.active_frame().plot().slice(2).orientation=SliceSurface.YPlanes
tp.active_frame().plot().slice(2).origin.y=0.604532
tp.active_frame().plot().slice(2).edge.show=True
tp.active_frame().plot().slice(2).slice_source=SliceSource.SurfaceZones
tp.active_frame().plot().slice(2).show=True
tp.active_frame().plot().slice(3).show=True
tp.active_frame().plot().slice(3).orientation=SliceSurface.YPlanes
tp.active_frame().plot().slice(3).origin.y=0.935383
tp.active_frame().plot().slice(3).edge.show=True
tp.active_frame().plot().slice(3).slice_source=SliceSource.SurfaceZones
tp.active_frame().plot().slice(4).edge.show=True
tp.active_frame().plot().slice(4).slice_source=SliceSource.SurfaceZones
tp.active_frame().plot().slice(4).origin.y=1.17379
tp.active_frame().plot().slice(4).show=True
tp.active_frame().plot().slice(0).edge.show=False
tp.active_frame().plot().slice(0).mesh.show=True
tp.active_frame().plot().slice(0).mesh.color=tp.active_frame().plot().contour(0)
tp.active_frame().plot().slice(1).mesh.show=True
tp.active_frame().plot().slice(1).mesh.color=tp.active_frame().plot().contour(0)
tp.active_frame().plot().slice(2).mesh.show=True
tp.active_frame().plot().slice(2).mesh.color=tp.active_frame().plot().contour(0)
tp.active_frame().plot().slice(1).edge.show=False
tp.active_frame().plot().slice(2).edge.show=False
tp.active_frame().plot().slice(3).mesh.show=True
tp.active_frame().plot().slice(3).mesh.color=tp.active_frame().plot().contour(0)
tp.active_frame().plot().slice(3).edge.show=False
tp.active_frame().plot().slice(4).mesh.show=True
tp.active_frame().plot().slice(4).edge.show=False
tp.active_frame().plot().slice(4).edge.show=True
tp.active_frame().plot().slice(4).edge.show=False
tp.active_frame().plot().slice(4).mesh.color=tp.active_frame().plot().contour(0)
tp.macro.execute_command('$!RedrawAll')
tp.active_frame().plot().slice(0).mesh.line_thickness=0.8
tp.active_frame().plot().slice(1).mesh.line_thickness=0.8
tp.active_frame().plot().slice(2).mesh.line_thickness=0.8
tp.active_frame().plot().slice(3).mesh.line_thickness=0.8
tp.active_frame().plot().slice(4).mesh.line_thickness=0.8
tp.active_frame().plot().slices(0,1,2,3,4).extract(transient_mode=TransientOperationMode.AllSolutionTimes)
tp.macro.execute_command('$!RedrawAll')
tp.macro.execute_command('''$!Pick AddAtPosition
  X = 1.0106685633
  Y = 0.580014224751
  ConsiderStyle = Yes''')
tp.macro.execute_command('''$!FrameControl ActivateByNumber
  Frame = 1''')
tp.macro.execute_command('$!Pick Copy')
tp.macro.execute_command('$!Pick Paste')
tp.active_frame().plot().linking_between_frames.link_slice_positions=True
tp.macro.execute_extended_command(command_processor_id='Multi Frame Manager',
    command='TILEFRAMESHORIZ')
tp.macro.execute_command('$!RedrawAll')
tp.macro.execute_command('''$!Pick AddAtPosition
  X = 0.248221906117
  Y = 5.22297297297
  ConsiderStyle = Yes''')
tp.macro.execute_command('''$!FrameControl ActivateByNumber
  Frame = 2''')
tp.active_frame().plot().show_shade=False
tp.active_frame().plot().slice(1).show=False
tp.active_frame().plot().slice(2).show=False
tp.active_frame().plot().slice(3).show=False
tp.active_frame().plot().slice(4).show=False
tp.macro.execute_command('$!RedrawAll')
tp.active_frame().plot().view.position=(6.96919,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    4.30244,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    4.26577)
tp.active_frame().plot().view.width=1.62394
tp.active_frame().plot().view.position=(6.90955,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    4.21353,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    4.43224)
tp.active_frame().plot().view.width=1.62394
tp.active_frame().plot().axes.z_axis.variable_index=12
tp.active_frame().plot().view.position=(0.155406,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -14.9367,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    0.340061)
tp.active_frame().plot().view.psi=90
tp.active_frame().plot().view.theta=0
tp.active_frame().plot().view.position=(0.985677,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    16.1531,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.theta=-180
tp.active_frame().plot().view.position=(0.155406,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    -0.417258)
tp.active_frame().plot().view.alpha=-180
tp.macro.execute_command('$!RedrawAll')
tp.active_frame().plot().view.position=(0.214342,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    16.1531,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    -0.152047)
tp.active_frame().plot().view.width=4.56399
tp.active_frame().plot().axes.x_axis.show=True
tp.active_frame().plot().axes.z_axis.show=True
tp.active_frame().plot().axes.axis_mode=AxisMode.Independent
tp.macro.execute_command('$!RedrawAll')
tp.active_frame().plot().axes.x_axis.scale_factor=1.1
tp.active_frame().plot().axes.x_axis.scale_factor=1.21
tp.active_frame().plot().axes.x_axis.scale_factor=1.331
tp.active_frame().plot().axes.x_axis.scale_factor=1.4641
tp.active_frame().plot().axes.x_axis.scale_factor=1.61051
tp.active_frame().plot().axes.x_axis.scale_factor=1.77156
tp.active_frame().plot().axes.x_axis.scale_factor=1.94872
tp.active_frame().plot().axes.x_axis.scale_factor=2.14359
tp.active_frame().plot().axes.x_axis.scale_factor=2.35795
tp.active_frame().plot().axes.x_axis.scale_factor=2.59374
tp.active_frame().plot().axes.x_axis.scale_factor=2.85312
tp.active_frame().plot().axes.x_axis.scale_factor=3.13843
tp.macro.execute_command('$!RedrawAll')
tp.active_frame().plot().view.position=(0.457045,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    16.1531,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    -0.152047)
tp.active_frame().plot().view.width=6.23291
tp.active_frame().plot().view.position=(0.457045,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    16.1531,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    -0.152047)
tp.active_frame().plot().view.width=9.21285
tp.macro.execute_command('''$!Pick SetMouseMode
  MouseMode = Select''')
tp.macro.execute_command('''$!Pick AddAtPosition
  X = 9.94381223329
  Y = 5.26849217639
  ConsiderStyle = Yes''')
tp.macro.execute_command('''$!Pick SetMouseMode
  MouseMode = Select''')
tp.macro.execute_command('''$!Pick AddAtPosition
  X = 10.0348506401
  Y = 5.21159317212
  ConsiderStyle = Yes''')
tp.macro.execute_command('''$!Pick SetMouseMode
  MouseMode = Select''')
tp.macro.execute_command('''$!Pick AddAtPosition
  X = 10.0120910384
  Y = 5.18883357041
  ConsiderStyle = Yes''')
tp.macro.execute_command('''$!Pick AddAtPosition
  X = 10.0120910384
  Y = 5.15469416785
  CollectingObjectsMode = HomogeneousAdd
  ConsiderStyle = Yes''')
tp.macro.execute_command('$!Pick Clear')
tp.macro.execute_command('''$!Pick AddAtPosition
  X = 9.3293029872
  Y = 4.90433854908
  ConsiderStyle = Yes''')
tp.macro.execute_command('''$!Pick AddAtPosition
  X = 9.3293029872
  Y = 4.93847795164
  CollectingObjectsMode = HomogeneousAdd
  ConsiderStyle = Yes''')
tp.macro.execute_command('$!Pick Clear')
tp.active_frame().plot().axes.x_axis.scale_factor=3.45227
tp.active_frame().plot().axes.x_axis.scale_factor=3.7975
tp.active_frame().plot().axes.x_axis.scale_factor=4.17725
tp.active_frame().plot().axes.x_axis.scale_factor=4.59497
tp.macro.execute_command('$!RedrawAll')
tp.active_frame().plot().axes.x_axis.scale_factor=4.17725
tp.active_frame().plot().axes.x_axis.scale_factor=3.7975
tp.active_frame().plot().axes.x_axis.scale_factor=4.17725
tp.active_frame().plot().axes.x_axis.title.offset=3
tp.macro.execute_command('$!RedrawAll')
tp.active_frame().plot().view.position=(0.497137,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    16.1531,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    -0.0231647)
tp.active_frame().plot().view.width=9.21285
tp.macro.execute_command('''$!Pick AddAtPosition
  X = 0.407539118065
  Y = 4.31258890469
  ConsiderStyle = Yes''')
tp.macro.execute_command('''$!FrameControl ActivateByNumber
  Frame = 2''')
tp.macro.execute_command('$!Pick Copy')
tp.macro.execute_command('$!Pick Paste')
tp.macro.execute_command('$!Pick Paste')
tp.macro.execute_command('$!Pick Paste')
tp.macro.execute_command('$!Pick Paste')
tp.macro.execute_extended_command(command_processor_id='Multi Frame Manager',
    command='TILEFRAMESHORIZ')
tp.macro.execute_command('$!RedrawAll')
tp.macro.execute_command('''$!FrameControl ActivateAtPosition
  X = 2.72901849218
  Y = 4.03947368421''')
tp.macro.execute_command('''$!Pick AddAtPosition
  X = 2.75177809388
  Y = 4.05085348506
  ConsiderStyle = Yes''')
tp.active_frame().plot().slice(0).show=False
tp.active_frame().plot().slice(1).show=True
tp.macro.execute_command('$!RedrawAll')
tp.macro.execute_command('''$!FrameControl ActivateAtPosition
  X = 6.78022759602
  Y = 3.72083926031''')
tp.macro.execute_command('''$!Pick AddAtPosition
  X = 6.78022759602
  Y = 3.72083926031
  ConsiderStyle = Yes''')
tp.active_frame().plot().slice(0).show=False
tp.active_frame().plot().slice(2).show=True
tp.macro.execute_command('''$!FrameControl ActivateAtPosition
  X = 3.75320056899
  Y = 6.05369843528''')
tp.macro.execute_command('''$!Pick AddAtPosition
  X = 3.74182076814
  Y = 6.08783783784
  ConsiderStyle = Yes''')
tp.active_frame().plot().slice(0).show=False
tp.active_frame().plot().slice(3).show=True
tp.macro.execute_command('''$!FrameControl ActivateAtPosition
  X = 6.35917496444
  Y = 5.93990042674''')
tp.macro.execute_command('''$!Pick AddAtPosition
  X = 6.34779516358
  Y = 5.9512802276
  ConsiderStyle = Yes''')
tp.active_frame().plot().slice(0).show=False
tp.active_frame().plot().slice(4).show=True
tp.macro.execute_command('$!RedrawAll')
# End Macro.

