import pandas as pd
import numpy as np
import pymysql as mdb

file14 = pd.read_csv("permCASC.csv")

con = mdb.connect('localhost', 'root', '', 'permcasc') # host, user, pswd, database

with con:

  cur = con.cursor()
  cur.execute("DROP TABLE IF EXISTS indiv")
  cur.execute("CREATE TABLE indiv (name VARCHAR(225), country VARCHAR(225), \
     job VARCHAR(225), total VARCHAR(25), icert VARCHAR(25), \
     picert VARCHAR(25), iden VARCHAR(25), piden VARCHAR(25))")

  # calculate total, cert, denied, percentage of each
  for a in file14['Employer_Name'].value_counts().index:
     aa = file14[file14['Employer_Name']==a]
     for b in aa['Country_of_Citizenship'].value_counts().index:
        bb = aa[aa['Country_of_Citizenship']==b]
        for c in bb['PW_Job_Title_9089'].value_counts().index:
            cc = bb[bb['PW_Job_Title_9089']==c]
            icert = len(cc[cc['Certified']==1])
            iden = len(cc[cc['Certified']==0])
            itot = len(cc)
            picert = 100. * icert / itot
            piden = 100. * iden / itot
            #print a + " " + b + " " + c + " " + str(itot) + " " + str(icert) + " " + str(picert) + " " + str(iden) + " " + str(piden)

            cline = "INSERT INTO indiv(name, country, job, total, icert, \
               picert, iden, piden) VALUES('" + a + "','" + b + "','" + c + \
               "'," + \
               str(itot) + "," + str(icert) + "," + str(picert) + "," + \
               str(iden) + "," + str(piden) + ")"
            print cline
            cur.execute(cline)
  cur.close()

