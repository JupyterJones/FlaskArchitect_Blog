import numpy as np

import vsketch

vsk = vsketch.Vsketch()
vsk.size("a4", landscape=True)
vsk.scale("4mm")

phase = -np.pi / 2
for i in range(20):
    angles = np.linspace(0, 2 * np.pi, i + 4)
    vsk.polygon((i + 1) * np.cos(angles + phase), (i + 1) * np.sin(angles + phase))

vsk.display(mode="matplotlib")
vsk.save("polygons.svg")

