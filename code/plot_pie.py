#!/usr/local/bin/python
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['font.size'] = 16.0

labels = ['Accepted', 'Denied']

cert14 = 29416 + 22299
denied14 = 2712

cert13 = 17756 + 11389
denied13 = 3789

cert12 = 44529 + 1
denied12 = 5185

res = [cert14, denied14]

plt.pie(res, labels=labels, colors=['mediumseagreen', 'white'], autopct='%1.1f%%')
plt.axis('equal')
plt.title('2014 data')
plt.show()
