# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2023 replay file
# Internal Version: 2023_03_20-20.15.03 RELr425 183417
# Run by tpennock on Tue May 20 10:46:30 2025
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=550.666687011719, 
    height=264.733001708984)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
openMdb('First delta flume.cae')
#: The model database "D:\tpennock\9-Block Flume\First delta flume.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['Block']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58.381, 
    farPlane=93.2375, width=43.3035, height=17.0399, viewOffsetX=0.908833, 
    viewOffsetY=-0.581269)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['Wall-1-lin-1-2'].faces
faces1 = f1.getSequenceFromMask(mask=('[#e ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.9584, 
    farPlane=91.66, width=21.3163, height=8.38798, viewOffsetX=0.408509, 
    viewOffsetY=0.8666)
a1 = mdb.models['Model-1'].rootAssembly
a1.excludeFromSimulation(instances=(a1.instances['HalfBlock-1'], 
    a1.instances['Block-2'], a1.instances['Block-2-lin-1-2'], 
    a1.instances['Block-2-lin-1-3'], a1.instances['Block-2-lin-1-4'], 
    a1.instances['Block-2-lin-1-5'], a1.instances['Block-2-lin-1-6'], 
    a1.instances['Block-2-lin-1-7'], a1.instances['Block-2-lin-1-8'], 
    a1.instances['HalfBlock-1-lin-1-2'], 
    a1.instances['Block-2-lin-1-8-lin-2-1'], 
    a1.instances['Block-2-lin-1-8-lin-2-1-lin-1-2'], 
    a1.instances['Block-2-lin-1-8-lin-2-1-lin-1-3'], 
    a1.instances['Block-2-lin-1-8-lin-2-1-lin-1-4'], 
    a1.instances['Block-2-lin-1-8-lin-2-1-lin-1-5'], 
    a1.instances['Block-2-lin-1-8-lin-2-1-lin-1-6'], 
    a1.instances['Block-2-lin-1-8-lin-2-1-lin-1-7'], 
    a1.instances['Block-2-lin-1-8-lin-2-1-lin-1-8'], 
    a1.instances['Block-2-lin-1-8-lin-2-1-lin-1-9'], 
    a1.instances['HalfBlock-1-lin-2-1'], a1.instances['HalfBlock-1-lin-3-1'], 
    a1.instances['HalfBlock-1-lin-4-1'], a1.instances['HalfBlock-1-lin-5-1'], 
    a1.instances['HalfBlock-1-lin-6-1'], a1.instances['HalfBlock-1-lin-7-1'], 
    a1.instances['HalfBlock-1-lin-8-1'], a1.instances['HalfBlock-1-lin-9-1'], 
    a1.instances['HalfBlock-1-lin-10-1'], a1.instances['HalfBlock-1-lin-11-1'], 
    a1.instances['Block-2-lin-2-1'], ), exclude=True)
#: Warning: There are one or more sets or surfaces defined on at least some of the selected instances.
#: If these are used in the model definition, then errors may result in the analysis.
a = mdb.models['Model-1'].rootAssembly
a.deleteFeatures(('HalfBlock-1', 'Block-2', 'Block-2-lin-1-2', 
    'Block-2-lin-1-3', 'Block-2-lin-1-4', 'Block-2-lin-1-5', 'Block-2-lin-1-6', 
    'Block-2-lin-1-7', 'Block-2-lin-1-8', 'HalfBlock-1-lin-1-2', 
    'Block-2-lin-1-8-lin-2-1', 'Block-2-lin-1-8-lin-2-1-lin-1-2', 
    'Block-2-lin-1-8-lin-2-1-lin-1-3', 'Block-2-lin-1-8-lin-2-1-lin-1-4', 
    'Block-2-lin-1-8-lin-2-1-lin-1-5', 'Block-2-lin-1-8-lin-2-1-lin-1-6', 
    'Block-2-lin-1-8-lin-2-1-lin-1-7', 'Block-2-lin-1-8-lin-2-1-lin-1-8', 
    'Block-2-lin-1-8-lin-2-1-lin-1-9', 'HalfBlock-1-lin-2-1', 
    'HalfBlock-1-lin-3-1', 'HalfBlock-1-lin-4-1', 'HalfBlock-1-lin-5-1', 
    'HalfBlock-1-lin-6-1', 'HalfBlock-1-lin-7-1', 'HalfBlock-1-lin-8-1', 
    'HalfBlock-1-lin-9-1', 'HalfBlock-1-lin-10-1', 'HalfBlock-1-lin-11-1', 
    'Block-2-lin-2-1', ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.5794, 
    farPlane=92.039, width=27.5455, height=10.8392, viewOffsetX=7.44427, 
    viewOffsetY=-0.8767)
a = mdb.models['Model-1'].rootAssembly
a.deleteFeatures(('Block-2-lin-3-1', 'Block-2-lin-4-1', 'Block-2-lin-5-1', 
    'Block-2-lin-6-1', 'Block-2-lin-7-1', 'Block-2-lin-8-1', 'Block-2-lin-9-1', 
    'Block-2-lin-10-1', 'Block-2-lin-11-1', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-2-1-1', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-3-1-1', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-4-1-1', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-5-1-1', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-6-1-1', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-7-1-1', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-8-1-1', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-9-1-1', 
    'Block-2-lin-1-8-lin-2-1-lin-lin-10-1-1', 
    'Block-2-lin-1-8-lin-2-1-lin-lin-11-1-1', 'Block-2-lin-1-2-lin-2-1', 
    'Block-2-lin-1-2-lin-3-1', 'Block-2-lin-1-2-lin-4-1', 
    'Block-2-lin-1-2-lin-5-1', 'Block-2-lin-1-2-lin-6-1', 
    'Block-2-lin-1-2-lin-7-1', 'Block-2-lin-1-2-lin-8-1', 
    'Block-2-lin-1-2-lin-9-1', 'Block-2-lin-1-2-lin-10-1', 
    'Block-2-lin-1-2-lin-11-1', 'Block-2-lin-1-8-lin-2-1-lin--lin-2-1-3', ))
a = mdb.models['Model-1'].rootAssembly
a.deleteFeatures(('Block-2-lin-1-8-lin-2-1-lin--lin-3-1-3', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-4-1-3', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-5-1-3', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-6-1-3', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-7-1-3', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-8-1-3', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-9-1-3', 'Block-2-lin-1-4-lin-2-1', 
    'Block-2-lin-1-4-lin-3-1', 'Block-2-lin-1-4-lin-4-1', 
    'Block-2-lin-1-4-lin-5-1', 'Block-2-lin-1-4-lin-6-1', 
    'Block-2-lin-1-4-lin-7-1', 'Block-2-lin-1-4-lin-8-1', 
    'Block-2-lin-1-4-lin-9-1', 'Block-2-lin-1-4-lin-10-1', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-2-1-5', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-3-1-5', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-4-1-5', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-5-1-5', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-6-1-5', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-7-1-5', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-8-1-5', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-9-1-5', ))
a = mdb.models['Model-1'].rootAssembly
a.deleteFeatures(('Block-2-lin-1-6-lin-2-1', 'Block-2-lin-1-6-lin-3-1', 
    'Block-2-lin-1-6-lin-4-1', 'Block-2-lin-1-6-lin-5-1', 
    'Block-2-lin-1-6-lin-6-1', 'Block-2-lin-1-6-lin-7-1', 
    'Block-2-lin-1-6-lin-8-1', 'Block-2-lin-1-6-lin-9-1', 
    'Block-2-lin-1-6-lin-10-1', ))
a = mdb.models['Model-1'].rootAssembly
a.deleteFeatures(('Block-2-lin-1-8-lin-2-1-lin--lin-2-1-7', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-3-1-7', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-4-1-7', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-5-1-7', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-6-1-7', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-7-1-7', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-8-1-7', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-9-1-7', 
    'Block-2-lin-1-8-lin-2-1-lin-lin-10-1-7', ))
a = mdb.models['Model-1'].rootAssembly
a.deleteFeatures(('Block-2-lin-1-8-lin-2-1-1', 'Block-2-lin-1-8-lin-3-1', 
    'Block-2-lin-1-8-lin-4-1', 'Block-2-lin-1-8-lin-5-1', 
    'Block-2-lin-1-8-lin-6-1', 'Block-2-lin-1-8-lin-7-1', 
    'Block-2-lin-1-8-lin-8-1', 'Block-2-lin-1-8-lin-9-1', 
    'Block-2-lin-1-8-lin-10-1', ))
a = mdb.models['Model-1'].rootAssembly
a.deleteFeatures(('HalfBlock-1-lin-1-2-lin-2-1', 'HalfBlock-1-lin-1-2-lin-3-1', 
    'HalfBlock-1-lin-1-2-lin-4-1', 'HalfBlock-1-lin-1-2-lin-5-1', 
    'HalfBlock-1-lin-1-2-lin-6-1', 'HalfBlock-1-lin-1-2-lin-7-1', 
    'HalfBlock-1-lin-1-2-lin-8-1', 'HalfBlock-1-lin-1-2-lin-9-1', 
    'HalfBlock-1-lin-1-2-lin-10-1', ))
a = mdb.models['Model-1'].rootAssembly
a.deleteFeatures(('Block-2-lin-1-8-lin-2-1-lin--lin-2-1', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-3-1', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-4-1', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-5-1', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-6-1', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-7-1', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-8-1', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-9-1', 
    'Block-2-lin-1-8-lin-2-1-lin-lin-10-1', 
    'Block-2-lin-1-8-lin-2-1-lin-lin-11-1', ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=60.504, 
    farPlane=91.1145, width=13.8941, height=5.65769, viewOffsetX=5.59225, 
    viewOffsetY=-2.00428)
a = mdb.models['Model-1'].rootAssembly
a.deleteFeatures(('Block-2-lin-1-8-lin-2-1-lin-lin-11-1-2', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-2-1-2', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-3-1-2', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-4-1-2', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-5-1-2', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-6-1-2', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-7-1-2', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-8-1-2', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-9-1-2', 
    'Block-2-lin-1-8-lin-2-1-lin-lin-10-1-2', ))
a = mdb.models['Model-1'].rootAssembly
a.deleteFeatures(('HalfBlock-1-lin-1-2-lin-11-1', 'Block-2-lin-1-3-lin-2-1', 
    'Block-2-lin-1-3-lin-3-1', 'Block-2-lin-1-3-lin-4-1', 
    'Block-2-lin-1-3-lin-5-1', 'Block-2-lin-1-3-lin-6-1', 
    'Block-2-lin-1-3-lin-7-1', 'Block-2-lin-1-3-lin-8-1', 
    'Block-2-lin-1-3-lin-9-1', 'Block-2-lin-1-3-lin-10-1', ))
a = mdb.models['Model-1'].rootAssembly
a.deleteFeatures(('Block-2-lin-1-8-lin-2-1-lin--lin-2-1-4', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-3-1-4', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-4-1-4', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-5-1-4', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-6-1-4', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-7-1-4', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-8-1-4', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-9-1-4', ))
a = mdb.models['Model-1'].rootAssembly
a.deleteFeatures(('Block-2-lin-1-8-lin-2-1-lin-2-1', 
    'Block-2-lin-1-8-lin-2-1-lin-3-1', 'Block-2-lin-1-8-lin-2-1-lin-4-1', 
    'Block-2-lin-1-8-lin-2-1-lin-5-1', 'Block-2-lin-1-8-lin-2-1-lin-6-1', 
    'Block-2-lin-1-8-lin-2-1-lin-7-1', 'Block-2-lin-1-8-lin-2-1-lin-8-1', 
    'Block-2-lin-1-8-lin-2-1-lin-9-1', 'Block-2-lin-1-8-lin-2-1-lin-10-1', 
    'Block-2-lin-1-8-lin-2-1-lin-11-1', ))
a = mdb.models['Model-1'].rootAssembly
a.deleteFeatures(('Block-2-lin-1-5-lin-2-1', 'Block-2-lin-1-5-lin-3-1', 
    'Block-2-lin-1-5-lin-4-1', 'Block-2-lin-1-5-lin-5-1', 
    'Block-2-lin-1-5-lin-6-1', 'Block-2-lin-1-5-lin-7-1', 
    'Block-2-lin-1-5-lin-8-1', 'Block-2-lin-1-5-lin-9-1', 
    'Block-2-lin-1-5-lin-10-1', ))
a = mdb.models['Model-1'].rootAssembly
a.deleteFeatures(('Block-2-lin-1-8-lin-2-1-lin--lin-2-1-6', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-3-1-6', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-4-1-6', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-5-1-6', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-6-1-6', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-7-1-6', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-8-1-6', 
    'Block-2-lin-1-8-lin-2-1-lin--lin-9-1-6', ))
a = mdb.models['Model-1'].rootAssembly
a.deleteFeatures(('Block-2-lin-1-7-lin-2-1', 'Block-2-lin-1-7-lin-3-1', 
    'Block-2-lin-1-7-lin-4-1', 'Block-2-lin-1-7-lin-5-1', 
    'Block-2-lin-1-7-lin-6-1', 'Block-2-lin-1-7-lin-7-1', 
    'Block-2-lin-1-7-lin-8-1', 'Block-2-lin-1-7-lin-9-1', ))
a = mdb.models['Model-1'].rootAssembly
del a.features['Block-2-lin-1-7-lin-10-1']
a = mdb.models['Model-1'].rootAssembly
del a.features['Block-2-lin-1-8-lin-11-1']
a = mdb.models['Model-1'].rootAssembly
del a.features['Block-2-lin-1-8-lin-2-1-lin-lin-11-1-7']
a = mdb.models['Model-1'].rootAssembly
a.deleteFeatures(('Block-2-lin-1-8-lin-2-1-lin-lin-10-1-6', 
    'Block-2-lin-1-8-lin-2-1-lin-lin-11-1-6', 'Block-2-lin-1-7-lin-11-1', ))
mdb.save()
#: The model database has been saved to "D:\tpennock\9-Block Flume\First delta flume.cae".
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Loading')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.jobs['Job-2'].submit(consistencyChecking=OFF)
#: The job input file "Job-2.inp" has been submitted for analysis.
#: Error in job Job-2: SURFACE DEFINITION ASSEMBLY__PICKEDSURF459 NOT FOUND.
#: Error in job Job-2: SURFACE DEFINITION ASSEMBLY__PICKEDSURF460 NOT FOUND.
#: Error in job Job-2: SURFACE DEFINITION ASSEMBLY__PICKEDSURF461 NOT FOUND.
#: Error in job Job-2: SURFACE DEFINITION ASSEMBLY__PICKEDSURF462 NOT FOUND.
#: Error in job Job-2: SURFACE DEFINITION ASSEMBLY__PICKEDSURF463 NOT FOUND.
#: Error in job Job-2: SURFACE DEFINITION ASSEMBLY__PICKEDSURF464 NOT FOUND.
#: Error in job Job-2: SURFACE DEFINITION ASSEMBLY__PICKEDSURF465 NOT FOUND.
#: Error in job Job-2: SURFACE DEFINITION ASSEMBLY__PICKEDSURF466 NOT FOUND.
#: Error in job Job-2: SURFACE DEFINITION ASSEMBLY__PICKEDSURF467 NOT FOUND.
#: Error in job Job-2: SURFACE DEFINITION ASSEMBLY__PICKEDSURF468 NOT FOUND.
#: Error in job Job-2: SURFACE DEFINITION ASSEMBLY__PICKEDSURF469 NOT FOUND.
#: Error in job Job-2: SURFACE DEFINITION ASSEMBLY__PICKEDSURF470 NOT FOUND.
#: Error in job Job-2: SURFACE DEFINITION ASSEMBLY__PICKEDSURF471 NOT FOUND.
#: Error in job Job-2: SURFACE DEFINITION ASSEMBLY__PICKEDSURF472 NOT FOUND.
#: Error in job Job-2: SURFACE DEFINITION ASSEMBLY__PICKEDSURF473 NOT FOUND.
#: Error in job Job-2: SURFACE DEFINITION ASSEMBLY__PICKEDSURF474 NOT FOUND.
#: Error in job Job-2: SURFACE DEFINITION ASSEMBLY__PICKEDSURF475 NOT FOUND.
#: Error in job Job-2: SURFACE DEFINITION ASSEMBLY__PICKEDSURF476 NOT FOUND.
#: Error in job Job-2: SURFACE DEFINITION ASSEMBLY__PICKEDSURF477 NOT FOUND.
#: Error in job Job-2: NODE 2 (ASSEMBLY) IS USED AS A REFERENCE NODE FOR MORE THAN ONE RIGID BODY PROPERTY DEFINITION. EACH RIGID BODY PROPERTY DEFINITION MUST HAVE A UNIQUE REFERENCE NODE
#: Error in job Job-2: NODE 2 (ASSEMBLY) IS USED AS A REFERENCE NODE FOR MORE THAN ONE RIGID BODY PROPERTY DEFINITION. EACH RIGID BODY PROPERTY DEFINITION MUST HAVE A UNIQUE REFERENCE NODE
#: Error in job Job-2: THE SURFACE ASSEMBLY__PICKEDSURF459 HAS NOT BEEN LOCATED
#: Error in job Job-2: THE SURFACE ASSEMBLY__PICKEDSURF460 HAS NOT BEEN LOCATED
#: Error in job Job-2: THE SURFACE ASSEMBLY__PICKEDSURF461 HAS NOT BEEN LOCATED
#: Error in job Job-2: THE SURFACE ASSEMBLY__PICKEDSURF462 HAS NOT BEEN LOCATED
#: Error in job Job-2: THE SURFACE ASSEMBLY__PICKEDSURF463 HAS NOT BEEN LOCATED
#: Error in job Job-2: THE SURFACE ASSEMBLY__PICKEDSURF464 HAS NOT BEEN LOCATED
#: Error in job Job-2: THE SURFACE ASSEMBLY__PICKEDSURF465 HAS NOT BEEN LOCATED
#: Error in job Job-2: THE SURFACE ASSEMBLY__PICKEDSURF466 HAS NOT BEEN LOCATED
#: Error in job Job-2: THE SURFACE ASSEMBLY__PICKEDSURF467 HAS NOT BEEN LOCATED
#: Error in job Job-2: THE SURFACE ASSEMBLY__PICKEDSURF468 HAS NOT BEEN LOCATED
#: Error in job Job-2: THE SURFACE ASSEMBLY__PICKEDSURF469 HAS NOT BEEN LOCATED
#: Error in job Job-2: THE SURFACE ASSEMBLY__PICKEDSURF470 HAS NOT BEEN LOCATED
#: Error in job Job-2: THE SURFACE ASSEMBLY__PICKEDSURF471 HAS NOT BEEN LOCATED
#: Error in job Job-2: THE SURFACE ASSEMBLY__PICKEDSURF472 HAS NOT BEEN LOCATED
#: Error in job Job-2: THE SURFACE ASSEMBLY__PICKEDSURF473 HAS NOT BEEN LOCATED
#: Error in job Job-2: THE SURFACE ASSEMBLY__PICKEDSURF474 HAS NOT BEEN LOCATED
#: Error in job Job-2: THE SURFACE ASSEMBLY__PICKEDSURF475 HAS NOT BEEN LOCATED
#: Error in job Job-2: THE SURFACE ASSEMBLY__PICKEDSURF476 HAS NOT BEEN LOCATED
#: Error in job Job-2: THE SURFACE ASSEMBLY__PICKEDSURF477 HAS NOT BEEN LOCATED
#: Job Job-2: Analysis Input File Processor aborted due to errors.
#: Error in job Job-2: Analysis Input File Processor exited with an error - Please see the  Job-2.dat file for possible error messages if the file exists.
#: Job Job-2 aborted due to errors.
session.viewports['Viewport: 1'].view.setValues(nearPlane=60.0476, 
    farPlane=91.5708, width=19.1742, height=8.1531, viewOffsetX=6.54476, 
    viewOffsetY=-1.89737)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
mdb.models['Model-1'].loads['Row1'].suppress()
mdb.models['Model-1'].loads['Row1'].resume()
mdb.models['Model-1'].loads['Row2'].suppress()
mdb.models['Model-1'].loads['Row2'].resume()
mdb.models['Model-1'].loads['Row3'].suppress()
mdb.models['Model-1'].loads['Row3'].resume()
del mdb.models['Model-1'].loads['Row4']
mdb.models['Model-1'].loads.delete(('Row5', 'Row6', 'Row7', 'Row8', 'Row9', 
    'Row10', 'Row11', 'Row12', 'Row13', 'Row14', 'Row15', 'Row16', 'Row17', 
    'Row18', 'Row19', 'Row20', 'Row21', 'Row22', ))
del mdb.models['Model-1'].amplitudes['Row22']
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
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.jobs['Job-2'].submit(consistencyChecking=OFF)
#: The job input file "Job-2.inp" has been submitted for analysis.
#: Error in job Job-2: NODE 2 (ASSEMBLY) IS USED AS A REFERENCE NODE FOR MORE THAN ONE RIGID BODY PROPERTY DEFINITION. EACH RIGID BODY PROPERTY DEFINITION MUST HAVE A UNIQUE REFERENCE NODE
#: Error in job Job-2: NODE 2 (ASSEMBLY) IS USED AS A REFERENCE NODE FOR MORE THAN ONE RIGID BODY PROPERTY DEFINITION. EACH RIGID BODY PROPERTY DEFINITION MUST HAVE A UNIQUE REFERENCE NODE
#: Job Job-2: Analysis Input File Processor aborted due to errors.
#: Error in job Job-2: Analysis Input File Processor exited with an error - Please see the  Job-2.dat file for possible error messages if the file exists.
#: Job Job-2 aborted due to errors.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60.8884, 
    farPlane=90.73, width=8.63246, height=3.13753, viewOffsetX=4.40304, 
    viewOffsetY=-2.76812)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Block-2-lin-1-8-lin-2-1-lin-lin-11-1-4'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#10 ]', ), )
s2 = a.instances['Block-2-lin-1-8-lin-2-1-lin-lin-11-1-5'].faces
side1Faces2 = s2.getSequenceFromMask(mask=('[#10 ]', ), )
s3 = a.instances['Block-2-lin-1-8-lin-2-1-lin-lin-11-1-3'].faces
side1Faces3 = s3.getSequenceFromMask(mask=('[#10 ]', ), )
region = regionToolset.Region(side1Faces=side1Faces1+side1Faces2+side1Faces3)
mdb.models['Model-1'].loads['Row1'].setValues(region=region)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Block-2-lin-1-3-lin-11-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#10 ]', ), )
s2 = a.instances['Block-2-lin-1-4-lin-11-1'].faces
side1Faces2 = s2.getSequenceFromMask(mask=('[#10 ]', ), )
s3 = a.instances['Block-2-lin-1-5-lin-11-1'].faces
side1Faces3 = s3.getSequenceFromMask(mask=('[#10 ]', ), )
s4 = a.instances['Block-2-lin-1-6-lin-11-1'].faces
side1Faces4 = s4.getSequenceFromMask(mask=('[#10 ]', ), )
region = regionToolset.Region(side1Faces=side1Faces1+side1Faces2+side1Faces3+\
    side1Faces4)
mdb.models['Model-1'].loads['Row2'].setValues(region=region)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Block-2-lin-1-8-lin-2-1-lin-lin-10-1-3'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#10 ]', ), )
s2 = a.instances['Block-2-lin-1-8-lin-2-1-lin-lin-10-1-4'].faces
side1Faces2 = s2.getSequenceFromMask(mask=('[#10 ]', ), )
s3 = a.instances['Block-2-lin-1-8-lin-2-1-lin-lin-10-1-5'].faces
side1Faces3 = s3.getSequenceFromMask(mask=('[#10 ]', ), )
region = regionToolset.Region(side1Faces=side1Faces1+side1Faces2+side1Faces3)
mdb.models['Model-1'].loads['Row3'].setValues(region=region)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.jobs['Job-2'].submit(consistencyChecking=OFF)
#: The job input file "Job-2.inp" has been submitted for analysis.
#: Error in job Job-2: NODE 2 (ASSEMBLY) IS USED AS A REFERENCE NODE FOR MORE THAN ONE RIGID BODY PROPERTY DEFINITION. EACH RIGID BODY PROPERTY DEFINITION MUST HAVE A UNIQUE REFERENCE NODE
#: Error in job Job-2: NODE 2 (ASSEMBLY) IS USED AS A REFERENCE NODE FOR MORE THAN ONE RIGID BODY PROPERTY DEFINITION. EACH RIGID BODY PROPERTY DEFINITION MUST HAVE A UNIQUE REFERENCE NODE
#: Job Job-2: Analysis Input File Processor aborted due to errors.
#: Error in job Job-2: Analysis Input File Processor exited with an error - Please see the  Job-2.dat file for possible error messages if the file exists.
#: Job Job-2 aborted due to errors.
session.viewports['Viewport: 1'].view.setValues(nearPlane=58.9757, 
    farPlane=92.6427, width=33.633, height=12.83, viewOffsetX=10.1159, 
    viewOffsetY=-2.85829)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['DikeRigid-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#20 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['DikeRigid-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#1 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60.4928, 
    farPlane=91.1256, width=13.9023, height=5.05289, viewOffsetX=5.7207, 
    viewOffsetY=-2.65153)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61.868, 
    farPlane=90.5673, width=14.2184, height=5.16776, cameraPosition=(58.6148, 
    19.3408, 57.0793), cameraUpVector=(-0.57735, 0.7803, -0.240413), 
    cameraTarget=(14.8463, 1.11533, -2.07468), viewOffsetX=5.85076, 
    viewOffsetY=-2.71181)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61.8455, 
    farPlane=90.5899, width=14.2132, height=5.1659, viewOffsetX=6.05024, 
    viewOffsetY=-0.818186)
