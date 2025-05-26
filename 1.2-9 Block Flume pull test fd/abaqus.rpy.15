# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2023 replay file
# Internal Version: 2023_03_20-20.15.03 RELr425 183417
# Run by tpennock on Wed May 21 11:39:53 2025
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
#: The model database "D:\tpennock\GitHub\Thesis_Repository\1.2-9 Block Flume pull test\First delta flume.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['Block']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=56.0107, 
    farPlane=97.4169, width=54.7773, height=19.0282, cameraPosition=(76.6743, 
    47.1273, 4.54603), cameraUpVector=(-0.811361, 0.57735, -0.0914366), 
    cameraTarget=(14.8429, 3.12913, -2.42207))
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.6189, 
    farPlane=93.8086, width=10.1369, height=3.52131, viewOffsetX=1.74348, 
    viewOffsetY=-3.08994)
o3 = session.openOdb(
    name='D:/tpennock/GitHub/Thesis_Repository/1.2-9 Block Flume pull test/Job-1.odb')
#: Model: D:/tpennock/GitHub/Thesis_Repository/1.2-9 Block Flume pull test/Job-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     13
#: Number of Meshes:             14
#: Number of Element Sets:       0
#: Number of Node Sets:          4
#: Number of Steps:              2
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['D:/tpennock/GitHub/Thesis_Repository/1.2-9 Block Flume pull test/Job-1.odb'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=48.2567, 
    farPlane=82.428, width=50.3028, height=17.4739, cameraPosition=(52.8834, 
    40.3687, 34.3811), cameraTarget=(15.0925, 2.57775, -3.40984))
session.viewports['Viewport: 1'].view.setValues(nearPlane=48.3149, 
    farPlane=83.9935, width=50.3635, height=17.495, cameraPosition=(68.1639, 
    40.3687, 2.72131), cameraUpVector=(-0.811203, 0.57735, -0.0928284), 
    cameraTarget=(15.066, 2.57775, -3.35487))
session.viewports['Viewport: 1'].view.setValues(nearPlane=51.744, 
    farPlane=80.5645, width=3.97563, height=1.38103, viewOffsetX=-0.256337, 
    viewOffsetY=-2.88028)
odb = session.odbs['D:/tpennock/GitHub/Thesis_Repository/1.2-9 Block Flume pull test/Job-1.odb']
xyList = xyPlot.xyDataListFromField(odb=odb, outputPosition=INTEGRATION_POINT, 
    variable=(('S', INTEGRATION_POINT, ((COMPONENT, 'S22'), )), ), 
    elementPick=(('BLOCK-2-LIN-1-5-LIN-11-1', 1, ('[#0 #2000 ]', )), ), )
xyp = session.XYPlot('XYPlot-1')
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
curveList = session.curveSet(xyData=xyList)
chart.setValues(curvesToPlot=curveList)
session.charts[chartName].autoColor(lines=True, symbols=True)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
xQuantity = visualization.QuantityType(type=TIME)
yQuantity = visualization.QuantityType(type=STRESS)
session.xyDataObjects['_S:S22 PI: BLOCK-2-LIN-1-5-LIN-11-1 E: 46 IP: 1'].setValues(
    data=((0, 0), (0.0500067, -14330.3), (0.100014, -26953.2), (0.150005, 
    -4697.13), (0.200012, -47069), (0.250003, 2083.42), (0.30001, -10284.4), (
    0.350001, 5368.97), (0.400007, -17385.4), (0.450014, 15150.5), (0.500004, 
    -34573.4), (0.550011, -16722.3), (0.600002, 33116.5), (0.650008, -30513.2), 
    (0.700015, 5027.5), (0.750006, -15254.7), (0.800012, -9330.69), (0.850003, 
    -37959.1), (0.900009, 48195.6), (0.95, 45131.2), (1, 8670.94), (1, 
    8670.94), (1.6, -7862.87), (2.20001, -10484), (2.8, -34386.1), (3.4, 
    1845.43), (4, 20805.2), (4.6, -14348.2), (5.2, 9137.75), (5.8, 3978.73), (
    6.4, 2896.49), (7.00002, 2976.29), (7.60001, 2980.13), (8.20001, 2956.89), 
    (8.80001, 4218.34), (9.40001, 5541.61), (10, 8106.03), (10.6, 1778.84), (
    11.2, 15395.2), (11.8, 29755.2), (12.4, 40550.3), ), 
    sourceDescription='Data modified in editor', axis1QuantityType=xQuantity, 
    axis2QuantityType=yQuantity, )
