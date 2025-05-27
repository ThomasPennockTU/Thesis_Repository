# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2023 replay file
# Internal Version: 2023_03_20-20.15.03 RELr425 183417
# Run by tpennock on Tue May 27 09:40:13 2025
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
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57.0147, 
    farPlane=95.3993, width=61.6359, height=21.4108, viewOffsetX=14.3812, 
    viewOffsetY=0.570509)
o3 = session.openOdb(
    name='D:/tpennock/GitHub/Thesis_Repository/1.2-9 Block Flume pull test fd/Job-3.odb')
#: Model: D:/tpennock/GitHub/Thesis_Repository/1.2-9 Block Flume pull test fd/Job-3.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     13
#: Number of Meshes:             14
#: Number of Element Sets:       0
#: Number of Node Sets:          5
#: Number of Steps:              2
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].view.setValues(nearPlane=49.8347, 
    farPlane=81.077, width=33.35, height=11.5849, viewOffsetX=4.15794, 
    viewOffsetY=-0.867012)
session.viewports['Viewport: 1'].view.setValues(nearPlane=52.6056, 
    farPlane=85.1693, width=35.2044, height=12.2291, cameraPosition=(71.7723, 
    40.3687, -1.4441), cameraUpVector=(-0.816401, 0.57735, 0.0124618), 
    cameraTarget=(18.334, 2.57775, -0.628399), viewOffsetX=4.38913, 
    viewOffsetY=-0.915221)
session.viewports['Viewport: 1'].view.setValues(nearPlane=54.8594, 
    farPlane=82.9156, width=2.75306, height=0.956345, viewOffsetX=1.86595, 
    viewOffsetY=-1.33523)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
mdb.models['Model-1'].rootAssembly.sets.changeKey(fromName='Set-1', 
    toName='Sides')
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['D:/tpennock/GitHub/Thesis_Repository/1.2-9 Block Flume pull test fd/Job-3.odb'])
odb = session.odbs['D:/tpennock/GitHub/Thesis_Repository/1.2-9 Block Flume pull test fd/Job-3.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
odb = session.odbs['D:/tpennock/GitHub/Thesis_Repository/1.2-9 Block Flume pull test fd/Job-3.odb']
xyList = xyPlot.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=((
    'RF', NODAL, ((COMPONENT, 'RF1'), (COMPONENT, 'RF2'), (COMPONENT, 'RF3'), 
    )), ), nodeSets=("SET-1", ))