session.viewports['Viewport: 1'].view.setValues(nearPlane=65.5848, 
    farPlane=81.6543, width=15.0726, height=5.47824, cameraPosition=(19.6572, 
    -35.59, 59.3311), cameraUpVector=(-0.272943, 0.946378, 0.17283), 
    cameraTarget=(12.8977, 1.20356, -6.60516), viewOffsetX=6.41605, 
    viewOffsetY=-0.867655)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=66.0062, 
    farPlane=81.2329, width=8.4125, height=3.05758, viewOffsetX=6.63058, 
    viewOffsetY=0.5234)
a = mdb.models['Model-1'].rootAssembly
c1 = a.instances['Block-2-lin-1-8-lin-2-1-lin-lin-10-1-5'].cells
cells1 = c1.getSequenceFromMask(mask=('[#1 ]', ), )
c2 = a.instances['Block-2-lin-1-8-lin-2-1-lin-lin-10-1-4'].cells
cells2 = c2.getSequenceFromMask(mask=('[#1 ]', ), )
c3 = a.instances['Block-2-lin-1-8-lin-2-1-lin-lin-10-1-3'].cells
cells3 = c3.getSequenceFromMask(mask=('[#1 ]', ), )
c4 = a.instances['Block-2-lin-1-6-lin-11-1'].cells
cells4 = c4.getSequenceFromMask(mask=('[#1 ]', ), )
c5 = a.instances['Block-2-lin-1-5-lin-11-1'].cells
cells5 = c5.getSequenceFromMask(mask=('[#1 ]', ), )
c6 = a.instances['Block-2-lin-1-4-lin-11-1'].cells
cells6 = c6.getSequenceFromMask(mask=('[#1 ]', ), )
c7 = a.instances['Block-2-lin-1-3-lin-11-1'].cells
cells7 = c7.getSequenceFromMask(mask=('[#1 ]', ), )
c8 = a.instances['Block-2-lin-1-8-lin-2-1-lin-lin-11-1-3'].cells
cells8 = c8.getSequenceFromMask(mask=('[#1 ]', ), )
c9 = a.instances['Block-2-lin-1-8-lin-2-1-lin-lin-11-1-4'].cells
cells9 = c9.getSequenceFromMask(mask=('[#1 ]', ), )
c10 = a.instances['Block-2-lin-1-8-lin-2-1-lin-lin-11-1-5'].cells
cells10 = c10.getSequenceFromMask(mask=('[#1 ]', ), )
region = regionToolset.Region(cells=cells1+cells2+cells3+cells4+cells5+cells6+\
    cells7+cells8+cells9+cells10)
