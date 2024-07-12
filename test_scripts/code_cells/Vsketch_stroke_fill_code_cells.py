from shapely.affinity import translate
from shapely.geometry import Polygon

import vsketch

vsk = vsketch.Vsketch()
vsk.size("a4", landscape=True)
vsk.scale("1cm")
vsk.penWidth("0.5mm")

p = translate(
    Polygon(
        [(-3, -1), (1.5, -2), (1.4, 2), (0, 1.5), (-1, 2.3)],
        holes=[[(-0.5, -0.5), (0.5, -0.5), (0.5, 0.5), (-0.5, 0.5)]],
    ),
    2.5,
    14,
)

# the default is no fill and stroke to layer 1
vsk.square(0, 0, 4)
vsk.circle(2, 8, 4)
vsk.geometry(p)

vsk.translate(7, 0)

# add some fill to layer 2
vsk.fill(2)
vsk.penWidth("1mm", 2)
vsk.square(0, 0, 4)
vsk.circle(2, 8, 4)
vsk.geometry(p)

vsk.translate(7, 0)

# with thick strock
vsk.fill(2)
vsk.penWidth("1mm", 2)
vsk.strokeWeight(4)
vsk.square(0, 0, 4)
vsk.circle(2, 8, 4)
vsk.geometry(p)

vsk.translate(7, 0)

# remove stroke and set fill to layer 3 with a thicker pen
vsk.fill(3)
vsk.penWidth("2mm", 3)
vsk.noStroke()
vsk.square(0, 0, 4)
vsk.circle(2, 8, 4)
vsk.geometry(p)


vsk.display(fig_size=(12, 8))
vsk.save("stroke_fill.svg")