xyp = session.XYPlot('XYPlot-1')
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
curveList = session.curveSet(xyData=xyList)
chart.setValues(curvesToPlot=curveList)
session.charts[chartName].autoColor(lines=True, symbols=True)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
xy1 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 1']
xy2 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 2']
xy3 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 3']
xy4 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 4']
xy5 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 5']
xy6 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 6']
xy7 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 7']
xy8 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 8']
xy9 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 9']
xy10 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 10']
xy11 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 11']
xy12 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 12']
xy13 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 13']
xy14 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 14']
xy15 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 15']
xy16 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 16']
xy17 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 17']
xy18 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 18']
xy19 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 19']
xy20 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 20']
xy21 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 21']
xy22 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 22']
xy23 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 23']
xy24 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 24']
xy25 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 25']
xy26 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 32']
xy27 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 33']
xy28 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 40']
xy29 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 41']
xy30 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 48']
xy31 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 49']
xy32 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 56']
xy33 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 57']
xy34 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 64']
xy35 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 65']
xy36 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 72']
xy37 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 73']
xy38 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 80']
xy39 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 81']
xy40 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 88']
xy41 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 89']
xy42 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 96']
xy43 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 97']
xy44 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 104']
xy45 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 105']
xy46 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 112']
xy47 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 113']
xy48 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 120']
xy49 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 121']
xy50 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 128']
xy51 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 129']
xy52 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 136']
xy53 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 137']
xy54 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 144']
xy55 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 145']
xy56 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 152']
xy57 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 153']
xy58 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 160']
xy59 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 161']
xy60 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 168']
xy61 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 169']
xy62 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 170']
xy63 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 171']
xy64 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 172']
xy65 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 173']
xy66 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 174']
xy67 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 175']
xy68 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 176']
xy69 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 177']
xy70 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 178']
xy71 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 179']
xy72 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 180']
xy73 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 181']
xy74 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 182']
xy75 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 183']
xy76 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 184']
xy77 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 185']
xy78 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 186']
xy79 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 187']
xy80 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 188']
xy81 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 189']
xy82 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 190']
xy83 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 191']
xy84 = sum((xy1, xy2, xy3, xy4, xy5, xy6, xy7, xy8, xy9, xy10, xy11, xy12, 
    xy13, xy14, xy15, xy16, xy17, xy18, xy19, xy20, xy21, xy22, xy23, xy24, 
    xy25, xy26, xy27, xy28, xy29, xy30, xy31, xy32, xy33, xy34, xy35, xy36, 
    xy37, xy38, xy39, xy40, xy41, xy42, xy43, xy44, xy45, xy46, xy47, xy48, 
    xy49, xy50, xy51, xy52, xy53, xy54, xy55, xy56, xy57, xy58, xy59, xy60, 
    xy61, xy62, xy63, xy64, xy65, xy66, xy67, xy68, xy69, xy70, xy71, xy72, 
    xy73, xy74, xy75, xy76, xy77, xy78, xy79, xy80, xy81, xy82, xy83))
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
c1 = session.Curve(xyData=xy84)
chart.setValues(curvesToPlot=(c1, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
odb = session.odbs['D:/tpennock/GitHub/Thesis_Repository/1.2-9 Block Flume pull test fd/Job-3.odb']
xyList = xyPlot.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=((
    'RF', NODAL, ((COMPONENT, 'RF1'), (COMPONENT, 'RF2'), (COMPONENT, 'RF3'), 
    )), ), nodeSets=("SET-1", ))
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
curveList = session.curveSet(xyData=xyList)
chart.setValues(curvesToPlot=curveList)
session.charts[chartName].autoColor(lines=True, symbols=True)
xy1 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 1']
xy2 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 2']
xy3 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 3']
xy4 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 4']
xy5 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 5']
xy6 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 6']
xy7 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 7']
xy8 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 8']
xy9 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 9']
xy10 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 10']
xy11 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 11']
xy12 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 12']
xy13 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 13']
xy14 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 14']
xy15 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 15']
xy16 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 16']
xy17 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 17']
xy18 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 18']
xy19 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 19']
xy20 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 20']
xy21 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 21']
xy22 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 22']
xy23 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 23']
xy24 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 24']
xy25 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 25']
xy26 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 32']
xy27 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 33']
xy28 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 40']
xy29 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 41']
xy30 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 48']
xy31 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 49']
xy32 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 56']
xy33 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 57']
xy34 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 64']
xy35 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 65']
xy36 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 72']
xy37 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 73']
xy38 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 80']
xy39 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 81']
xy40 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 88']
xy41 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 89']
xy42 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 96']
xy43 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 97']
xy44 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 104']
xy45 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 105']
xy46 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 112']
xy47 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 113']
xy48 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 120']
xy49 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 121']
xy50 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 128']
xy51 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 129']
xy52 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 136']
xy53 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 137']
xy54 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 144']
xy55 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 145']
xy56 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 152']
xy57 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 153']
xy58 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 160']
xy59 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 161']
xy60 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 168']
xy61 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 169']
xy62 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 170']
xy63 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 171']
xy64 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 172']
xy65 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 173']
xy66 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 174']
xy67 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 175']
xy68 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 176']
xy69 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 177']
xy70 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 178']
xy71 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 179']
xy72 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 180']
xy73 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 181']
xy74 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 182']
xy75 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 183']
xy76 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 184']
xy77 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 185']
xy78 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 186']
xy79 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 187']
xy80 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 188']
xy81 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 189']
xy82 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 190']
xy83 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 191']
xy84 = session.xyDataObjects['_RF:RF1 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 192']
xy85 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 1']
xy86 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 2']
xy87 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 3']
xy88 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 4']
xy89 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 5']
xy90 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 6']
xy91 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 7']
xy92 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 8']
xy93 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 9']
xy94 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 10']
xy95 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 11']
xy96 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 12']
xy97 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 13']
xy98 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 14']
xy99 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 15']
xy100 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 16']
xy101 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 17']
xy102 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 18']
xy103 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 19']
xy104 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 20']
xy105 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 21']
xy106 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 22']
xy107 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 23']
xy108 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 24']
xy109 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 25']
xy110 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 32']
xy111 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 33']
xy112 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 40']
xy113 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 41']
xy114 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 48']
xy115 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 49']
xy116 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 56']
xy117 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 57']
xy118 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 64']
xy119 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 65']
xy120 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 72']
xy121 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 73']
xy122 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 80']
xy123 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 81']
xy124 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 88']
xy125 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 89']
xy126 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 96']
xy127 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 97']
xy128 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 104']
xy129 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 105']
xy130 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 112']
xy131 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 113']
xy132 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 120']
xy133 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 121']
xy134 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 128']
xy135 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 129']
xy136 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 136']
xy137 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 137']
xy138 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 144']
xy139 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 145']
xy140 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 152']
xy141 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 153']
xy142 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 160']
xy143 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 161']
xy144 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 168']
xy145 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 169']
xy146 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 170']
xy147 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 171']
xy148 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 172']
xy149 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 173']
xy150 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 174']
xy151 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 175']
xy152 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 176']
xy153 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 177']
xy154 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 178']
xy155 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 179']
xy156 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 180']
xy157 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 181']
xy158 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 182']
xy159 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 183']
xy160 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 184']
xy161 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 185']
xy162 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 186']
xy163 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 187']
xy164 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 188']
xy165 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 189']
xy166 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 190']
xy167 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 191']
xy168 = session.xyDataObjects['_RF:RF2 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 192']
xy169 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 1']
xy170 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 2']
xy171 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 3']
xy172 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 4']
xy173 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 5']
xy174 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 6']
xy175 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 7']
xy176 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 8']
xy177 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 9']
xy178 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 10']
xy179 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 11']
xy180 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 12']
xy181 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 13']
xy182 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 14']
xy183 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 15']
xy184 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 16']
xy185 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 17']
xy186 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 18']
xy187 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 19']
xy188 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 20']
xy189 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 21']
xy190 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 22']
xy191 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 23']
xy192 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 24']
xy193 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 25']
xy194 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 32']
xy195 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 33']
xy196 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 40']
xy197 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 41']
xy198 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 48']
xy199 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 49']
xy200 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 56']
xy201 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 57']
xy202 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 64']
xy203 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 65']
xy204 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 72']
xy205 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 73']
xy206 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 80']
xy207 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 81']
xy208 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 88']
xy209 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 89']
xy210 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 96']
xy211 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 97']
xy212 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 104']
xy213 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 105']
xy214 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 112']
xy215 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 113']
xy216 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 120']
xy217 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 121']
xy218 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 128']
xy219 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 129']
xy220 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 136']
xy221 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 137']
xy222 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 144']
xy223 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 145']
xy224 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 152']
xy225 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 153']
xy226 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 160']
xy227 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 161']
xy228 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 168']
xy229 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 169']
xy230 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 170']
xy231 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 171']
xy232 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 172']
xy233 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 173']
xy234 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 174']
xy235 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 175']
xy236 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 176']
xy237 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 177']
xy238 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 178']
xy239 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 179']
xy240 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 180']
xy241 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 181']
xy242 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 182']
xy243 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 183']
xy244 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 184']
xy245 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 185']
xy246 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 186']
xy247 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 187']
xy248 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 188']
xy249 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 189']
xy250 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 190']
xy251 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 191']
xy252 = session.xyDataObjects['_RF:RF3 PI: BLOCK-2-LIN-1-5-LIN-11-1 N: 192']
xy253 = sum((xy1, xy2, xy3, xy4, xy5, xy6, xy7, xy8, xy9, xy10, xy11, xy12, 
    xy13, xy14, xy15, xy16, xy17, xy18, xy19, xy20, xy21, xy22, xy23, xy24, 
    xy25, xy26, xy27, xy28, xy29, xy30, xy31, xy32, xy33, xy34, xy35, xy36, 
    xy37, xy38, xy39, xy40, xy41, xy42, xy43, xy44, xy45, xy46, xy47, xy48, 
    xy49, xy50, xy51, xy52, xy53, xy54, xy55, xy56, xy57, xy58, xy59, xy60, 
    xy61, xy62, xy63, xy64, xy65, xy66, xy67, xy68, xy69, xy70, xy71, xy72, 
    xy73, xy74, xy75, xy76, xy77, xy78, xy79, xy80, xy81, xy82, xy83, xy84)), 
    sum((xy85, xy86, xy87, xy88, xy89, xy90, xy91, xy92, xy93, xy94, xy95, 
    xy96, xy97, xy98, xy99, xy100, xy101, xy102, xy103, xy104, xy105, xy106, 
    xy107, xy108, xy109, xy110, xy111, xy112, xy113, xy114, xy115, xy116, 
    xy117, xy118, xy119, xy120, xy121, xy122, xy123, xy124, xy125, xy126, 
    xy127, xy128, xy129, xy130, xy131, xy132, xy133, xy134, xy135, xy136, 
    xy137, xy138, xy139, xy140, xy141, xy142, xy143, xy144, xy145, xy146, 
    xy147, xy148, xy149, xy150, xy151, xy152, xy153, xy154, xy155, xy156, 
    xy157, xy158, xy159, xy160, xy161, xy162, xy163, xy164, xy165, xy166, 
    xy167, xy168)), sum((xy169, xy170, xy171, xy172, xy173, xy174, xy175, 
    xy176, xy177, xy178, xy179, xy180, xy181, xy182, xy183, xy184, xy185, 
    xy186, xy187, xy188, xy189, xy190, xy191, xy192, xy193, xy194, xy195, 
    xy196, xy197, xy198, xy199, xy200, xy201, xy202, xy203, xy204, xy205, 
    xy206, xy207, xy208, xy209, xy210, xy211, xy212, xy213, xy214, xy215, 
    xy216, xy217, xy218, xy219, xy220, xy221, xy222, xy223, xy224, xy225, 
    xy226, xy227, xy228, xy229, xy230, xy231, xy232, xy233, xy234, xy235, 
    xy236, xy237, xy238, xy239, xy240, xy241, xy242, xy243, xy244, xy245, 
    xy246, xy247, xy248, xy249, xy250, xy251, xy252))
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
c1 = session.Curve(xyData=xy253)
chart.setValues(curvesToPlot=(c1, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
#* TypeError: xyData; found tuple, expecting XYData
session.xyPlots[session.viewports['Viewport: 1'].displayedObject.name].setValues(
    transform=(0.691393, 0, 0, 0.109578, 0, 0.691393, 0, -0.0546828, 0, 0, 
    0.691393, 0, 0, 0, 0, 1))
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
o3 = session.openOdb(
    name='D:/tpennock/GitHub/Thesis_Repository/1.2-9 Block Flume pull test fd/Job-3.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['D:/tpennock/GitHub/Thesis_Repository/1.2-9 Block Flume pull test fd/Job-3.odb'])
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
x = session.xyPlots['XYPlot-1']
session.viewports['Viewport: 1'].setValues(displayedObject=x)
session.xyPlots[session.viewports['Viewport: 1'].displayedObject.name].setValues(
    transform=(0.733958, 0, 0, 0.153232, 0, 0.733958, 0, -0.01909, 0, 0, 
    0.733958, 0, 0, 0, 0, 1))
odb = session.odbs['D:/tpennock/GitHub/Thesis_Repository/1.2-9 Block Flume pull test fd/Job-3.odb']
xyList = xyPlot.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=((
    'CPRESS     General_Contact_Domain', NODAL), ('RF', NODAL, ((COMPONENT, 
    'RF1'), (COMPONENT, 'RF2'), (COMPONENT, 'RF3'), )), ), nodeSets=("SET-1", 
    ))
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
curveList = session.curveSet(xyData=xyList)
chart.setValues(curvesToPlot=curveList)
session.charts[chartName].autoColor(lines=True, symbols=True)
odb = session.odbs['D:/tpennock/GitHub/Thesis_Repository/1.2-9 Block Flume pull test fd/Job-3.odb']
xyList = xyPlot.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=((
    'CPRESS     General_Contact_Domain', NODAL), (
    'CSHEARF  General_Contact_Domain', NODAL, ((INVARIANT, 'Magnitude'), )), (
    'RF', NODAL, ((COMPONENT, 'RF1'), (COMPONENT, 'RF2'), (COMPONENT, 'RF3'), 
    )), ), nodeSets=("SET-1", ))
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
curveList = session.curveSet(xyData=xyList)
chart.setValues(curvesToPlot=curveList)
session.charts[chartName].autoColor(lines=True, symbols=True)
odb = session.odbs['D:/tpennock/GitHub/Thesis_Repository/1.2-9 Block Flume pull test fd/Job-3.odb']
xyList = xyPlot.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=((
    'CSHEARF  General_Contact_Domain', NODAL, ((INVARIANT, 'Magnitude'), )), (
    'RF', NODAL, ((COMPONENT, 'RF1'), (COMPONENT, 'RF2'), (COMPONENT, 'RF3'), 
    )), ), nodeSets=("SET-1", ))
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
curveList = session.curveSet(xyData=xyList)
chart.setValues(curvesToPlot=curveList)
session.charts[chartName].autoColor(lines=True, symbols=True)
odb = session.odbs['D:/tpennock/GitHub/Thesis_Repository/1.2-9 Block Flume pull test fd/Job-3.odb']
xyList = xyPlot.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=((
    'CPRESS     General_Contact_Domain', NODAL), ('RF', NODAL, ((COMPONENT, 
    'RF1'), (COMPONENT, 'RF2'), (COMPONENT, 'RF3'), )), ), nodeSets=("SET-1", 
    ))
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
curveList = session.curveSet(xyData=xyList)
chart.setValues(curvesToPlot=curveList)
session.charts[chartName].autoColor(lines=True, symbols=True)
odb = session.odbs['D:/tpennock/GitHub/Thesis_Repository/1.2-9 Block Flume pull test fd/Job-3.odb']
xyList = xyPlot.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=((
    'CPRESS     General_Contact_Domain', NODAL), ), nodeSets=("SET-1", ))
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
curveList = session.curveSet(xyData=xyList)
chart.setValues(curvesToPlot=curveList)
session.charts[chartName].autoColor(lines=True, symbols=True)
odb = session.odbs['D:/tpennock/GitHub/Thesis_Repository/1.2-9 Block Flume pull test fd/Job-3.odb']
xyList = xyPlot.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=((
    'CNORMF   General_Contact_Domain', NODAL), ), nodeSets=("SET-1", ))
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
curveList = session.curveSet(xyData=xyList)
chart.setValues(curvesToPlot=curveList)
session.charts[chartName].autoColor(lines=True, symbols=True)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Loading')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
xyp = session.xyPlots['XYPlot-1']
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
session.charts['Chart-1'].legend.area.setValues(positionMethod=MANUAL, 
    originOffset=(0.38576, 0.0131344))
session.charts['Chart-1'].legend.area.setValues(originOffset=(0.422246, 0))
session.charts['Chart-1'].legend.area.setValues(originOffset=(0.292106, 
    0.0206253))