mdb.models['Model-1'].loads['Gravity'].setValues(distributionType=UNIFORM, 
    field='', region=region)
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=56.9108, 
    farPlane=94.7077, width=59.2929, height=21.5504, viewOffsetX=-1.7198, 
    viewOffsetY=2.04226)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.2839, 
    farPlane=92.3345, width=30.0333, height=10.9158, viewOffsetX=-0.653073, 
    viewOffsetY=-1.99072)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['Wall-1-lin-1-2'].faces
faces1 = f1.getSequenceFromMask(mask=('[#e ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60.2587, 
    farPlane=91.3597, width=17.1969, height=6.25032, viewOffsetX=3.81731, 
    viewOffsetY=-3.01816)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.jobs['Job-2'].submit(consistencyChecking=OFF)
#: The job input file "Job-2.inp" has been submitted for analysis.
#: Error in job Job-2: NODE 2 (ASSEMBLY) IS USED AS A REFERENCE NODE FOR MORE THAN ONE RIGID BODY PROPERTY DEFINITION. EACH RIGID BODY PROPERTY DEFINITION MUST HAVE A UNIQUE REFERENCE NODE
#: Error in job Job-2: NODE 2 (ASSEMBLY) IS USED AS A REFERENCE NODE FOR MORE THAN ONE RIGID BODY PROPERTY DEFINITION. EACH RIGID BODY PROPERTY DEFINITION MUST HAVE A UNIQUE REFERENCE NODE
#: Job Job-2: Analysis Input File Processor aborted due to errors.
#: Error in job Job-2: Analysis Input File Processor exited with an error - Please see the  Job-2.dat file for possible error messages if the file exists.
#: Job Job-2 aborted due to errors.
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.7846, 
    farPlane=91.8338, width=22.3946, height=8.54284, viewOffsetX=-4.95398, 
    viewOffsetY=1.51003)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
