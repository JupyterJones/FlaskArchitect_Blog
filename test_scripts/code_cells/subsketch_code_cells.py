import vsketch

# create a stick figurestick figure
sub = vsketch.Vsketch()
sub.detail(0.01)
sub.rect(0, 0, 1, 2)
sub.circle(0.5, -0.5, 1)
sub.line(0, 0, -0.5, 1)
sub.line(1, 0, 1.5, 1)
sub.line(0, 2, -0.3, 4)
sub.line(1, 2, 1.3, 4)

# use the stick figure
vsk = vsketch.Vsketch()
vsk.size("a4", landscape=True)
vsk.scale("1cm")


for i in range(8):
    with vsk.pushMatrix():
        vsk.scale(0.95 ** i)
        vsk.rotate(8 * i, degrees=True)
        vsk.sketch(sub)
    
    vsk.translate(3, 0)


vsk.display(mode="matplotlib")
vsk.save("subsketch_basic.svg")

vsk = vsketch.Vsketch()

vsk.scale(1.5)
vsk.rect(-5, -5, 10, 10)

for i in range(10):
    vsk.rotate(10, degrees=True)
    vsk.sketch(vsk)
    
vsk.display(mode="matplotlib")
vsk.save("subsketch_recursive.svg")

