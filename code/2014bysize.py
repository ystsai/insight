import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import string

def rmpunct(ap):
  for a in string.punctuation:
    ap = ap.replace(a,"")
  return ap

def calcSalary(pay, time):
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
    return time * multi 

file14 = pd.read_csv("perm_from_h1b_2014.csv")
file13 = pd.read_csv("perm_from_h1b_2013.csv")
file12 = pd.read_csv("perm_from_h1b_2012.csv")


# small = < 500
# medium = 500 - 1000
# large = > 1000

# set sizes
cname = ['INTEL CORPORATION','NVIDIA CORPORATION','MARVELL SEMICONDUCTOR INC','ARISTA NETWORKS, INC.',          'APPLIED MATERIALS, INC.','ALPHA NET CONSULTING LLC.','OMNIVISION TECHNOLOGIES, INC.','BODHTREE SOLUTIONS, INC',          'MCAFEE INC.','SERVICENOW, INC.','HITACHI DATA SYSTEMS CORPORATION','KRYPT INC','PALO ALTO NETWORKS, INC.',          'SERENE CORPORATION','CHEGG, INC.','PERSISTENT SYSTEMS INC.','GS SOFT INC','AGILENT TECHNOLOGIES, INC.',          'NANOSEMANTICS INC.','SOFT MACHINES, INC.','INNOVATE SOLUTIONS INC','SILVER PEAK','KNO INC.','EMBRANE',          'INTEL MEDIA, INC','CALSOFT LABS INC','AERIS COMMUNICATIONS, INC.','CIGNEX DATAMATICS, INC.','INFOOBJECTS, INC.',          'SILVACO INC.','AFFYMETRIX, INC','VERSA NETWORKS, INC','COHERENT, INC','ACNOVATE CORPORATION',          'GLOBALFOUNDRIES U.S. INC.','ELECTRONIC COOLING SOLUTIONS, INC.','GIGAMON, INC.',          'MASTERMIND EDUCATIONAL SERVICES INC.', 'ROVI CORPORATION','STMICROELECTRONICS, INC.', 'INFOSTRETCH CORPORATION',          'TRANSNATIVE ASSOCIATES, INC', 'YV TECHNOLOGIES INC', 'TAVANT TECHNOLOGIES INC', 'QUANTA LABORATORIES',          'INFOBLOX', 'DIGIA USA INC', 'BIG SWITCH NETWORKS', 'IRISLOGIC INC', 'V2SOLUTIONS INC.', 'EVANS ANALYTICAL GROUP',          'DYNAMIC ACCESS SYSTEMS, INC', 'ACROPETAL, INC.', 'LUMENDATA, INC.', 'ZENVERGE, INC.', 'SAVARI INC',          'PELICAN IMAGING CORPORATION', 'TELLUS SOLUTIONS INC.', 'OMEGA SOLUTIONS INC', 'NSIGHT, INC', 'SURIYA SYSTEMS INC',         'TRIANZ', 'FILEMAKER INC.', 'NOR1', 'CHANGYOU.COM (US) LLC', 'FOVEON, INC.', 'MARSTEK SOLUTIONS, LLC',          'MIPS TECHNOLOGIES', 'INTEGRAL SOLUTIONS INT\'L', 'FUJIFILM DIMATIX, INC.', 'WINCERE INC.', 'COOKING PAPA, INC.',          'LEEYO SOFTWARE, INC.', 'INTEL FEDERAL, INC.', 'ALPINE ELECTRONICS OF SILICON VALLEY, INC.', 'TRANSLATTICE INC.',          'THE LAXMI GROUP INC.', 'ATOPTECH, INC.', 'DROISYS INC', 'NEXTBIO', 'Malhar, Inc.', 'PROCESS GLOBAL INC',         'CONTINUUM ELECTRO-OPTICS, INC.', 'NEXENTA SYSTEMS, INC', 'THATONE COMPANY', 'ACCEL NORTH AMERICA INC',          'LUMASENSE TECHNOLOGIES, INC.', 'CRYSTALFISH INC', 'AB OVO, INC.', 'MICROPOINT BIOSCIENCE,INC.',          'ENSPHERE SOLUTIONS, INC.', 'NANGATE', 'CLIQR TECHNOLOGIES, INC.']
csize = ['large','large','large','medium','large','small','large','medium','large','large','large','small','large','small',         'medium','small','small','large','small','small','small','small','small','small','small', 'large', 'small',          'medium','small','small','large','small','large','small','large','small','small','small','large','small', 'small',          'small', 'small', 'large', 'small', 'medium', 'small', 'small', 'medium', 'medium', 'medium', 'small', 'small',          'small', 'large', 'small', 'small', 'small', 'small', 'small', 'small', 'medium', 'small', 'small', 'small',          'small', 'small', 'large', 'small', 'small', 'small', 'small', 'small', 'small', 'small', 'small', 'small', 'small',         'small', 'small', 'small', 'small', 'small', 'small', 'small', 'small', 'small', 'small', 'small', 'small', 'small',         'small', 'small']


print len(cname)
print len(csize)

# make dataframe of company sizes
cnsize = pd.DataFrame({'name':cname, 'size':csize})

