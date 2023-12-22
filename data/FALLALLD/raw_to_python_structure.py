"""FallAllD files to Python struct
By Majd SALEH 08-April-2020.
Adapt for ALERT project by Krittin Kulrattanaruks 22-Dec-2023"""
import os
from numpy import genfromtxt
import numpy as np
import pandas as pd

oldDir = os.getcwd()
ParentDir = os.getcwd()
FP = ParentDir+"\\FallAllD\\"
os.chdir(FP)

FileNamesAll = os.listdir(FP)
FileNames = []
for F_NAME in FileNamesAll:
    if F_NAME.endswith('_A.dat'):
        FileNames.append(F_NAME)
LL = len(FileNames)

l_SubjectID = []
l_ActivityID = []
l_TrialNo = []
l_Acc = []
l_Gyr = []
l_Mag = []
l_Bar = []
l_Fall = []

for i in range(LL):
    F_NAME = FileNames[i]
    SubjectID = int(F_NAME[1:3])
    l_SubjectID.append(np.uint8(SubjectID))
    ActivityID = int(F_NAME[8:11])
    l_ActivityID.append(np.uint8(ActivityID))
    if ActivityID > 100:
        l_Fall.append(np.uint8(1))
    else:
        l_Fall.append(np.uint8(0))
    TrialNo = int(F_NAME[13:15])
    l_TrialNo.append(np.uint8(TrialNo))
    if int(F_NAME[5]) != 2:  # if only device on wrist
        continue

    l_Acc.append(np.int16(genfromtxt(F_NAME, delimiter=',')))
    chArr = list(F_NAME)
    chArr[16] = 'G'
    F_NAME = "".join(chArr)
    l_Gyr.append(np.int16(genfromtxt(F_NAME, delimiter=',')))
    chArr = list(F_NAME)
    chArr[16] = 'M'
    F_NAME = "".join(chArr)
    l_Mag.append(np.int16(genfromtxt(F_NAME, delimiter=',')))
    chArr = list(F_NAME)
    chArr[16] = 'B'
    F_NAME = "".join(chArr)
    l_Bar.append(genfromtxt(F_NAME, delimiter=','))
    print(f'File  {i+1}  out of {len(FileNames)}')
os.chdir(oldDir)


FallAllD = pd.DataFrame(list(zip(l_SubjectID, l_ActivityID, l_Fall,
                                 l_TrialNo, l_Acc, l_Gyr, l_Mag, l_Bar)),
                        columns=['SubjectID', 'ActivityID', 'Fall',
                                 'TrialNo', 'Acc', 'Gyr', 'Mag', 'Bar'])

FallAllD.to_pickle('FallAllD.pkl')
# FallAllD.to_hdf('FallAllD.h5', key='df', mode='w')
# to import data use:
# FallAllD = pd.read_pickle('FallAllD.pkl')
# FallAllD = pd.read_hdf('FallAllD.h5', 'df')
