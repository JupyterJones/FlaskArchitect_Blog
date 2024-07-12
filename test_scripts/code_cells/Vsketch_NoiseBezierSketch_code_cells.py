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

!vsk run ../quick_draw

import vsketch


class SchotterSketch(vsketch.SketchClass):
    columns = vsketch.Param(12)
    rows = vsketch.Param(22)
    fuzziness = vsketch.Param(1.0)

    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size("a4", landscape=False)
        vsk.scale("cm")

        for j in range(self.rows):
            with vsk.pushMatrix():
                for i in range(self.columns):
                    with vsk.pushMatrix():
                        vsk.rotate(self.fuzziness * 0.03 * vsk.random(-j, j))
                        vsk.translate(
                            self.fuzziness * 0.01 * vsk.randomGaussian() * j,
                            self.fuzziness * 0.01 * vsk.randomGaussian() * j,
                        )
                        vsk.rect(0, 0, 1, 1)
                    vsk.translate(1, 0)
            vsk.translate(0, 1)
            vsk.save("squares.svg") 
    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype("linemerge linesimplify reloop linesort")
        

SchotterSketch.display()


from shapely.affinity import translate
from shapely.geometry import Polygon

import vsketch


class StrokeJoinSketch(vsketch.SketchClass):
    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size("a4", landscape=False)
        vsk.scale("cm")

        p = translate(
            Polygon(
                [(-3, -1), (1.5, -2), (1.4, 2), (0, 1.5), (-1, 2.3)],
                holes=[[(-0.5, -0.5), (0.5, -0.5), (0.5, 0.5), (-0.5, 0.5)]],
            ),
            2.5,
            14,
        )

        # round join style (default)
        vsk.strokeWeight(10)
        vsk.square(0, 0, 4)
        vsk.triangle(0, 6, 2, 10, 4, 7)
        vsk.geometry(p)

        vsk.translate(7, 0)

        # bevel join style
        vsk.strokeJoin("bevel")
        vsk.square(0, 0, 4)
        vsk.triangle(0, 6, 2, 10, 4, 7)
        vsk.geometry(p)

        vsk.translate(7, 0)

        # mitre join style
        vsk.strokeJoin("mitre")
        vsk.square(0, 0, 4)
        vsk.triangle(0, 6, 2, 10, 4, 7)
        vsk.geometry(p)

    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype("linemerge linesimplify reloop linesort")


if __name__ == "__main__":
    StrokeJoinSketch.display()

import numpy as np

import vsketch
from vsketch import Vsketch


class EasingSketch(vsketch.SketchClass):
    mode = vsketch.Param("linear", choices=vsketch.EASING_FUNCTIONS.keys())
    low_deadzone = vsketch.Param(0.0, 0.0, 100.0, step=5)
    high_deadzone = vsketch.Param(0.0, 0.0, 100.0, step=5)
    param = vsketch.Param(10.0, step=1.0, decimals=1)

    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size("20x20cm", landscape=False, center=False)
        vsk.scale("cm")

        vsk.translate(2.5, 2.5)
        vsk.scale(15)
        input_coord = np.linspace(0.0, 1.0, num=1000)
        output_coord = Vsketch.easing(
            input_coord,
            mode=self.mode,
            low_dead=self.low_deadzone / 100.0,
            high_dead=self.high_deadzone / 100.0,
            param=self.param,
        )
        vsk.stroke(2)
        vsk.polygon(input_coord, 1.0 - output_coord)
        vsk.point(0.0, 1.0)
        vsk.point(1.0, 0.0)
        if self.low_deadzone > 0.0:
            vsk.point(self.low_deadzone / 100.0, 1.0)
        if self.high_deadzone > 0.0:
            vsk.point(1.0 - self.high_deadzone / 100.0, 0.0)
        vsk.vpype("penwidth --layer 2 .6mm")

        # Draw axes
        vsk.stroke(3)
        vsk.polygon([0, 0, 1, 1], [1.05, 1.07, 1.07, 1.05])
        vsk.polygon([-0.05, -0.07, -0.07, -0.05], [0, 0, 1, 1])
        vsk.vpype("color --layer 3 black")

        # Draw grid
        vsk.stroke(1)
        for coord in np.linspace(0, 1, num=11):
            vsk.line(coord, 0, coord, 1)
            vsk.line(0, coord, 1, coord)
        vsk.vpype("color --layer 1 #eee")

        # Draw text
        vsk.stroke(3)
        vsk.textMode("label")
        vsk.text("0", 0, 1.1, align="center")
        vsk.text("1", 1, 1.1, align="center")
        vsk.text("input", 0.5, 1.1, align="center")
        vsk.text("0", -0.1, 1, align="center")
        vsk.text("1", -0.1, 0, align="center")

        # vsk.text() doesn't support vertical text in label mode
        with vsk.pushMatrix():
            vsk.translate(-0.1, 0.5)
            vsk.rotate(-90, degrees=True)
            vsk.text("output", align="center", mode="transform", size=0.03)

        vsk.stroke(5)
        vsk.text(self.mode, 0.5, -0.07, align="center", size="30pt")
        vsk.vpype(f"color -l5 black")

    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype("linemerge linesimplify reloop linesort")


if __name__ == "__main__":
    EasingSketch.display()

import numpy as np

import vsketch


class NoiseBezierSketch(vsketch.SketchClass):
    N = vsketch.Param(200, 0)
    freq = vsketch.Param(0.003, decimals=3)
    drift = vsketch.Param(0.06, decimals=2)

    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size("a4", landscape=False)
        vsk.scale("cm")

        t = np.arange(self.N) * self.freq
        perlin = vsk.noise(t, np.arange(8) * 1000)

        for i in range(self.N):
            v = i * self.drift
            vsk.bezier(
                perlin[i, 0] * 15 + v,
                perlin[i, 1] * 15 + v,
                perlin[i, 2] * 15 + v,
                perlin[i, 3] * 15 + v,
                perlin[i, 4] * 15 + v,
                perlin[i, 5] * 15 + v,
                perlin[i, 6] * 15 + v,
                perlin[i, 7] * 15 + v,
            )
        vsk.display(fig_size=(12, 12))
    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype("linemerge linesimplify reloop linesort")


NoiseBezierSketch.display()





