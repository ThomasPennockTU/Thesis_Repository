# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2023 replay file
# Internal Version: 2023_03_20-20.15.03 RELr425 183417
# Run by tpennock on Tue May 27 10:29:29 2025
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
#: The model database "D:\tpennock\GitHub\Thesis_Repository\1.0-First delta flume no forces w spacers\First delta flume.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['Block']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.6339, 
    farPlane=92.7801, width=27.2009, height=9.44891, viewOffsetX=4.71613, 
    viewOffsetY=0.5465)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
#: Abaqus Error: Detected lock file Job-1.lck. Please confirm that no other applications are attempting to write to the output database associated with this job before removing the lock file and resubmitting.
#: Abaqus/Analysis exited with error(s).
#: The job input file "Job-1.inp" has been submitted for analysis.
mdb.save()
#: The model database has been saved to "D:\tpennock\GitHub\Thesis_Repository\1.0-First delta flume no forces w spacers\First delta flume.cae".
