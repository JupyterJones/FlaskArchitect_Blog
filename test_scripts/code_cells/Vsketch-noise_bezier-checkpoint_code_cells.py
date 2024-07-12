import vsketch

vsk = vsketch.Vsketch()
vsk.size("a4")
vsk.scale("1cm")

NUM = 200
FREQ = 0.003
SPEED = 0.06

for i in range(NUM):
    t = i * FREQ
    v = i * SPEED
    vsk.bezier(
        vsk.noise(t, 0) * 10 + v,
        vsk.noise(t, 1000) * 10 + v,
        vsk.noise(t, 2000) * 10 + v,
        vsk.noise(t, 3000) * 10 + v,
        vsk.noise(t, 4000) * 10 + v,
        vsk.noise(t, 5000) * 10 + v,
        vsk.noise(t, 6000) * 10 + v,
        vsk.noise(t, 7000) * 10 + v,
    )

vsk.display()



