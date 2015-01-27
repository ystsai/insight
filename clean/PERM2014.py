import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

file14 = pd.read_csv("perm_raw/txtfile/Disclosure_Data_Complete_FY14.txt")

# function to convert salary amount to annual salary
def calcSalary(dfrow):
    time = dfrow['PW_UNIT_OF_PAY_9089']
    multi = 1.0
    if (time == 'Year'):
        multi = 1.0
    elif (time == 'Month'):
        multi = 12.0
    elif (time == 'Bi-Weekly'):
        multi = 26.0
    elif (time == 'Week'):
        multi = 52.0
    elif (time == 'Hour'):
        multi = 8.0 * 5.0 * 52.0
    return dfrow['PW_AMOUNT_9089'] * multi 

# apply function
file14.apply(calcSalary, axis=1)

# make DataFrame
awage = pd.DataFrame(file14.apply(calcSalary, axis=1), index=np.arange(70998), columns=['Annual_Wage'])

# add to current DataFrame
file14a = pd.concat([file14, awage], axis=1)

# function to convert status to 0 or 1
# certified, certified-expired = 1
# otherwise (denied, withdrawl) = 0
def numericalStat(dfrow):
    statname = dfrow['Case_Status']
    status = 0
    if (statname == 'Certified'):
        status = 1
    elif (statname == 'Certified-Expired'):
        status = 1
    return status

# apply function
file14a.apply(numericalStat, axis=1)

# make DataFrame
nstatus = pd.DataFrame(file14a.apply(numericalStat, axis=1), index=np.arange(70998), columns=['Certified'])

# add to current DataFrame
file14n = pd.concat([file14a, nstatus], axis=1)

# save DataFrame as csv file
#file14n.to_csv('perm2014_added.csv')

# only extract applications from H-1B visas
# only extract status of certified, certified-expired, denied
fileh1b = file14n[file14['Class_of_Admission']=='H-1B'][(file14['Case_Status']=='Certified') | (file14['Case_Status']=='Certified-Expired') | (file14['Case_Status']=='Denied')]

# save DataFrame to csv file
#fileh1b.to_csv('perm_frm_h1b_2014.csv')
