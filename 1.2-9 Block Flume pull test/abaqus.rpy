# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2023 replay file
# Internal Version: 2023_03_20-20.15.03 RELr425 183417
# Run by tpennock on Tue May 20 11:44:23 2025
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
#: The model database "D:\tpennock\1.2-9 Block Flume pull test\First delta flume.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['Block']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.04619, 
    farPlane=1.9713, width=1.8808, height=0.687218, viewOffsetX=0.203331, 
    viewOffsetY=0.0197136)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58.1004, 
    farPlane=94.3136, width=47.8644, height=17.489, viewOffsetX=0.867729, 
    viewOffsetY=-0.141379)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['Wall-1-lin-1-2'].faces
faces1 = f1.getSequenceFromMask(mask=('[#a ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60.382, 
    farPlane=92.032, width=17.3948, height=6.35583, viewOffsetX=2.93703, 
    viewOffsetY=-1.42812)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Loading')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
del mdb.models['Model-1'].loads['Row1']
del mdb.models['Model-1'].loads['Row2']
del mdb.models['Model-1'].loads['Row3']
del mdb.models['Model-1'].amplitudes['Row1']
del mdb.models['Model-1'].amplitudes['Row2']
del mdb.models['Model-1'].amplitudes['Row3']
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
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
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Loading')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Gravity')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Loading')
mdb.models['Model-1'].steps['Loading'].setValues(
    timeIncrementationMethod=AUTOMATIC_GLOBAL, scaleFactor=1.0, 
    maxIncrement=None, improvedDtMethod=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
mdb.jobs['Job-2'].submit(consistencyChecking=OFF)
#: The job input file "Job-2.inp" has been submitted for analysis.
#: Job Job-2: Analysis Input File Processor completed successfully.
#: Job Job-2: Abaqus/Explicit Packager completed successfully.
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p1 = mdb.models['Model-1'].parts['Block']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
session.viewports['Viewport: 1'].setValues(displayedObject=None)
s = mdb.models['Model-1'].ConstrainedSketch(name='__edit__', 
    objectToCopy=mdb.models['Model-1'].sketches['Dike'])
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__edit__']
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p1 = mdb.models['Model-1'].parts['Block']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].parts['Block']
s1 = p.features['Solid extrude-1'].sketch
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=s1)
s2 = mdb.models['Model-1'].sketches['__edit__']
g, v, d, c = s2.geometry, s2.vertices, s2.dimensions, s2.constraints
s2.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s2, 
    upToFeature=p.features['Solid extrude-1'], filter=COPLANAR_EDGES)
#: Job Job-2: Abaqus/Explicit completed successfully.
#: Job Job-2 completed successfully. 
session.viewports['Viewport: 1'].view.setValues(nearPlane=22.747, 
    farPlane=25.9314, width=20.382, height=7.81444, cameraPosition=(5.09297, 
    0.242725, 24.4142), cameraTarget=(5.09297, 0.242725, 0))
s2.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__edit__']
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(name='D:/tpennock/1.2-9 Block Flume pull test/Job-2.odb')
#: Model: D:/tpennock/1.2-9 Block Flume pull test/Job-2.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     13
#: Number of Meshes:             14
#: Number of Element Sets:       0
#: Number of Node Sets:          4
#: Number of Steps:              2
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].view.setValues(nearPlane=50.4958, 
    farPlane=80.4159, width=24.6141, height=8.5503, viewOffsetX=5.26432, 
    viewOffsetY=-0.0701045)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50.4137, 
    farPlane=80.3338, width=24.574, height=8.5364, cameraPosition=(52.6267, 
    40.3687, 34.6921), cameraTarget=(14.8358, 2.57775, -3.09881), 
    viewOffsetX=5.25576, viewOffsetY=-0.0699905)
session.viewports['Viewport: 1'].view.setValues(nearPlane=48.5886, 
    farPlane=82.1589, width=46.6885, height=16.2184, viewOffsetX=3.8729, 
    viewOffsetY=-1.04768)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51.1277, 
    farPlane=86.0808, width=49.1283, height=17.0659, cameraPosition=(71.1383, 
    40.3687, 3.14535), cameraUpVector=(-0.813995, 0.57735, -0.0638589), 
    cameraTarget=(17.8576, 2.57775, -1.03459), viewOffsetX=4.07529, 
    viewOffsetY=-1.10243)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].view.setValues(nearPlane=53.9682, 
    farPlane=83.2411, width=7.64364, height=2.65521, viewOffsetX=1.62338, 
    viewOffsetY=-1.26771)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=HARMONIC)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=SCALE_FACTOR)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='CPRESS     General_Contact_Domain', outputPosition=NODAL, )
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].odbDisplay.setDeformedVariable(
    variableLabel='A', )
session.viewports['Viewport: 1'].view.setValues(nearPlane=16867.2, 
    farPlane=33484.2, width=5.52004, height=1.91752, viewOffsetX=0.845536, 
    viewOffsetY=-1.01636)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='CSHEARMAG  General_Contact_Domain', outputPosition=NODAL, )
session.viewports['Viewport: 1'].view.setValues(nearPlane=21572.4, 
    farPlane=28577.6, width=232.523, height=80.7726, viewOffsetX=36.8949, 
    viewOffsetY=5.79363)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=52.4732, 
    farPlane=84.5082, width=25.5151, height=8.8633, viewOffsetX=1.78248, 
    viewOffsetY=-1.74962)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='A', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61.0383, 
    farPlane=91.3757, width=8.47442, height=3.09644, viewOffsetX=3.14164, 
    viewOffsetY=-1.90208)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Block-2-lin-1-5-lin-11-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#10 ]', ), )