a = mdb.models['Model-1'].rootAssembly
a.deleteFeatures(('RP-1', 'RP-2', ))
a = mdb.models['Model-1'].rootAssembly
a.ReferencePoint(point=(0.0, 0.0, 0.0))
a = mdb.models['Model-1'].rootAssembly
a.ReferencePoint(point=(0.0, 0.0, 1.0))
a = mdb.models['Model-1'].rootAssembly
a.ReferencePoint(point=(0.0, 0.0, 2.0))
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[482], )
region1=regionToolset.Region(referencePoints=refPoints1)
mdb.models['Model-1'].constraints['Constraint-1'].setValues(
    refPointRegion=region1)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[483], )
region1=regionToolset.Region(referencePoints=refPoints1)
mdb.models['Model-1'].constraints['Constraint-2'].setValues(
    refPointRegion=region1)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[484], )
region1=regionToolset.Region(referencePoints=refPoints1)
mdb.models['Model-1'].constraints['Constraint-3'].setValues(
    refPointRegion=region1)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[482], )
region = regionToolset.Region(referencePoints=refPoints1)
mdb.models['Model-1'].boundaryConditions['BC-1'].setValues(region=region)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57.0128, 
    farPlane=94.086, width=53.9138, height=19.5953, viewOffsetX=7.81474, 
    viewOffsetY=2.1379)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.jobs['Job-2'].submit(consistencyChecking=OFF)
