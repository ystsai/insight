import fileinput

for eachline in fileinput.input("list"):
   print "<option>" + eachline.strip("\r\n") + "</option>"