region = regionToolset.Region(side1Faces=side1Faces1)
mdb.models['Model-1'].Pressure(name='pull', createStepName='Loading', 
    region=region, distributionType=UNIFORM, field='', magnitude=13540.0, 
    amplitude=UNSET)
mdb.models['Model-1'].loads['pull'].setValues(magnitude=-13540.0)
mdb.models['Model-1'].SmoothStepAmplitude(name='pull_step', timeSpan=STEP, 
    data=((0.0, 0.0), (12.0, 1.0)))
mdb.models['Model-1'].loads['pull'].setValues(amplitude='pull_step')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
#: The job input file "Job-1.inp" has been submitted for analysis.
#: Job Job-1: Analysis Input File Processor completed successfully.
#: Job Job-1: Abaqus/Explicit Packager completed successfully.
#: Job Job-1: Abaqus/Explicit completed successfully.
#: Job Job-1 completed successfully. 
session.viewports['Viewport: 1'].view.setValues(nearPlane=57.9968, 
    farPlane=94.4172, width=49.9128, height=19.1365, viewOffsetX=10.6556, 
    viewOffsetY=-4.12648)
o3 = session.openOdb(name='D:/tpennock/1.2-9 Block Flume pull test/Job-1.odb')
#: Model: D:/tpennock/1.2-9 Block Flume pull test/Job-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     13
#: Number of Meshes:             14
#: Number of Element Sets:       0
#: Number of Node Sets:          4
#: Number of Steps:              2
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].view.setValues(nearPlane=47.8863, 
    farPlane=83.7783, width=49.9166, height=17.3398, cameraPosition=(67.8841, 
    40.3687, 1.18821), cameraUpVector=(-0.81433, 0.57735, -0.0594367), 
    cameraTarget=(14.5814, 2.57775, -2.70228))
session.viewports['Viewport: 1'].view.setValues(nearPlane=50.0019, 
    farPlane=81.6627, width=24.3098, height=8.44461, viewOffsetX=2.95379, 
    viewOffsetY=-2.12553)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].view.setValues(nearPlane=868.648, 
    farPlane=1334.53, width=14.4616, height=5.02359, viewOffsetX=-19.5407, 
    viewOffsetY=103.596)
session.viewports['Viewport: 1'].view.setValues(nearPlane=868.574, 
    farPlane=1334.37, width=14.4603, height=5.02316, cameraPosition=(1171.47, 
    625.762, 51.6203), cameraTarget=(264.51, -17.261, -14.5775), 
    viewOffsetX=-19.539, viewOffsetY=103.587)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].view.setValues(nearPlane=942.452, 
    farPlane=1343.65, width=15.6903, height=5.45041, cameraPosition=(1196.56, 
    579.078, 6.01359), cameraUpVector=(-0.788207, 0.612098, -0.0637694), 
    cameraTarget=(259.677, -22.8509, -13.3415), viewOffsetX=-21.2009, 
    viewOffsetY=112.398)
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=775.33, 
    farPlane=1127.91, width=83.4015, height=28.9716, viewOffsetX=-102.694, 
    viewOffsetY=66.6881)
session.viewports['Viewport: 1'].view.setValues(nearPlane=748.78, 
    farPlane=1127.49, width=80.5456, height=27.9795, cameraPosition=(844.743, 
    509.447, 465.32), cameraUpVector=(-0.582372, 0.594895, -0.554024), 
    cameraTarget=(216.151, -19.7364, -14.6954), viewOffsetX=-99.1776, 
    viewOffsetY=64.4045)
session.viewports['Viewport: 1'].view.setValues(nearPlane=714.648, 
    farPlane=1122.69, width=76.874, height=26.7041, cameraPosition=(928.032, 
    472.344, 322.9), cameraUpVector=(-0.616346, 0.607392, -0.50119), 
    cameraTarget=(198.52, -31.2557, -23.1883), viewOffsetX=-94.6567, 
    viewOffsetY=61.4687)
session.viewports['Viewport: 1'].view.setValues(nearPlane=711.441, 
    farPlane=1125.9, width=121.48, height=42.1992, viewOffsetX=-89.411, 
    viewOffsetY=59.5783)
session.viewports['Viewport: 1'].view.setValues(session.views['Top'])
session.viewports['Viewport: 1'].view.setValues(session.views['Back'])
session.viewports['Viewport: 1'].view.setValues(session.views['Top'])
session.viewports['Viewport: 1'].view.setValues(session.views['Bottom'])
session.viewports['Viewport: 1'].view.setValues(session.views['Left'])
session.viewports['Viewport: 1'].view.setValues(session.views['Right'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=658.188, 
    farPlane=1074.22, width=4.25651, height=1.4786, viewOffsetX=0.294744, 
    viewOffsetY=-0.593875)
session.animationOptions.setValues(frameRate=5)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60.4165, 
    farPlane=91.9975, width=16.9193, height=6.18208, viewOffsetX=6.6416, 
    viewOffsetY=-2.58141)
mdb.save()
#: The model database has been saved to "D:\tpennock\1.2-9 Block Flume pull test\First delta flume.cae".
