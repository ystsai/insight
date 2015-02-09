from flask import render_template, request
from app import app
import pymysql as mdb
import numpy as np


@app.route('/')

@app.route('/index')
def index():
   return render_template("index.html")

@app.route('/other')
def other():
   return render_template("other.html")

@app.route('/input')
def companies_input():
  return render_template("input.html")

@app.route('/output')
def companies_output():
  #pull 'company' from input field and store it
  company = request.args.get('company')

  cstring = "SELECT * FROM comp WHERE name='%s';" % company
  istring = "SELECT * FROM indiv WHERE name='%s';" % company

  db = mdb.connect(user=app.config['DB_USER'], host=app.config['DB_HOST'], passwd=app.config['DB_PASSWORD'], db=app.config['DB_DB'], charset='utf8')

  with db:
    cur = db.cursor()
    cur.execute(cstring)
    company_results = cur.fetchall()
    cur.execute(istring)
    indiv_results = cur.fetchall()
    cur.close()

  ctotal = []
  for result in company_results:
    ctotal.append(dict(name=result[0], tot=result[1], ncert=result[2], \
       pcert=float(result[3]), nden=result[4], \
       pden=float(result[5])))
  cout = ctotal[0]

  itotal = []
  for result in indiv_results:
    itotal.append(dict(name=result[0],country=result[1],job=result[2], \
      tot=result[3], icert=result[4], pcert=float(result[5]), \
      iden=result[6], pden=float(result[7])))  

  if company_results == [] or indiv_results == []:
    return render_template("error.html")
  else: 
    return render_template("output.html", company = company, itotal=itotal, \
        ctotal = ctotal)
