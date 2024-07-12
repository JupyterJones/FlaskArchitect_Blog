import vsketch
import matplotlib
%matplotlib inline
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


vsk.display()
vsk.save("subsketch_basic.svg")

import cairosvg

width = 720
height = 480
cairosvg.svg2png(url="subsketch_basic.svg", write_to='subsketch_basic.png', output_width=width, output_height=height)

from PIL import Image
im = Image.open('subsketch_basic.png')
im

import matplotlib.pyplot as plt
import numpy as np
pi = 3.14
x = np.arange(0,100,0.00001)
y = x*np.sin(2*pi*x)
plt.plot(y)
plt.show()


!ls *.svg

import matplotlib.pyplot as plt
import svgutils.compose as sc
from IPython.display import SVG # /!\ note the 'SVG' function also in svgutils.compose
import numpy as np

# drawing a random figure on top of your SVG
fig, ax = plt.subplots(1, figsize=(4,4))
ax.plot(np.sin(np.linspace(0,2.*np.pi)), np.cos(np.linspace(0,2.*np.pi)), 'k--', lw=2.)
ax.plot(np.random.randn(20)*.3, np.random.randn(20)*.3, 'ro', label='random sampling')
ax.legend()
ax2 = plt.axes([.2, .2, .2, .2])
ax2.bar([0,1], [70,30])
plt.xticks([0.5,1.5], ['water  ', ' ground'])
plt.yticks([0,50])
plt.title('ratio (%)')
fig.savefig('cover.svg', transparent=True)
# here starts the assembling using svgutils 
sc.Figure("8cm", "8cm", 
    #sc.Panel(sc.SVG("./Worldmap_northern.svg").scale(0.405).move(36,29)),
    sc.Panel(sc.SVG("world.svg").scale(0.405).move(36,29)),
    sc.Panel(sc.SVG("cover.svg"))
    ).save("compose.svg")
SVG('compose.svg')

from IPython.display import SVG, display
def show_svg(filename):
    display(SVG(filename))
    
filename = "world.svg"    
show_svg(filename)    

from IPython.display import SVG, display
def show_svg(filename):
    display(SVG(filename))
    
filename = "subsketch_basic.svg"    
show_svg(filename)    

dir(SVG)

from IPython.display import SVG
from keras.utils import model_to_dot
SVG(model_to_dot(model).create(prog='dot', format='svg'))

from IPython.display import SVG
from keras.utils import model_to_dot
model = open("subsketch_recursive.svg")
SVG(model_to_dot(model, show_shapes= True, show_layer_names=True, dpi=65).create(prog='dot', format='svg'))

import spacy
import re
from spacy import displacy

nlp_model = spacy.load("en_core_web_sm")
doc = nlp_model(u"To be or not to be, that is the question")
svg = displacy.render(doc,  style='dep', page=True, jupyter=False)

def add_viewbox_svg(svg):
    regex = r'class="displacy" width="([\d\.]*)" height="([\d\.]*)'
    match_results = re.findall(regex,svg)
    new_svg = svg.replace("<svg ","<svg viewBox='0 0 "+
                          match_results[0][0]+" "+
                          match_results[0][1]+
                          "' preserveAspectRatio='none' ")
    return new_svg

#svg = "subsketch_basic.svg"  
new_svg = add_viewbox_svg(svg)

%%HTML
style = "<style>svg{width:100% !important;height:100% !important;</style>"
display(HTML(style))
display(HTML(new_svg))


vsk = vsketch.Vsketch()

vsk.scale(1.5)
vsk.rect(-5, -5, 10, 10)

for i in range(10):
    vsk.rotate(10, degrees=True)
    vsk.sketch(vsk)
    
vsk.display(mode="matplotlib")
vsk.save("subsketch_recursive.svg")