print cnsize[cnsize['size']=='large'].shape
print cnsize[cnsize['size']=='medium'].shape
print cnsize[cnsize['size']=='small'].shape


# calculate tot, cert, denied, and percentages for large company
ltot = 0
lcert = 0
lden = 0
for b in [file14]:
  #print b.columns
  for a in cnsize[cnsize['size']=='large']['name']:
    newa = rmpunct(a)
    #print a
    try:
      aa = b[b['Employer_Name'].apply((lambda x: rmpunct(x)))==newa]
    except KeyError:
      aa = b[b['EMPLOYER_NAME'].apply((lambda x: rmpunct(x)))==newa]
    try:
      lcert = lcert + len(aa[aa['Case_Status']=='Certified']) + len(aa[aa['Case_Status']=='Certified-Expired'])
    except KeyError:
      lcert = lcert + len(aa[aa['CASE_STATUS']=='Certified']) + len(aa[aa['CASE_STATUS']=='Certified-Expired'])
    try:
      lden = lden + len(aa[aa['Case_Status']=='Denied'])
    except KeyError:
      lden = lden + len(aa[aa['CASE_STATUS']=='Denied'])
    ltot = ltot + len(aa)
print "large company"
print lcert
print lden
print ltot
plcert = 100. * lcert / ltot
plden = 100. * lden / ltot
print plcert
print plden


# calculate for medium company
mtot = 0
mcert = 0
mden = 0
for b in [file14]:
  for a in cnsize[cnsize['size']=='medium']['name']:
    newa = rmpunct(a)
    #print a
    try:
      aa = b[b['Employer_Name'].apply((lambda x: rmpunct(x)))==newa]
    except KeyError:
      aa = b[b['EMPLOYER_NAME'].apply((lambda x: rmpunct(x)))==newa]
    try:
      mcert = mcert + len(aa[aa['Case_Status']=='Certified']) + len(aa[aa['Case_Status']=='Certified-Expired'])
    except KeyError:
      mcert = mcert + len(aa[aa['CASE_STATUS']=='Certified']) + len(aa[aa['CASE_STATUS']=='Certified-Expired'])
    try:
      mden = mden + len(aa[aa['Case_Status']=='Denied'])
    except KeyError:
      mden = mden + len(aa[aa['CASE_STATUS']=='Denied'])
    mtot = mtot + len(aa)
print "medium size"
pmcert = 100. * mcert / mtot
pmden = 100. * mden / mtot
print mcert
print mden
print mtot
print pmcert
print pmden

#### calculate for small company
stot = 0
scert = 0
sden = 0
for b in [file14]:
  for a in cnsize[cnsize['size']=='small']['name']:
     #print a
     newa = rmpunct(a)
     try:
       aa = b[b['Employer_Name'].apply((lambda x: rmpunct(x)))==newa]
     except KeyError:
       aa = b[b['EMPLOYER_NAME'].apply((lambda x: rmpunct(x)))==newa]
     try:
       scert = scert + len(aa[aa['Case_Status']=='Certified']) + len(aa[aa['Case_Status']=='Certified-Expired'])
     except KeyError:
       scert = scert + len(aa[aa['CASE_STATUS']=='Certified']) + len(aa[aa['CASE_STATUS']=='Certified-Expired'])
     try:
       sden = sden + len(aa[aa['Case_Status']=='Denied'])
     except KeyError:
       sden = sden + len(aa[aa['CASE_STATUS']=='Denied'])
     stot = stot + len(aa)
print "small"
pscert = 100. * scert / stot
psden = 100. * sden / stot
print scert
print sden
print stot
print pscert
print psden


## plot
N = 3
certall = (plcert, pmcert, pscert)
denall = (plden, pmden, psden)

ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

f,(ax,ax2) = plt.subplots(2,1,sharex=True)

#p1 = plt.bar(ind, certall, width, color='mediumseagreen')
#p2 = plt.bar(ind, denall, width, color='white',bottom=certall)

ax.bar(ind, certall, width, color='mediumseagreen')
ax2.bar(ind, certall, width, color='mediumseagreen')

ax.set_ylim(80,100)
ax2.set_ylim(0,20)

ax.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)

ax.xaxis.tick_top()

ax.tick_params(labeltop='off')
ax2.xaxis.tick_bottom()

#plt.ylabel('Percent',fontsize=16)
#plt.title('Percent certified by company size',fontsize=16)

ax.set_title('Percent accepted',fontsize=16)

ax.axhline(y=95)

plt.xticks(ind+width/2., ('Large', 'Medium', 'Small'), fontsize=16)

d = 0.01
kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)
ax.plot((-d,+d),(-d,+d), **kwargs)
ax.plot((1-d,1+d),(-d,+d), **kwargs)

kwargs.update(transform=ax2.transAxes)
ax2.plot((-d,+d),(1-d,1+d), **kwargs)
ax2.plot((1-d,1+d),(1-d,1+d), **kwargs)

#plt.yticks(np.arange(0,101,10), fontsize=16)
#plt.legend( (p1[0], p2[0]), ('Accepted', 'Denied'), fontsize=16, loc='lower right')
plt.show()

#plt.savefig('size.png')

