import vsketch

class MySketch(vsketch.SketchClass):
    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size("a4", landscape=False)

    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype("linemerge linesimplify reloop linesort")


if __name__ == "__main__":
    MySketch().display()

class MySketch(vsketch.SketchClass):
    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size("a4", landscape=False)

    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype("linemerge linesimplify reloop linesort")



import vsketch

vsk = vsketch.Vsketch()
vsk.size("a4", landscape=True)
vsk.line(0, 0, 100, 202)
vsk.rect(100, 100, 500, 180)
vsk.circle(2, 2, radius=300)
vsk.triangle(0, 0, 1, 1, 0, 1)

vsk.display()

import vsketch

vsk = vsketch.Vsketch()
vsk.size("a4", landscape=False)
for i in range(0,150,15):
    #vsk.line(0, 0, 100, 202)
    vsk.rect(-150+i, 60+i, 10+i*3, 250+i)
    vsk.circle(200, -200, radius=150+i)
    #vsk.triangle(i, 10+i, 100, 100, 500, 200)
vsk.save("my_file.svg")
vsk.display()

!vsk run examples/quick_draw

!ls 



