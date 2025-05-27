# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2023 replay file
# Internal Version: 2023_03_20-20.15.03 RELr425 183417
# Run by tpennock on Mon May 26 15:45:40 2025
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
session.viewports['Viewport: 1'].view.setValues(nearPlane=57.8551, 
    farPlane=94.5589, width=50.1027, height=17.4044, viewOffsetX=4.03582, 
    viewOffsetY=-1.07032)
mdb.jobs['Job-2'].submit(consistencyChecking=OFF)
#: The job input file "Job-2.inp" has been submitted for analysis.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Loading')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
#: Job Job-2: Analysis Input File Processor completed successfully.
mdb.models['Model-1'].Interaction(name='Int-2', 
    objectToCopy=mdb.models['Model-1'].interactions['Int-1'], 
    toStepName='Initial')
#* The specified type of interaction cannot be created or resumed in this type 
#* of step.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
#: Job Job-2: Abaqus/Explicit Packager completed successfully.
#: Error in job Job-2: The elements contained in element set ErrElemExcessDistortion-Step1 have distorted excessively.
#: Error in job Job-2: Print-out suppressed for subsequent distorted elements
#: Error in job Job-2: There are a total of 8965 excessively distorted elements
#: Error in job Job-2: The ratio of deformation speed to wave speed exceeds 1.0000 in at least one element. This usually indicates an error with the model definition. Additional diagnostic information may be found in the message file.
#: Error in job Job-2: The elements contained in element set ErrElemExcessDistortion-Step1 have distorted excessively.
#: Job Job-2: Abaqus/Explicit aborted due to errors.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Loading')
#: Error in job Job-2: Abaqus/Explicit Analysis exited with an error - Please see the  status file for possible error messages if the file exists.
#: Job Job-2 aborted due to errors.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
mdb.models['Model-1'].ContactExp(name='Int-2', createStepName='Initial')
mdb.models['Model-1'].interactions['Int-2'].includedPairs.setValuesInStep(
    stepName='Initial', useAllstar=ON)
mdb.models['Model-1'].interactions['Int-2'].contactPropertyAssignments.appendInStep(
    stepName='Initial', assignments=((GLOBAL, SELF, 'IntProp-1'), ))
#: The interaction "Int-2" has been created.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Loading')
del mdb.models['Model-1'].interactions['Int-1']
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
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
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=4.04473, 
    viewOffsetY=-1.07269)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
mdb.models['Model-1'].SmoothStepAmplitude(name='Amp-1', timeSpan=STEP, data=((
    0.0, 0.0), (1.0, 1.0)))
mdb.models['Model-1'].loads['Gravity'].setValues(amplitude='Amp-1', 
    distributionType=UNIFORM, field='')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.jobs['Job-2'].submit(consistencyChecking=OFF)
#: The job input file "Job-2.inp" has been submitted for analysis.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
#: Job Job-2: Analysis Input File Processor completed successfully.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
#: Job Job-2: Abaqus/Explicit Packager completed successfully.
#: Error in job Job-2: The elements contained in element set ErrElemExcessDistortion-Step1 have distorted excessively.
#: Error in job Job-2: Print-out suppressed for subsequent distorted elements
#: Error in job Job-2: There are a total of 72 excessively distorted elements
#: Error in job Job-2: The ratio of deformation speed to wave speed exceeds 1.0000 in at least one element. This usually indicates an error with the model definition. Additional diagnostic information may be found in the message file.
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
session.viewports['Viewport: 1'].view.setValues(nearPlane=47.6595, 
    farPlane=83.9776, width=49.6921, height=17.2618, cameraPosition=(67.3354, 
    40.3746, 5.91174), cameraUpVector=(-0.80581, 0.57735, -0.131669), 
    cameraTarget=(14.5812, 2.57702, -2.70827))
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
#: Error in job Job-2: The elements contained in element set ErrElemExcessDistortion-Step1 have distorted excessively.
#: Job Job-2: Abaqus/Explicit aborted due to errors.
#: Error in job Job-2: Abaqus/Explicit Analysis exited with an error - Please see the  status file for possible error messages if the file exists.
#: Job Job-2 aborted due to errors.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.models['Model-1'].steps['Loading'].setValues(
    timeIncrementationMethod=AUTOMATIC_GLOBAL, scaleFactor=1.0, 
    maxIncrement=None, improvedDtMethod=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
mdb.jobs['Job-2'].submit(consistencyChecking=OFF)
#: The job input file "Job-2.inp" has been submitted for analysis.
#: Job Job-2: Analysis Input File Processor completed successfully.
#: Job Job-2: Abaqus/Explicit Packager completed successfully.
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.6181, 
    farPlane=92.7959, width=27.912, height=10.1987, viewOffsetX=5.98169, 
    viewOffsetY=-1.47131)
mdb.save()
#: The model database has been saved to "D:\tpennock\GitHub\Thesis_Repository\1.0-First delta flume no forces\First delta flume.cae".
#: Job Job-2: Abaqus/Explicit completed successfully.
#: Job Job-2 completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['D:/tpennock/GitHub/Thesis_Repository/1.0-First delta flume no forces/Job-2.odb'])
#: Warning: The output database 'D:/tpennock/GitHub/Thesis_Repository/1.0-First delta flume no forces/Job-2.odb' disk file has changed.
#: 
#: The current plot operation has been canceled, re-open the file to view the results
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
mdb.save()
#: The model database has been saved to "D:\tpennock\GitHub\Thesis_Repository\1.0-First delta flume no forces\First delta flume.cae".
