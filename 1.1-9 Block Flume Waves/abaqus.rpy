# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2023 replay file
# Internal Version: 2023_03_20-20.15.03 RELr425 183417
# Run by tpennock on Wed May 21 10:23:03 2025
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
#: The model database "D:\tpennock\GitHub\Thesis_Repository\1.1-9 Block Flume Waves\First delta flume.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['Block']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58.7619, 
    farPlane=93.6521, width=42.3027, height=14.6949, viewOffsetX=2.44659, 
    viewOffsetY=-0.458517)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.3195, 
    farPlane=98.675, width=42.7041, height=14.8343, cameraPosition=(78.5955, 
    45.7812, -18.6892), cameraUpVector=(-0.773806, 0.594988, 0.217286), 
    cameraTarget=(17.8752, 3.1487, -1.28159), viewOffsetX=2.46981, 
    viewOffsetY=-0.462868)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60.7904, 
    farPlane=97.2041, width=22.2138, height=7.71652, viewOffsetX=1.33781, 
    viewOffsetY=-1.25061)
mdb.jobs['Job-2'].submit(consistencyChecking=OFF)
#: The job input file "Job-2.inp" has been submitted for analysis.
#: Job Job-2: Analysis Input File Processor completed successfully.
#: Job Job-2: Abaqus/Explicit Packager completed successfully.
#: Error in job Job-2: The elements contained in element set ErrElemExcessDistortion-Step2 have distorted excessively.
#: Error in job Job-2: There are a total of 2 excessively distorted elements
#: Error in job Job-2: The ratio of deformation speed to wave speed exceeds 1.0000 in at least one element. This usually indicates an error with the model definition. Additional diagnostic information may be found in the message file.
#: Error in job Job-2: The elements contained in element set ErrElemExcessDistortion-Step2 have distorted excessively.
#: Job Job-2: Abaqus/Explicit aborted due to errors.
#: Error in job Job-2: Abaqus/Explicit Analysis exited with an error - Please see the  status file for possible error messages if the file exists.
#: Job Job-2 aborted due to errors.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Gravity')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, interactions=ON, constraints=ON, 
    engineeringFeatures=ON)
