import os 
os.chdir("/home/jack/Desktop/dockercommands")

import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

x_bounds = np.array([0, 10])
y_bounds = np.array([0, 10])
x_buffer, y_buffer = 1, 1
x_plot = x_bounds + np.array([x_buffer, -x_buffer])
y_plot = y_bounds + np.array([y_buffer, -y_buffer])

num_points = 400

x = np.random.uniform(*x_bounds, size=num_points).reshape((num_points, 1))
y = np.random.uniform(*y_bounds, size=num_points).reshape((num_points, 1))
pts = np.hstack([x, y])

plt.scatter(*pts.transpose(),c = '#000000')
plt.show()

vor = Voronoi(pts)
verts = vor.vertices
shapes_ind = vor.regions

shapes_ind = [s+s[0:1] for s in shapes_ind if len(s)>0 and -1 not in s]
shapes = [verts[s] for s in shapes_ind]
print(len(shapes))

fig, ax = plt.subplots(figsize=(10,10))
ax.set_xlim(*x_plot)
ax.set_ylim(*y_plot)
lc = LineCollection(shapes,colors="#000000")
ax.add_collection(lc)

filled_polygon = shapes

n_fill_lines = 5
min_scalar = 0.1

num_polygons = 120
lst = np.random.randint(low=0, high=len(shapes)-1, size=num_polygons)

for i in lst:
  center = np.mean(shapes[i],axis=0)
  polygon = shapes[i]
  for scaler in np.linspace(min_scalar, 1, num=n_fill_lines, endpoint=False):
      scaled = scaler*(polygon - center) + center
      filled_polygon.append(scaled)
    
    
fig, ax = plt.subplots(figsize=(10,10))
ax.set_xlim(*x_plot)
ax.set_ylim(*y_plot)
lc = LineCollection(filled_polygon,colors="#001220")
ax.add_collection(lc)
plt.show()

fig.savefig('onevid/experiment1.png', bbox_inches = 'tight', pad_inches = 0)

!ls -d */



