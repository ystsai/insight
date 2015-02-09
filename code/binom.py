import numpy as np
import scipy.misc as sc
import scipy.stats as st
from math import sqrt

def se2(p, t):
  return (p*(1-p))/t

def sz(a, b, sa, sb):
  return (b - a) / sqrt(sa + sb)

lmcert = 3074.
lmden = 211.
lmtot = lmcert + lmden

plcert = lmcert / lmtot

smcert = 277.
smden = 27.
smtot = smcert + smden

pscert = smcert / smtot

lse2 = se2(plcert, lmtot)
sse2 = se2(pscert, smtot)

szt = sz(plcert, pscert, lse2, sse2)

print "2012-2014"
print szt
print st.norm.cdf(szt)

lmcert14 = 1456.
lmden14 = 33.
lmtot14 = lmcert14 + lmden14

plcert14 = lmcert14 / lmtot14

smcert14 = 161.
smden14 = 7.
smtot14 = smcert14 + smden14

pscert14 = smcert14 / smtot14

lse14 = se2(plcert14, lmtot14)
sse14 = se2(pscert14, smtot14)

sz14 = sz(plcert14, pscert14, lse14, sse14)

print "2014"
print sz14
print st.norm.cdf(sz14)

lmcert12 = 439.
lmden12 = 465.
lmtot12 = lmcert12 + lmden12
plcert12 = lmcert12 / lmtot12

smcert12 = 59.
smden12 = 11.
smtot12 = smcert12 + smcert12
pscert12 = smcert12 / smtot12

lse12 = se2(plcert12, lmtot12)
sse12 = se2(pscert12, smtot12)
sz12 = sz(plcert12, pscert12, lse12, sse12)

print "2012"
print sz12
print st.norm.cdf(sz12)

lmcert13 = 1179.
lmden13 = 152.
lmtot13 = lmcert13 + lmden13
plcert13 = lmcert13 / lmtot13

smcert13 = 57.
smden13 = 9.
smtot13 = smcert13 + smden13
pscert13 = smcert13 / smtot13

lse13 = se2(plcert13, lmtot13)
sse13 = se2(pscert13, smtot13)
sz13 = sz(plcert13, pscert13, lse13, sse13)

print "2013"
print sz13
print st.norm.cdf(sz13)



