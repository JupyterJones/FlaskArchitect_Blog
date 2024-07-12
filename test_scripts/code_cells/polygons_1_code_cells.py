import numpy as np

import vsketch

vsk = vsketch.Vsketch()
vsk.size("a4", landscape=True)
vsk.scale("4mm")

phase = -np.pi / 2
for i in range(20):
    angles = np.linspace(0, 2 * np.pi, i + 4)
    vsk.polygon((i + 1) * np.cos(angles + phase), (i + 1) * np.sin(angles + phase))

vsk.display()#mode="matplotlib")
vsk.save("polygons.svg")

import numpy as np

import vsketch

vsk = vsketch.Vsketch()
vsk.size("a4", landscape=True)
vsk.scale("4mm")

phase = -np.pi / 2
for i in range(50):
    angles = np.linspace(0, 2 * np.pi, i + 3)
    vsk.polygon((i + 1) * np.cos(angles + phase), (i + 1) * np.sin(angles + phase))

vsk.display()#mode="matplotlib")
vsk.save("polygons.svg")

import numpy as np
from random import randint
import vsketch

vsk = vsketch.Vsketch()
vsk.size("a4", landscape=True)
vsk.scale("4mm")
def inc():
    var = randint(0,4)
    return var
phase = -np.pi / 2
for i in range(150):
    angles = np.linspace(0, 2 * np.pi, i + 3)
    vsk.polygon((i + 1) * np.cos(angles-inc() + phase+inc()), (i + 1) * np.sin(angles + phase))

vsk.display()#mode="matplotlib")
vsk.save("polygons.svg")

import numpy as np
from random import randint
import vsketch

vsk = vsketch.Vsketch()
vsk.size(1440,960, landscape=False)
vsk.scale("px")
def inc():
    var = randint(0,4)
    return var
phase = -np.pi / 2
for i in range(0,450,5):
    angles = np.linspace(0, 2 * np.pi, i + 3)
    vsk.polygon((i + 1) * np.cos(angles-inc() + phase+inc()), (i + 1) * np.sin(angles + phase))

vsk.display()#mode="matplotlib")
vsk.save("polygons-px.svg")

import numpy as np
from random import randint
import vsketch

vsk = vsketch.Vsketch()
vsk.size(1440,960, landscape=False)
vsk.scale("px")
def inc():
    var = randint(0,4)
    return var
num_lines = 850
x_coords = np.linspace(0., 250., 1000)
perlin = vsk.noise(x_coords * 0.1, np.linspace(0, 5., num_lines))
for j in range(0,num_lines,20):
    vsk.polygon(x_coords, j + perlin[:, j] * 45)

vsk.display()#mode="matplotlib")
vsk.save("polygons-px.svg")