odb = session.odbs['D:/tpennock/GitHub/Thesis_Repository/1.2-9 Block Flume pull test/Job-1.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
odb = session.odbs['D:/tpennock/GitHub/Thesis_Repository/1.2-9 Block Flume pull test/Job-1.odb']
xyList = xyPlot.xyDataListFromField(odb=odb, outputPosition=INTEGRATION_POINT, 
    variable=(('S', INTEGRATION_POINT, ((COMPONENT, 'S22'), )), ), 
    elementPick=(('BLOCK-2-LIN-1-4-LIN-11-1', 1, ('[#0 #4 ]', )), ), )
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
curveList = session.curveSet(xyData=xyList)
chart.setValues(curvesToPlot=curveList)
session.charts[chartName].autoColor(lines=True, symbols=True)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
odb = session.odbs['D:/tpennock/GitHub/Thesis_Repository/1.2-9 Block Flume pull test/Job-1.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=47.28, 
    farPlane=85.0285, width=48.3249, height=16.3151, viewOffsetX=5.33385, 
    viewOffsetY=-0.311109)
session.animationOptions.setValues(frameRate=20)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50.9327, 
    farPlane=81.3758, width=9.28065, height=3.13327, viewOffsetX=0.355861, 
    viewOffsetY=-2.69153)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].view.setValues(nearPlane=20474, 
    farPlane=20917.4, width=7.82446, height=2.64164, cameraPosition=(17053.7, 
    11931.4, 1905.89), viewOffsetX=-38.963, viewOffsetY=152.31)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['Block-2-lin-1-5-lin-11-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#10 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=264.118, 
    farPlane=265.379, width=3.26523, height=1.18362, cameraPosition=(232.765, 
    158.199, 22.1367), viewOffsetX=0.702039, viewOffsetY=-4.01022)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
i1 = a.instances['Block-2-lin-1-5-lin-11-1']
leaf = dgm.LeafFromInstance((i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['D:/tpennock/GitHub/Thesis_Repository/1.2-9 Block Flume pull test/Job-1.odb'])
odb = session.odbs['D:/tpennock/GitHub/Thesis_Repository/1.2-9 Block Flume pull test/Job-1.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
leaf = dgo.LeafFromPartInstance(partInstanceName=("BLOCK-2-LIN-1-5-LIN-11-1", 
    ))
session.viewports['Viewport: 1'].odbDisplay.displayGroup.replace(leaf=leaf)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=20881.5, 
    farPlane=20882.7, width=2.72538, height=0.920125, viewOffsetX=-40.4381, 
    viewOffsetY=155.622)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='CPRESS     General_Contact_Domain', outputPosition=NODAL, )
session.viewports['Viewport: 1'].view.setValues(nearPlane=20881.4, 
    farPlane=20882.7, width=2.72536, height=0.92012, cameraPosition=(17053.7, 
    11189.8, 4556.55), cameraUpVector=(-0.811203, 0.583377, 0.0402646), 
    cameraTarget=(265.314, -13.9237, -19.3303), viewOffsetX=-40.4379, 
    viewOffsetY=155.621)
session.viewports['Viewport: 1'].view.setValues(nearPlane=20881.3, 
    farPlane=20882.6, width=2.72535, height=0.920116, cameraPosition=(14462.2, 
    11189.8, 10114.5), cameraUpVector=(-0.775935, 0.583377, -0.239993), 
    cameraTarget=(256.227, -13.9237, 65.6071), viewOffsetX=-40.4377, 
    viewOffsetY=155.62)
session.viewports['Viewport: 1'].view.setValues(nearPlane=20881.4, 
    farPlane=20882.5, width=1.37917, height=0.465625, viewOffsetX=-40.7467, 
    viewOffsetY=155.663)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=263.899, 
    farPlane=265.323, width=3.26253, height=1.18263, cameraPosition=(153.755, 
    158.199, 164.636), cameraUpVector=(-0.511549, 0.57735, -0.636385), 
    cameraTarget=(16.3588, 3.12913, -6.2897), viewOffsetX=0.701457, 
    viewOffsetY=-4.0069)
odb = session.odbs['D:/tpennock/GitHub/Thesis_Repository/1.2-9 Block Flume pull test/Job-1.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.animationOptions.setValues(frameRate=53)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].view.setValues(nearPlane=20881.3, 
    farPlane=20882.7, width=3.89211, height=1.31403, viewOffsetX=-41.616, 
    viewOffsetY=155.738)
leaf = dgo.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].odbDisplay.displayGroup.replace(leaf=leaf)
leaf = dgo.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].odbDisplay.displayGroup.replace(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=20870.1, 
    farPlane=20902, width=22.1848, height=7.48989, viewOffsetX=-39.5817, 
    viewOffsetY=156.727)
session.viewports['Viewport: 1'].view.setValues(nearPlane=20871.5, 
    farPlane=20904.2, width=22.1863, height=7.49041, cameraPosition=(17638.9, 
    11189.8, 731.91), cameraUpVector=(-0.78292, 0.583377, 0.216122), 
    cameraTarget=(256.76, -13.9237, -74.4055), viewOffsetX=-39.5845, 
    viewOffsetY=156.738)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
