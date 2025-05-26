# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2023 replay file
# Internal Version: 2023_03_20-20.15.03 RELr425 183417
# Run by tpennock on Mon May 26 11:31:17 2025
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
#: The model database "D:\tpennock\GitHub\Thesis_Repository\1.2-9 Block Flume pull test fd\First delta flume.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['Block']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(
    name='D:/tpennock/GitHub/Thesis_Repository/1.2-9 Block Flume pull test fd/Job-3.odb')
#: Model: D:/tpennock/GitHub/Thesis_Repository/1.2-9 Block Flume pull test fd/Job-3.odb
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
    displayedObject=session.odbs['D:/tpennock/GitHub/Thesis_Repository/1.2-9 Block Flume pull test fd/Job-3.odb'])
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=48.6881, 
    farPlane=83.0305, width=39.9509, height=17.6301, cameraPosition=(67.7789, 
    40.3687, -7.83494), cameraUpVector=(-0.812723, 0.57735, 0.0784141), 
    cameraTarget=(14.5814, 2.57775, -2.70228))
session.viewports['Viewport: 1'].view.setValues(nearPlane=51.0846, 
    farPlane=80.6341, width=9.17216, height=4.04763, viewOffsetX=-0.502641, 
    viewOffsetY=-3.16636)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.6177, 
    farPlane=92.7963, width=27.697, height=12.2225, viewOffsetX=2.77256, 
    viewOffsetY=-1.74823)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60.3687, 
    farPlane=96.6723, width=28.0459, height=12.3765, cameraPosition=(79.2472, 
    47.1273, -1.5547), cameraUpVector=(-0.816368, 0.57735, 0.0145042), 
    cameraTarget=(17.0342, 3.12913, -0.449372), viewOffsetX=2.80749, 
    viewOffsetY=-1.77025)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62.1583, 
    farPlane=94.8826, width=3.35244, height=1.47941, viewOffsetX=2.01996, 
    viewOffsetY=-2.2446)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['DikeRigid-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#20 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=67.8344, 
    farPlane=86.3051, width=50.1319, height=22.1229, viewOffsetX=5.63154, 
    viewOffsetY=-1.56925)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61.949, 
    farPlane=95.092, width=6.13791, height=2.70863, viewOffsetX=2.25455, 
    viewOffsetY=-2.01011)
a = mdb.models['Model-1'].rootAssembly
i1 = a.instances['Block-2-lin-1-5-lin-11-1']
leaf = dgm.LeafFromInstance((i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=73.7116, 
    farPlane=74.6517, width=2.19475, height=0.96853, viewOffsetX=1.93402, 
    viewOffsetY=-2.77802)
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['D:/tpennock/GitHub/Thesis_Repository/1.2-9 Block Flume pull test fd/Job-3.odb'])
odb = session.odbs['D:/tpennock/GitHub/Thesis_Repository/1.2-9 Block Flume pull test fd/Job-3.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51.4717, 
    farPlane=80.247, width=4.26723, height=1.88311, viewOffsetX=-0.3754, 
    viewOffsetY=-2.99737)
leaf = dgo.LeafFromPartInstance(partInstanceName=("BLOCK-2-LIN-1-5-LIN-11-1", 
    ))
session.viewports['Viewport: 1'].odbDisplay.displayGroup.replace(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60.717, 
    farPlane=61.6696, width=2.01541, height=0.889391, viewOffsetX=-0.798125, 
    viewOffsetY=-3.69015)
odb = session.odbs['D:/tpennock/GitHub/Thesis_Repository/1.2-9 Block Flume pull test fd/Job-3.odb']
xyList = xyPlot.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=((
    'U', NODAL, ((COMPONENT, 'U2'), )), ), nodePick=((
    'BLOCK-2-LIN-1-5-LIN-11-1', 1, ('[#0 #1 ]', )), ), )
xyp = session.XYPlot('XYPlot-1')
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
curveList = session.curveSet(xyData=xyList)
chart.setValues(curvesToPlot=curveList)
session.charts[chartName].autoColor(lines=True, symbols=True)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
odb = session.odbs['D:/tpennock/GitHub/Thesis_Repository/1.2-9 Block Flume pull test fd/Job-3.odb']
xyList = xyPlot.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=((
    'U', NODAL, ((COMPONENT, 'U1'), )), ), nodePick=((
    'BLOCK-2-LIN-1-5-LIN-11-1', 1, ('[#0 #1 ]', )), ), )
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
curveList = session.curveSet(xyData=xyList)
chart.setValues(curvesToPlot=curveList)
session.charts[chartName].autoColor(lines=True, symbols=True)
odb = session.odbs['D:/tpennock/GitHub/Thesis_Repository/1.2-9 Block Flume pull test fd/Job-3.odb']
xyList = xyPlot.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=((
    'U', NODAL, ((COMPONENT, 'U3'), )), ), nodePick=((
    'BLOCK-2-LIN-1-5-LIN-11-1', 1, ('[#0 #1 ]', )), ), )
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
curveList = session.curveSet(xyData=xyList)
chart.setValues(curvesToPlot=curveList)
session.charts[chartName].autoColor(lines=True, symbols=True)
odb = session.odbs['D:/tpennock/GitHub/Thesis_Repository/1.2-9 Block Flume pull test fd/Job-3.odb']
xyList = xyPlot.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=((
    'U', NODAL, ((COMPONENT, 'U2'), )), ), nodePick=((
    'BLOCK-2-LIN-1-5-LIN-11-1', 1, ('[#0 #1 ]', )), ), )
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
curveList = session.curveSet(xyData=xyList)
chart.setValues(curvesToPlot=curveList)
session.charts[chartName].autoColor(lines=True, symbols=True)
