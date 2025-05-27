# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2023 replay file
# Internal Version: 2023_03_20-20.15.03 RELr425 183417
# Run by tpennock on Mon May 26 16:11:43 2025
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
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.7524, 
    farPlane=92.6616, width=25.3582, height=8.80881, viewOffsetX=6.33672, 
    viewOffsetY=-1.41278)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61.5588, 
    farPlane=98.2235, width=26.1249, height=9.07512, cameraPosition=(78.5704, 
    47.1273, 15.5755), cameraUpVector=(-0.791081, 0.57735, -0.202133), 
    cameraTarget=(18.2845, 3.12913, 0.171499), viewOffsetX=6.52829, 
    viewOffsetY=-1.45549)
o3 = session.openOdb(
    name='D:/tpennock/GitHub/Thesis_Repository/1.2-9 Block Flume pull test/Job-2.odb')
#: Model: D:/tpennock/GitHub/Thesis_Repository/1.2-9 Block Flume pull test/Job-2.odb
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
    displayedObject=session.odbs['D:/tpennock/GitHub/Thesis_Repository/1.2-9 Block Flume pull test/Job-2.odb'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=47.6693, 
    farPlane=83.9509, width=49.6904, height=17.2612, cameraPosition=(67.3936, 
    40.3687, 5.4943), cameraUpVector=(-0.806837, 0.57735, -0.125223), 
    cameraTarget=(14.5814, 2.57775, -2.70228))
session.viewports['Viewport: 1'].view.setValues(nearPlane=49.7182, 
    farPlane=81.9019, width=24.6861, height=8.57534, viewOffsetX=2.57894, 
    viewOffsetY=-3.88354)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
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
session.viewports['Viewport: 1'].view.setValues(nearPlane=48.0098, 
    farPlane=83.6714, width=50.0454, height=17.3845, cameraPosition=(67.9926, 
    40.3687, -0.815188), cameraUpVector=(-0.815987, 0.57735, -0.0288299), 
    cameraTarget=(14.5814, 2.57775, -2.70228))
session.viewports['Viewport: 1'].view.setValues(nearPlane=50.403, 
    farPlane=81.2782, width=20.3728, height=7.07699, viewOffsetX=2.05883, 
    viewOffsetY=-3.78857)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].view.setValues(nearPlane=862.256, 
    farPlane=1326, width=20.4515, height=7.10434, viewOffsetX=-8.95893, 
    viewOffsetY=103.486)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].view.setValues(nearPlane=943.29, 
    farPlane=1336.79, width=5.80045, height=2.01493, viewOffsetX=-11.1812, 
    viewOffsetY=113.33)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62.5404, 
    farPlane=97.2419, width=11.7103, height=4.06787, viewOffsetX=5.33561, 
    viewOffsetY=-2.25909)
a = mdb.models['Model-1'].rootAssembly
i1 = a.instances['Wall-1-lin-1-2']
leaf = dgm.LeafFromInstance((i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62.6101, 
    farPlane=97.1621, width=10.6799, height=3.70992, viewOffsetX=4.9575, 
    viewOffsetY=-1.79393)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
a = mdb.models['Model-1'].rootAssembly
a.DatumAxisByPrincipalAxis(principalAxis=YAXIS)
a = mdb.models['Model-1'].rootAssembly
a.DatumAxisByPrincipalAxis(principalAxis=YAXIS)
a = mdb.models['Model-1'].rootAssembly
a.DatumAxisByPrincipalAxis(principalAxis=YAXIS)
a = mdb.models['Model-1'].rootAssembly
a.DatumAxisByPrincipalAxis(principalAxis=YAXIS)
session.viewports['Viewport: 1'].view.setValues(nearPlane=63.1603, 
    farPlane=96.6118, width=3.54065, height=1.22993, viewOffsetX=3.2214, 
    viewOffsetY=-1.56946)
a = mdb.models['Model-1'].rootAssembly
v1 = a.instances['Block-2-lin-1-5-lin-11-1'].vertices
e1 = a.instances['Block-2-lin-1-8-lin-2-1-lin-lin-11-1-5'].edges
a.DatumCsysByThreePoints(origin=v1[4], name='Datum csys-2', 
    coordSysType=CARTESIAN, 
    point1=a.instances['Block-2-lin-1-8-lin-2-1-lin-lin-11-1-5'].InterestingPoint(
    edge=e1[4], rule=MIDDLE), line2=(0.075, 0.225625, 0.003953))
session.viewports['Viewport: 1'].view.setValues(nearPlane=62.657, 
    farPlane=97.1152, width=10.3822, height=3.5464, viewOffsetX=4.79298, 
    viewOffsetY=-0.981554)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['D:/tpennock/GitHub/Thesis_Repository/1.2-9 Block Flume pull test/Job-1.odb'])
o3 = session.openOdb(
    name='D:/tpennock/GitHub/Thesis_Repository/1.2-9 Block Flume pull test/Job-2.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].view.setValues(nearPlane=50.488, 
    farPlane=81.132, width=14.6199, height=4.99396, viewOffsetX=1.87056, 
    viewOffsetY=-3.5135)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=ON, geometricRestrictions=ON, stopConditions=ON)
o3 = session.openOdb(
    name='D:/tpennock/GitHub/Thesis_Repository/1.2-9 Block Flume pull test/Job-1.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['D:/tpennock/GitHub/Thesis_Repository/1.2-9 Block Flume pull test/Job-1.odb'])
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61.1104, 
    farPlane=98.6618, width=31.2239, height=10.6656, viewOffsetX=10.0621, 
    viewOffsetY=0.907825)
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.5936, 
    farPlane=92.7749, width=27.9103, height=9.53375, viewOffsetX=2.20856, 
    viewOffsetY=-1.49666)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
#: The job input file "Job-1.inp" has been submitted for analysis.
#: Job Job-1: Analysis Input File Processor completed successfully.
#: Job Job-1: Abaqus/Explicit Packager completed successfully.
session.viewports['Viewport: 1'].view.setValues(nearPlane=60.3448, 
    farPlane=92.0236, width=16.8849, height=6.07176, viewOffsetX=2.99483, 
    viewOffsetY=-1.99002)
mdb.save()
#: The model database has been saved to "D:\tpennock\GitHub\Thesis_Repository\1.2-9 Block Flume pull test\First delta flume.cae".