#: The job input file "Job-2.inp" has been submitted for analysis.
#: Job Job-2: Analysis Input File Processor completed successfully.
#: Error in job Job-2: The rigid bodies with the reference nodes contained in node set ErrNodeRefNodeNoMass have no mass associated with them and some degrees of freedom of the reference node are not restrained. Either mass must be defined or all of the translational degrees of freedom must be constrained. See the status file for further details.
#: Error in job Job-2: The rigid bodies with the reference nodes contained in node set ErrNodeRefNodeNoRot1Axis have atleast one axis about which the rotary inertia magnitude is zero, and the rigid bodies have atleast one rotational degree of freedom which is unconstrained. Either rotary inertia must be defined at the reference nodes or all of the rotational degrees of freedom at the reference nodes must be constrained. See the status file for further details.
#: Job Job-2: Abaqus/Explicit Packager aborted due to errors.
#: Error in job Job-2: Abaqus/Explicit Packager exited with an error - Please see the  status file for possible error messages if the file exists.
#: Job Job-2 aborted due to errors.
o3 = session.openOdb(name='D:/tpennock/9-Block Flume/Job-2.odb')
#: Model: D:/tpennock/9-Block Flume/Job-2.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     13
#: Number of Meshes:             14
#: Number of Element Sets:       0
#: Number of Node Sets:          5
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60.2381, 
    farPlane=90.8607, width=10.2631, height=3.73019, viewOffsetX=-6.67342, 
    viewOffsetY=1.53688)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[482], r1[483], r1[484], )
