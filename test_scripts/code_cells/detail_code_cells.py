import math

import numpy as np

import vsketch

vsk = vsketch.Vsketch()
vsk.size("a5", landscape=True)
vsk.scale("1cm")

# high level of detail
vsk.detail("0.1mm")
vsk.circle(0, 0, 1)
vsk.circle(0, 0, 2)
with vsk.pushMatrix():
    vsk.scale(4)
    vsk.circle(0, 0, 1)

# rough level of detail
vsk.translate(7, 0)
vsk.detail("5mm")
vsk.circle(0, 0, 1)
vsk.circle(0, 0, 2)
with vsk.pushMatrix():
    vsk.scale(4)
    vsk.circle(0, 0, 1)

# hardly usable level of detail
vsk.translate(7, 0)
vsk.detail("2cm")
vsk.circle(0, 0, 1)
vsk.circle(0, 0, 2)
with vsk.pushMatrix():
    vsk.scale(4)
    vsk.circle(0, 0, 1)

vsk.display(mode="matplotlib")
vsk.save("detail.svg")

