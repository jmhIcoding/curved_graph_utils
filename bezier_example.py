__author__ = 'jmh081701'
import matplotlib.pyplot as plt
import numpy as np
import bezier
from matplotlib.collections import LineCollection
nodes = np.asfortranarray([
    [5.0,6.0,7.0,7.0,5.0,5.0,5.0],
    [5.0,5.0,5.0,7.0,7.0,6.0,5.0]])
curve = bezier.Curve(nodes, degree=6)
s_vals = np.linspace(0.0, 1.0, 30)
data=curve.evaluate_multi(s_vals)
x33=data[0]
y33=data[1]

segments = []
for index in range(0,len(x33)):
    segments.append([x33[index],y33[index]])
segments = [segments]
print(np.array(segments).shape)

lc = LineCollection(segments,linewidths=2)
ax = plt.axes()
ax.add_collection(lc)
ax.autoscale_view()
plt.show()