region = regionToolset.Region(referencePoints=refPoints1)
mdb.models['Model-1'].boundaryConditions['BC-1'].setValues(region=region)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.jobs['Job-2'].submit(consistencyChecking=OFF)
#: The job input file "Job-2.inp" has been submitted for analysis.
#: Job Job-2: Analysis Input File Processor completed successfully.
#: Job Job-2: Abaqus/Explicit Packager completed successfully.
#: Error in job Job-2: The elements contained in element set ErrElemExcessDistortion-Step1 have distorted excessively.
#: Error in job Job-2: Print-out suppressed for subsequent distorted elements
#: Error in job Job-2: There are a total of 470 excessively distorted elements
#: Error in job Job-2: The ratio of deformation speed to wave speed exceeds 1.0000 in at least one element. This usually indicates an error with the model definition. Additional diagnostic information may be found in the message file.
#: Error in job Job-2: The elements contained in element set ErrElemExcessDistortion-Step1 have distorted excessively.
#: Job Job-2: Abaqus/Explicit aborted due to errors.
#: Error in job Job-2: Abaqus/Explicit Analysis exited with an error - Please see the  status file for possible error messages if the file exists.
#: Job Job-2 aborted due to errors.
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['D:/tpennock/9-Block Flume/Job-2.odb'])
o3 = session.openOdb(name='D:/tpennock/9-Block Flume/Job-2.odb')
#: Model: D:/tpennock/9-Block Flume/Job-2.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     13
#: Number of Meshes:             14
#: Number of Element Sets:       4
#: Number of Node Sets:          8
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(name='D:/tpennock/9-Block Flume/Job-2.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF, adaptiveMeshConstraints=ON)
mdb.models['Model-1'].ExplicitDynamicsStep(name='Gravity', previous='Initial', 
    improvedDtMethod=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Gravity')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Loading')
del mdb.models['Model-1'].loads['Gravity']
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Gravity')
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.5805, 
    farPlane=91.5183, width=18.9424, height=6.88475, viewOffsetX=3.26322, 
    viewOffsetY=-2.65958)
