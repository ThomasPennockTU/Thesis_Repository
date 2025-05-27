# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2023 replay file
# Internal Version: 2023_03_20-20.15.03 RELr425 183417
# Run by tpennock on Tue May 27 09:40:44 2025
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=532.666687011719, 
    height=243.115371704102)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
openMdb('First delta flume.cae')
#: The model database "D:\tpennock\GitHub\Thesis_Repository\1.0-First delta flume no forces\First delta flume.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['Block']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
o3 = session.openOdb(
    name='D:/tpennock/GitHub/Thesis_Repository/1.0-First delta flume no forces/Job-2.odb')
#: Model: D:/tpennock/GitHub/Thesis_Repository/1.0-First delta flume no forces/Job-2.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     212
#: Number of Meshes:             213
#: Number of Element Sets:       0
#: Number of Node Sets:          5
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].view.setValues(nearPlane=47.9542, 
    farPlane=83.7407, width=49.9994, height=17.3685, cameraPosition=(67.9563, 
    40.3746, 0.19144), cameraUpVector=(-0.815294, 0.57735, -0.0442925), 
    cameraTarget=(14.5812, 2.57702, -2.70827))
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50.2027, 
    farPlane=81.4923, width=22.0937, height=7.67481, viewOffsetX=-0.29656, 
    viewOffsetY=-1.81354)
session.viewports['Viewport: 1'].odbDisplay.setDeformedVariable(
    variableLabel='RF', )
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].view.setValues(nearPlane=273563, 
    farPlane=542888, width=5.69347, height=1.97777, viewOffsetX=0.0235868, 
    viewOffsetY=-2.35657)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].view.setValues(nearPlane=308885, 
    farPlane=541616, width=7.09539, height=2.46476, viewOffsetX=0.578684, 
    viewOffsetY=-2.47127)
leaf = dgo.LeafFromPartInstance(partInstanceName=(
    "BLOCK-2-LIN-1-8-LIN-2-1-LIN-LIN-11-1-2", ))
session.viewports['Viewport: 1'].odbDisplay.displayGroup.replace(leaf=leaf)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].view.setValues(nearPlane=427795, 
    farPlane=427800, width=2.42052, height=0.840826, viewOffsetX=1.18263, 
    viewOffsetY=-4.01346)
odb = session.odbs['D:/tpennock/GitHub/Thesis_Repository/1.0-First delta flume no forces/Job-2.odb']
xyList = xyPlot.xyDataListFromField(odb=odb, outputPosition=INTEGRATION_POINT, 
    variable=(('S', INTEGRATION_POINT, ((COMPONENT, 'S22'), )), ), 
    elementPick=(('BLOCK-2-LIN-1-8-LIN-2-1-LIN-LIN-11-1-2', 1, ('[#1 ]', )), ), 
    )
xyp = session.XYPlot('XYPlot-1')
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
curveList = session.curveSet(xyData=xyList)
chart.setValues(curvesToPlot=curveList)
session.charts[chartName].autoColor(lines=True, symbols=True)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
odb = session.odbs['D:/tpennock/GitHub/Thesis_Repository/1.0-First delta flume no forces/Job-2.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
odb = session.odbs['D:/tpennock/GitHub/Thesis_Repository/1.0-First delta flume no forces/Job-2.odb']
xyList = xyPlot.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=((
    'S', INTEGRATION_POINT, ((COMPONENT, 'S22'), )), ), nodePick=((
    'BLOCK-2-LIN-1-8-LIN-2-1-LIN-LIN-11-1-2', 1, ('[#0 #1 ]', )), ), )
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
curveList = session.curveSet(xyData=xyList)
chart.setValues(curvesToPlot=curveList)
session.charts[chartName].autoColor(lines=True, symbols=True)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
odb = session.odbs['D:/tpennock/GitHub/Thesis_Repository/1.0-First delta flume no forces/Job-2.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
odb = session.odbs['D:/tpennock/GitHub/Thesis_Repository/1.0-First delta flume no forces/Job-2.odb']
xyList = xyPlot.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=((
    'RF', NODAL, ((COMPONENT, 'RF1'), (COMPONENT, 'RF2'), (COMPONENT, 'RF3'), 
    )), ), nodePick=(('BLOCK-2-LIN-1-8-LIN-2-1-LIN-LIN-11-1-2', 1, ('[#0 #1 ]', 
    )), ), )
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
curveList = session.curveSet(xyData=xyList)
chart.setValues(curvesToPlot=curveList)
session.charts[chartName].autoColor(lines=True, symbols=True)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
odb = session.odbs['D:/tpennock/GitHub/Thesis_Repository/1.0-First delta flume no forces/Job-2.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
odb = session.odbs['D:/tpennock/GitHub/Thesis_Repository/1.0-First delta flume no forces/Job-2.odb']
xyList = xyPlot.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=((
    'CPRESS     General_Contact_Domain', NODAL), ), nodePick=((
    'BLOCK-2-LIN-1-8-LIN-2-1-LIN-LIN-11-1-2', 1, ('[#0 #1 ]', )), ), )
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
curveList = session.curveSet(xyData=xyList)
chart.setValues(curvesToPlot=curveList)
session.charts[chartName].autoColor(lines=True, symbols=True)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Loading')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(variables=(
    'S', 'SVAVG', 'PE', 'PEVAVG', 'PEEQ', 'PEEQVAVG', 'LE', 'U', 'V', 'A', 
    'RF', 'RT', 'CF', 'SF', 'BF', 'P', 'CSTRESS', 'EVF'))
xyp = session.xyPlots['XYPlot-1']
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
#: The job input file "Job-1.inp" has been submitted for analysis.
#: Job Job-1: Analysis Input File Processor completed successfully.
session.viewports['Viewport: 1'].view.setValues(nearPlane=56.2464, 
    farPlane=97.1888, width=52.2962, height=19.1083, cameraPosition=(76.7346, 
    47.1273, 3.98809), cameraUpVector=(-0.812152, 0.57735, -0.0841152), 
    cameraTarget=(14.8429, 3.12913, -2.42208))
#: Job Job-1: Abaqus/Explicit Packager completed successfully.
session.viewports['Viewport: 1'].view.setValues(nearPlane=58.8035, 
    farPlane=94.6316, width=20.9637, height=7.65987, viewOffsetX=3.80513, 
    viewOffsetY=-2.87164)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.2757, 
    farPlane=94.1594, width=14.2755, height=4.95894, viewOffsetX=4.97779, 
    viewOffsetY=-1.37253)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
mdb.save()
#: The model database has been saved to "D:\tpennock\GitHub\Thesis_Repository\1.0-First delta flume no forces\First delta flume.cae".
