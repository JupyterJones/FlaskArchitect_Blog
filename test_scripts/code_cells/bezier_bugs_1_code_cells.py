# Pedro Alcocer
# http://art.pedroalcocer.com

import numpy as np

import vsketch


def bug(x, y):
    ts = [682, 268, 624, 98]
    xy_max = 143.25

    for _ in range(0, 150, 12):
        random = vsk.random(1)
        ts = [t * random + 0.24 for t in ts]

        x1 = np.interp(vsk.noise(ts[0]), [-1, 1], [0, xy_max])
        y1 = np.interp(vsk.noise(ts[1]), [-1, 1], [0, xy_max])
        x2 = np.interp(vsk.noise(ts[2]), [-1, 1], [0, xy_max])
        y2 = np.interp(vsk.noise(ts[3]), [-1, 1], [0, xy_max])
        x3 = np.interp(vsk.noise(ts[3]), [-1, 1], [0, xy_max])
        y3 = np.interp(vsk.noise(ts[2]), [-1, 1], [0, xy_max])
        x4 = np.interp(vsk.noise(ts[1]), [-1, 1], [0, xy_max])
        y4 = np.interp(vsk.noise(ts[0]), [-1, 1], [0, xy_max])

        with vsk.pushMatrix():
            vsk.translate(x, y)
            vsk.rotate(45, degrees=True)
            vsk.bezier(x1, y1, x2, y2, x3, y3, x4, y4)


vsk = vsketch.Vsketch()
vsk.size("10in", "10in")

for row in range(7):
    for col in range(7):
        x = col * 100.5
        y = row * 100.5
        bug(x, y)

vsk.display(fig_size=(12, 12))
vsk.save("bezier_bugs3.svg")#, color_mode="none")