a = mdb.models['Model-1'].rootAssembly
c1 = a.instances['Block-2-lin-1-8-lin-2-1-lin-lin-10-1-5'].cells
cells1 = c1.getSequenceFromMask(mask=('[#1 ]', ), )
c2 = a.instances['Block-2-lin-1-8-lin-2-1-lin-lin-10-1-4'].cells
cells2 = c2.getSequenceFromMask(mask=('[#1 ]', ), )
c3 = a.instances['Block-2-lin-1-8-lin-2-1-lin-lin-10-1-3'].cells
cells3 = c3.getSequenceFromMask(mask=('[#1 ]', ), )
c4 = a.instances['Block-2-lin-1-3-lin-11-1'].cells
cells4 = c4.getSequenceFromMask(mask=('[#1 ]', ), )
c5 = a.instances['Block-2-lin-1-4-lin-11-1'].cells
cells5 = c5.getSequenceFromMask(mask=('[#1 ]', ), )
c6 = a.instances['Block-2-lin-1-5-lin-11-1'].cells
cells6 = c6.getSequenceFromMask(mask=('[#1 ]', ), )
c7 = a.instances['Block-2-lin-1-6-lin-11-1'].cells
cells7 = c7.getSequenceFromMask(mask=('[#1 ]', ), )
c8 = a.instances['Block-2-lin-1-8-lin-2-1-lin-lin-11-1-5'].cells
cells8 = c8.getSequenceFromMask(mask=('[#1 ]', ), )
c9 = a.instances['Block-2-lin-1-8-lin-2-1-lin-lin-11-1-4'].cells
cells9 = c9.getSequenceFromMask(mask=('[#1 ]', ), )
c10 = a.instances['Block-2-lin-1-8-lin-2-1-lin-lin-11-1-3'].cells
cells10 = c10.getSequenceFromMask(mask=('[#1 ]', ), )
region = regionToolset.Region(cells=cells1+cells2+cells3+cells4+cells5+cells6+\
    cells7+cells8+cells9+cells10)
mdb.models['Model-1'].Gravity(name='Gravity', createStepName='Gravity', 
    comp2=-9.81, distributionType=UNIFORM, field='', region=region)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.jobs['Job-2'].submit(consistencyChecking=OFF)
#: The job input file "Job-2.inp" has been submitted for analysis.
#: Job Job-2: Analysis Input File Processor completed successfully.
#: Error in job Job-2: The rigid bodies with the reference nodes contained in node set ErrNodeRefNodeNoMass have no mass associated with them and some degrees of freedom of the reference node are not restrained. Either mass must be defined or all of the translational degrees of freedom must be constrained. See the status file for further details.
#: Error in job Job-2: The rigid bodies with the reference nodes contained in node set ErrNodeRefNodeNoRot1Axis have atleast one axis about which the rotary inertia magnitude is zero, and the rigid bodies have atleast one rotational degree of freedom which is unconstrained. Either rotary inertia must be defined at the reference nodes or all of the rotational degrees of freedom at the reference nodes must be constrained. See the status file for further details.
#: Job Job-2: Abaqus/Explicit Packager aborted due to errors.
#: Error in job Job-2: Abaqus/Explicit Packager exited with an error - Please see the  status file for possible error messages if the file exists.
#: Job Job-2 aborted due to errors.
session.viewports['Viewport: 1'].view.setValues(nearPlane=270.674, 
    farPlane=301.534, width=12.0704, height=4.60449, cameraPosition=(180.179, 
    168.498, 162.42), viewOffsetX=-9.59346, viewOffsetY=2.07391)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Loading')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=270.3, 
    farPlane=301.908, width=16.3972, height=5.95969, viewOffsetX=-8.34231, 
    viewOffsetY=2.2226)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Gravity')
mdb.models['Model-1'].FieldOutputRequest(name='F-Output-2', 
    createStepName='Gravity', variables=PRESELECT)
mdb.models['Model-1'].HistoryOutputRequest(name='H-Output-2', 
    createStepName='Gravity', variables=PRESELECT)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
mdb.jobs['Job-2'].submit(consistencyChecking=OFF)
#: The job input file "Job-2.inp" has been submitted for analysis.
#: Job Job-2: Analysis Input File Processor completed successfully.
#: Error in job Job-2: The rigid bodies with the reference nodes contained in node set ErrNodeRefNodeNoMass have no mass associated with them and some degrees of freedom of the reference node are not restrained. Either mass must be defined or all of the translational degrees of freedom must be constrained. See the status file for further details.
#: Error in job Job-2: The rigid bodies with the reference nodes contained in node set ErrNodeRefNodeNoRot1Axis have atleast one axis about which the rotary inertia magnitude is zero, and the rigid bodies have atleast one rotational degree of freedom which is unconstrained. Either rotary inertia must be defined at the reference nodes or all of the rotational degrees of freedom at the reference nodes must be constrained. See the status file for further details.
#: Job Job-2: Abaqus/Explicit Packager aborted due to errors.
#: Error in job Job-2: Abaqus/Explicit Packager exited with an error - Please see the  status file for possible error messages if the file exists.
#: Job Job-2 aborted due to errors.
session.viewports['Viewport: 1'].view.setValues(nearPlane=268.646, 
    farPlane=303.563, width=37.3539, height=14.2493, viewOffsetX=1.23894, 
    viewOffsetY=3.88275)
session.viewports['Viewport: 1'].view.setValues(nearPlane=267.881, 
    farPlane=304.327, width=48.1277, height=17.4923, viewOffsetX=5.49915, 
    viewOffsetY=5.37568)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Loading')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=265.878, 
    farPlane=306.33, width=72.7249, height=26.4324, viewOffsetX=14.4976, 
    viewOffsetY=6.41354)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=270.962, 
    farPlane=301.246, width=7.78425, height=2.82924, viewOffsetX=-9.84872, 
    viewOffsetY=2.30646)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[482], r1[483], r1[484], )
region = regionToolset.Region(referencePoints=refPoints1)
mdb.models['Model-1'].DisplacementBC(name='BC-2', createStepName='Loading', 
    region=region, u1=0.0, u2=0.0, u3=0.0, ur1=0.0, ur2=0.0, ur3=0.0, 
    amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', 
    localCsys=None)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Gravity')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Loading')
