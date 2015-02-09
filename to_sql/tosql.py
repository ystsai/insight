import pandas as pd
import numpy as np
import pymysql as mdb

file14 = pd.read_csv("permCASC.csv")

con = mdb.connect('localhost', 'root', '', 'permcasc') # host, user, pswd, database

with con:

  cur = con.cursor()
  cur.execute("DROP TABLE IF EXISTS comp")
  cur.execute("CREATE TABLE comp (name VARCHAR(225), total VARCHAR(25), \
     numcert VARCHAR(25), perccert VARCHAR(25), numden VARCHAR(25), \
     percden VARCHAR(25))")

  # calculate total, cert, denied, percentage of each
  for a in file14['Employer_Name'].value_counts().index:
     aa = file14[file14['Employer_Name']==a]
     cert = len(aa[aa['Certified']==1])
     den = len(aa[aa['Certified']==0])
     tot = len(aa)
     pcert = 100. * cert / tot
     pden = 100. * den / tot

     cline = "INSERT INTO comp(name, total, numcert, perccert, numden, \
        percden) VALUES('" \
        + a + "'," + str(tot) + "," + str(cert) + "," + str(pcert) + "," + \
        str(den) + "," + str(pden) + ")"
     print cline
     cur.execute(cline)

  cur.close()
