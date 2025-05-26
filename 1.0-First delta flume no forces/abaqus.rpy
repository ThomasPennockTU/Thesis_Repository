# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2023 replay file
# Internal Version: 2023_03_20-20.15.03 RELr425 183417
# Run by tpennock on Mon May 26 10:05:36 2025
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
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.0987, 
    farPlane=92.5197, width=32.5081, height=11.2925, viewOffsetX=3.11252, 
    viewOffsetY=-1.34631)
a = mdb.models['Model-1'].rootAssembly
a.deleteFeatures(('RP-1', 'RP-2', ))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF, optimizationTasks=ON, 
    geometricRestrictions=ON, stopConditions=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60.1694, 
    farPlane=91.449, width=18.0276, height=6.26233, viewOffsetX=-3.79482, 
    viewOffsetY=0.6989)
a = mdb.models['Model-1'].rootAssembly
a.ReferencePoint(point=(0.0, 0.0, 0.0))
a = mdb.models['Model-1'].rootAssembly
a.ReferencePoint(point=(0.0, 0.0, 1.0))
a = mdb.models['Model-1'].rootAssembly
a.ReferencePoint(point=(0.0, 0.0, 2.0))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Loading')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.9307, 
    farPlane=91.1682, width=14.1743, height=4.92379, viewOffsetX=-5.45935, 
    viewOffsetY=0.906976)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[478], r1[479], r1[480], )
region = regionToolset.Region(referencePoints=refPoints1)
mdb.models['Model-1'].boundaryConditions['BC-1'].setValues(region=region)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, interactions=ON, constraints=ON, 
    engineeringFeatures=ON)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[478], )
region1=regionToolset.Region(referencePoints=refPoints1)
mdb.models['Model-1'].constraints['Constraint-1'].setValues(
    refPointRegion=region1)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[479], )
region1=regionToolset.Region(referencePoints=refPoints1)
mdb.models['Model-1'].constraints['Constraint-2'].setValues(
    refPointRegion=region1)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[480], )
region1=regionToolset.Region(referencePoints=refPoints1)
mdb.models['Model-1'].constraints['Constraint-3'].setValues(
    refPointRegion=region1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=55.1775, 
    farPlane=95.9213, width=76.364, height=26.5269, viewOffsetX=27.1328, 
    viewOffsetY=2.65371)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
mdb.models['Model-1'].loads.delete(('Row1', 'Row2', 'Row3', 'Row4', 'Row5', 
    'Row6', 'Row7', 'Row8', 'Row9', 'Row10', 'Row11', 'Row12', 'Row13', 
    'Row14', 'Row15', 'Row16', 'Row17', 'Row18', 'Row19', 'Row20', 'Row21', 
    'Row22', ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=58.0001, 
    farPlane=93.0987, width=39.8409, height=13.8397, viewOffsetX=11.8067, 
    viewOffsetY=0.41339)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58.041, 
    farPlane=92.9852, width=39.869, height=13.8495, cameraPosition=(58.8562, 
    46.9346, 40.5518), cameraTarget=(15.0877, 3.16609, -3.21667), 
    viewOffsetX=11.815, viewOffsetY=0.413682)
session.viewports['Viewport: 1'].view.setValues(nearPlane=66.7483, 
    farPlane=104.98, width=45.8502, height=15.9272, cameraPosition=(88.4511, 
    46.9346, -1.30528), cameraUpVector=(-0.815816, 0.57735, 0.0333265), 
    cameraTarget=(26.6047, 3.16609, 1.2212), viewOffsetX=13.5875, 
    viewOffsetY=0.475742)
session.viewports['Viewport: 1'].view.setValues(nearPlane=66.4355, 
    farPlane=105.292, width=41.7827, height=14.5143, viewOffsetX=13.0525, 
    viewOffsetY=3.95051)
del mdb.models['Model-1'].amplitudes['Row1']
del mdb.models['Model-1'].amplitudes['Row2']
del mdb.models['Model-1'].amplitudes['Row3']
del mdb.models['Model-1'].amplitudes['Row4']
del mdb.models['Model-1'].amplitudes['Row5']
del mdb.models['Model-1'].amplitudes['Row6']
del mdb.models['Model-1'].amplitudes['Row7']
del mdb.models['Model-1'].amplitudes['Row8']
del mdb.models['Model-1'].amplitudes['Row9']
del mdb.models['Model-1'].amplitudes['Row10']
del mdb.models['Model-1'].amplitudes['Row11']
del mdb.models['Model-1'].amplitudes['Row12']
del mdb.models['Model-1'].amplitudes['Row13']
del mdb.models['Model-1'].amplitudes['Row14']
del mdb.models['Model-1'].amplitudes['Row15']
del mdb.models['Model-1'].amplitudes['Row16']
del mdb.models['Model-1'].amplitudes['Row17']
del mdb.models['Model-1'].amplitudes['Row18']
del mdb.models['Model-1'].amplitudes['Row19']
del mdb.models['Model-1'].amplitudes['Row20']
del mdb.models['Model-1'].amplitudes['Row21']
del mdb.models['Model-1'].amplitudes['Row22']
mdb.save()
#: The model database has been saved to "D:\tpennock\GitHub\Thesis_Repository\1.0-First delta flume no forces\First delta flume.cae".
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.jobs['Job-2'].submit(consistencyChecking=OFF)
#: The job input file "Job-2.inp" has been submitted for analysis.
#: Job Job-2: Analysis Input File Processor completed successfully.
#: Job Job-2: Abaqus/Explicit Packager completed successfully.
#: Error in job Job-2: The elements contained in element set ErrElemExcessDistortion-Step1 have distorted excessively.
#: Error in job Job-2: Print-out suppressed for subsequent distorted elements
#: Error in job Job-2: There are a total of 8965 excessively distorted elements
#: Error in job Job-2: The ratio of deformation speed to wave speed exceeds 1.0000 in at least one element. This usually indicates an error with the model definition. Additional diagnostic information may be found in the message file.
#: Error in job Job-2: The elements contained in element set ErrElemExcessDistortion-Step1 have distorted excessively.
#: Job Job-2: Abaqus/Explicit aborted due to errors.
#: Error in job Job-2: Abaqus/Explicit Analysis exited with an error - Please see the  status file for possible error messages if the file exists.
#: Job Job-2 aborted due to errors.
mdb.save()
#: The model database has been saved to "D:\tpennock\GitHub\Thesis_Repository\1.0-First delta flume no forces\First delta flume.cae".