del mdb.models['Model-1'].boundaryConditions['BC-1']
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.jobs['Job-2'].submit(consistencyChecking=OFF)
#: The job input file "Job-2.inp" has been submitted for analysis.
#: Job Job-2: Analysis Input File Processor completed successfully.
#: Error in job Job-2: The rigid bodies with the reference nodes contained in node set ErrNodeRefNodeNoMass have no mass associated with them and some degrees of freedom of the reference node are not restrained. Either mass must be defined or all of the translational degrees of freedom must be constrained. See the status file for further details.
#: Error in job Job-2: The rigid bodies with the reference nodes contained in node set ErrNodeRefNodeNoRot1Axis have atleast one axis about which the rotary inertia magnitude is zero, and the rigid bodies have atleast one rotational degree of freedom which is unconstrained. Either rotary inertia must be defined at the reference nodes or all of the rotational degrees of freedom at the reference nodes must be constrained. See the status file for further details.
#: Job Job-2: Abaqus/Explicit Packager aborted due to errors.
#: Error in job Job-2: Abaqus/Explicit Packager exited with an error - Please see the  status file for possible error messages if the file exists.
#: Job Job-2 aborted due to errors.
session.viewports['Viewport: 1'].view.setValues(nearPlane=270.519, 
    farPlane=301.689, width=13.5763, height=5.17892, viewOffsetX=-8.2626, 
    viewOffsetY=2.78121)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
del mdb.models['Model-1'].boundaryConditions['BC-2']
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[482], r1[483], r1[484], )
region = regionToolset.Region(referencePoints=refPoints1)
mdb.models['Model-1'].DisplacementBC(name='BC-1', createStepName='Initial', 
    region=region, u1=SET, u2=SET, u3=SET, ur1=SET, ur2=SET, ur3=SET, 
    amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.jobs['Job-2'].submit(consistencyChecking=OFF)
#: The job input file "Job-2.inp" has been submitted for analysis.
#: Job Job-2: Analysis Input File Processor completed successfully.
#: Job Job-2: Abaqus/Explicit Packager completed successfully.
#: Error in job Job-2: The elements contained in element set ErrElemExcessDistortion-Step2 have distorted excessively.
#: Error in job Job-2: Print-out suppressed for subsequent distorted elements
#: Error in job Job-2: There are a total of 470 excessively distorted elements
#: Error in job Job-2: The ratio of deformation speed to wave speed exceeds 1.0000 in at least one element. This usually indicates an error with the model definition. Additional diagnostic information may be found in the message file.
#: Error in job Job-2: The elements contained in element set ErrElemExcessDistortion-Step2 have distorted excessively.
#: Job Job-2: Abaqus/Explicit aborted due to errors.
#: Error in job Job-2: Abaqus/Explicit Analysis exited with an error - Please see the  status file for possible error messages if the file exists.
#: Job Job-2 aborted due to errors.
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['D:/tpennock/9-Block Flume/Job-2.odb'])
o3 = session.openOdb(name='D:/tpennock/9-Block Flume/Job-2.odb')
#: Model: D:/tpennock/9-Block Flume/Job-2.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     13
#: Number of Meshes:             14
#: Number of Element Sets:       4
#: Number of Node Sets:          8
#: Number of Steps:              2
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].view.setValues(nearPlane=50.0707, 
    farPlane=80.841, width=29.7011, height=10.7951, viewOffsetX=2.97994, 
    viewOffsetY=-0.182601)
session.viewports['Viewport: 1'].view.setValues(session.views['Back'])
session.viewports['Viewport: 1'].view.setValues(session.views['Top'])
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].view.setValues(nearPlane=141.053, 
    farPlane=190.099, width=39.3784, height=14.3124, viewOffsetX=-0.101247, 
    viewOffsetY=-2.61271)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.animationOptions.setValues(frameRate=1)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].view.setValues(nearPlane=150.261, 
    farPlane=165.53, width=37.2979, height=13.5562, viewOffsetX=0.591434, 
    viewOffsetY=-3.23032)
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=49.7003, 
    farPlane=81.952, width=36.8094, height=13.3786, viewOffsetX=3.36691, 
    viewOffsetY=0.558044)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51.7316, 
    farPlane=85.3847, width=38.3139, height=13.9254, cameraPosition=(70.8749, 
    40.5557, 3.76541), cameraUpVector=(-0.812339, 0.57735, -0.0822882), 
    cameraTarget=(17.4017, 2.55091, -1.6513), viewOffsetX=3.50452, 
    viewOffsetY=0.580852)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50.3628, 
    farPlane=86.7536, width=59.2714, height=21.5426, viewOffsetX=9.75738, 
    viewOffsetY=-4.03381)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].view.setValues(nearPlane=53.172, 
    farPlane=83.9444, width=16.8261, height=6.11558, viewOffsetX=3.31153, 
    viewOffsetY=-2.03095)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Loading')
session.viewports['Viewport: 1'].view.setValues(nearPlane=270.432, 
    farPlane=301.776, width=14.5456, height=5.28672, viewOffsetX=5.10058, 
    viewOffsetY=-2.83764)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
mdb.models['Model-1'].ContactExp(name='Int-2', createStepName='Initial')
mdb.models['Model-1'].interactions['Int-2'].includedPairs.setValuesInStep(
    stepName='Initial', useAllstar=ON)
mdb.models['Model-1'].interactions['Int-2'].contactPropertyAssignments.appendInStep(
    stepName='Initial', assignments=((GLOBAL, SELF, ''), ))
#: The interaction "Int-2" has been created.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Loading')
del mdb.models['Model-1'].interactions['Int-1']
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
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
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['D:/tpennock/9-Block Flume/Job-2.odb'])
o3 = session.openOdb(name='D:/tpennock/9-Block Flume/Job-2.odb')
#: Model: D:/tpennock/9-Block Flume/Job-2.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     13
#: Number of Meshes:             14
#: Number of Element Sets:       4
#: Number of Node Sets:          8
#: Number of Steps:              2
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].view.setValues(nearPlane=48.1648, 
    farPlane=83.5432, width=47.9854, height=17.4406, cameraPosition=(67.9707, 
    40.3687, -5.13131), cameraUpVector=(-0.815653, 0.57735, 0.0371094), 
    cameraTarget=(14.5814, 2.57775, -2.70228))
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51.2961, 
    farPlane=80.4114, width=8.34221, height=3.03203, viewOffsetX=-0.301698, 
    viewOffsetY=-2.64428)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50.8427, 
    farPlane=80.8649, width=14.5845, height=5.30083, viewOffsetX=1.40162, 
    viewOffsetY=-3.54002)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Gravity')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF, adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
mdb.save()
#: The model database has been saved to "D:\tpennock\9-Block Flume\First delta flume.cae".
