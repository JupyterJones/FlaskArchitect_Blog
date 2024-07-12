!pwd

# -*- coding: utf-8 -*-



from numpy import pi
from numpy import array
from numpy import row_stack
from numpy.random import random
from numpy.random import randint
from numpy.linalg import norm
from numpy import cos
from numpy import sin
from numpy import arctan2


TWOPI = pi*2
HPI = pi*0.5


class Fracture(object):

  def __init__(
      self,
      fractures,
      fid,
      start,
      dx,
      frac_spd,
      frac_diminish
    ):

    self.i = 0
    self.fractures = fractures
    self.tree = fractures.tree
    self.frac_spd = frac_spd
    self.frac_diminish = frac_diminish

    self.start = start
    self.inds = [start]
    self.dxs = [dx]
    self.alive = True

    self.fid = fid

  def __relative_neigh_test(self, curr, new):

    from numpy import concatenate
    from numpy import unique
    from scipy.spatial.distance import cdist

    sources = self.fractures.sources
    visited = self.fractures.visited
    tri = self.fractures.tri
    simplices = tri.simplices
    simp = tri.find_simplex(new,bruteforce=True,tol=1e-10)
    neigh = concatenate((tri.neighbors[simp],[simp]))
    vv = set(list(unique(simplices[neigh,:])))

    if curr in vv:
      vv.remove(curr)
    vv = array(list(vv))

    dist = cdist(sources[vv, :], row_stack([new,sources[curr,:]]))
    mas = dist.max(axis=1)

    # curr_new = norm(new-sources[curr,:])
    curr_new = self.fractures.frac_stp

    free = mas<curr_new

    if sum(free)==0:
      return -1
    else:
      col = [k for k in vv[free] if k in visited]
      if col:
        return col[0]
      else:
        return -1

  def step(self, dbg=False):

    self.i += 1
    self.frac_spd *= self.frac_diminish

    dbgs = ''

    fractures = self.fractures
    sources = fractures.sources
    frac_dst = fractures.frac_dst
    dt = fractures.frac_dot
    visited = fractures.visited
    stp = fractures.frac_stp

    c = self.inds[-1]
    cx = sources[c,:]
    cdx = self.dxs[-1].reshape((1,2))

    near = self.tree.query_ball_point(cx, frac_dst)

    neardiff = sources[near,:] - cx
    nearnrm = norm(neardiff,axis=1).reshape((-1,1))

    nearnrm[nearnrm<=1e-9] = 1e10
    neardiff /= nearnrm

    mask = (cdx*neardiff).sum(axis=1)>dt

    if mask.sum()<1:
      self.alive = False
      if dbg:
        print(self.fid, 'no nearby sources')
      return False

    masked_diff = neardiff[mask]
    masked_nrm = nearnrm[mask]

    new_dx = (masked_diff/masked_nrm).sum(axis=0).flatten()
    new_dx /= norm(new_dx)
    new_pos = cx + new_dx*stp

    rel = self.__relative_neigh_test(c, new_pos)

    if rel>-1:
      dbgs += '{:d}: {:s}'.format(self.fid, 'collision (rn)')
      h = rel
      self.alive = False
    else:
      # new source
      dbgs += '{:d}: {:s}'.format(self.fid, 'new source')
      h = self.fractures._add_tmp_source(new_pos)
      self.alive = True
      visited[h] = new_dx

    if dbg:
      print(dbgs)

    self.dxs.append(new_dx)
    self.inds.append(h)

    return self.alive

class Fractures(object):

  def __init__(
      self,
      init_num,
      init_rad,
      source_dst,
      frac_dot,
      frac_dst,
      frac_stp,
      frac_spd=1.0,
      frac_diminish=1.0,
      frac_spawn_diminish=1.0,
      domain='rect'
    ):

    self.i = 0
    self.init_num = init_num
    self.init_rad = init_rad
    self.source_dst = source_dst
    self.frac_dot = frac_dot
    self.frac_dst = frac_dst
    self.frac_stp = frac_stp
    self.frac_spd = frac_spd
    self.frac_diminish = frac_diminish
    self.spawn_diminish = frac_spawn_diminish

    self.alive_fractures = []
    self.dead_fractures = []

    self.visited = {}

    self.count = 0

    self.tmp_sources = []
    self.__make_sources(domain=domain)

  def blow(self,n, x=array([0.5,0.5])):

    self.tmp_sources = []

    for a in random(size=n)*TWOPI:
      dx = array([cos(a), sin(a)])
      self.__make_fracture(x=x, dx=dx)

    self._append_tmp_sources()

  def __make_sources(self, xx=0.5, yy=0.5, rad=None, domain='rect'):

    from scipy.spatial import cKDTree as kdt
    from scipy.spatial import Delaunay as triag
    from iutils.random import darts
    from iutils.random import darts_rect

    if rad is None:
      rad = self.init_rad

    if domain=='circ':
      sources = darts(
        self.init_num,
        xx,
        yy,
        self.init_rad,
        self.source_dst
      )
    elif domain=='rect':
      sources = darts_rect(
        self.init_num,
        xx,
        yy,
        2*rad,
        2*rad,
        self.source_dst
      )
    else:
      raise ValueError('domain must be "rect" or "circ".')
    tree = kdt(sources)
    self.sources = sources
    self.tree = tree
    self.tri = triag(
      self.sources,
      incremental=False,
      qhull_options='QJ Qc'
    )
    self.num_sources = len(self.sources)

    return len(sources)

  def _add_tmp_source(self, x):

    self.tmp_sources.append(x)
    return len(self.sources)+len(self.tmp_sources)-1

  def _append_tmp_sources(self):

    from scipy.spatial import cKDTree as kdt
    from scipy.spatial import Delaunay as triag

    sources = row_stack([self.sources]+self.tmp_sources)
    tree = kdt(sources)
    self.sources = sources
    self.tree = tree
    self.tmp_sources = []
    self.tri = triag(
      self.sources,
      incremental=False,
      qhull_options='QJ Qc'
    )
    self.num_sources = len(self.sources)

    return len(sources)

  def __make_fracture(self, x=None, p=None, dx=None, spd=None):

    if p is None:
      _,p = self.tree.query(x,1)

    if spd is None:
      spd = self.frac_spd

    f = Fracture(
      self,
      self.count,
      p,
      dx,
      spd,
      self.frac_diminish
    )
    self.count += 1
    res = f.step()
    if res:
      self.alive_fractures.append(f)
    return res

  # def spawn_front(self, factor=1.0, angle=0.7):

    # if not self.alive_fractures:
      # return 0

    # self.tmp_sources = []
    # count = 0

    # for i in (random(size=len(self.alive_fractures))<factor).nonzero()[0]:
      # f = self.alive_fractures[i]
      # dx = f.dxs[-1]
      # a = arctan2(dx[1], dx[0]) + (-1)**randint(2)*HPI + (0.5-random()) * angle
      # count += int(self.__make_fracture(p=f.inds[-1], dx=array([cos(a), sin(a)])))

    # self._append_tmp_sources()

    # return count

  def spawn_front(self, factor=1.0, angle=0.7):

    if not self.alive_fractures:
      return 0

    self.tmp_sources = []
    count = 0

    for i,rnd in enumerate(random(size=len(self.alive_fractures))):
      f = self.alive_fractures[i]

      if rnd>f.frac_spd*factor:
        continue

      dx = f.dxs[-1]
      a = arctan2(dx[1], dx[0]) + (-1)**randint(2)*HPI + (0.5-random()) * angle
      count += int(
        self.__make_fracture(
          p=f.inds[-1],
          dx=array([cos(a), sin(a)]),
          spd=f.frac_spd*self.spawn_diminish
        )
      )

    self._append_tmp_sources()

    return count

  def step(self, dbg=False):

    self.i += 1

    self.tmp_sources = []

    fracs = []
    for f in self.alive_fractures:
      f.step(dbg)
      if f.alive:
        fracs.append(f)
      else:
        if len(f.inds)>1:
          self.dead_fractures.append(f)
        else:
          print('discarding path')

    self.alive_fractures = fracs

    self._append_tmp_sources()

    return len(fracs)>0

  def get_fracture_paths(self):

    paths = []

    for f in self.alive_fractures + self.dead_fractures:
      if len(f.inds)<2:
        continue
      path = row_stack([self.sources[p,:] for p in f.inds])
      paths.append(path)

    return paths

  def get_vertices_and_paths(self):

    vertices = self.sources
    paths = []
    for f in self.alive_fractures + self.dead_fractures:
      if len(f.inds)<2:
        continue

      paths.append(array(f.inds, 'int'))

    return vertices, paths

  def print_stats(self):

    alive = len(self.alive_fractures)
    dead = len(self.dead_fractures)
    print('# {:d} a: {:d} d: {:d} s: {:d}\n'
      .format(self.i, alive, dead, len(self.sources))
    )

spawn_front(self, factor=1.0, angle=0.7)
print_stats(self)

dir(Fracture)

#!/usr/bin/python3
# -*- coding: utf-8 -*-




BACK = [1,1,1,1]
FRONT = [0,0,0,0.8]
LIGHT = [0,0,0,0.2]
CYAN = [0,0.5,0.5,0.2]
BLUE = [0,0,1,0.3]


NMAX = 10**6
SIZE = 1200
ONE = 1./SIZE
LINEWIDTH = ONE*1.1

INIT_NUM = 20000
INIT_RAD = 0.45

SOURCE_DST = 2.0*ONE

FRAC_DOT = 0.85
FRAC_DST = 100.*ONE
FRAC_STP = ONE*2
FRAC_SPD = 1.0

FRAC_DIMINISH = 0.997
FRAC_SPAWN_DIMINISH = 0.9


SPAWN_ANGLE = 2.0
SPAWN_FACTOR = 0.2



def show(render,fractures):

  sources = fractures.sources
  alive_fractures = fractures.alive_fractures
  dead_fractures = fractures.dead_fractures

  def draw_sources():
    for i,s in enumerate(sources):
      if i not in fractures.visited:
        render.circle(*s, r=4*ONE, fill=True)

  def draw_lines(fracs):
    for frac in fracs:
      start = frac.inds[0]
      render.ctx.move_to(*sources[start,:])
      for c in frac.inds[1:]:
        render.ctx.line_to(*sources[c,:])
      render.ctx.stroke()

  render.clear_canvas()

  # render.ctx.set_source_rgba(*LIGHT)
  # draw_sources()

  render.ctx.set_source_rgba(*LIGHT)
  render.set_line_width(3*LINEWIDTH)
  draw_lines(alive_fractures+dead_fractures)

  render.ctx.set_source_rgba(*FRONT)
  render.set_line_width(LINEWIDTH)
  draw_lines(alive_fractures+dead_fractures)

  # for f in alive_fractures:
    # for s in sources[f.inds,:]:
      # render.circle(*s, r=2*ONE, fill=False)

def random_uniform_circle(rad, num):

  from numpy.random import random
  from numpy.linalg import norm
  from numpy import array


  while True:
    xy = 0.5-random(size=2)
    if norm(xy)>1.0:
      continue
    r = array([0.5]*2)+xy*rad
    return r



def main():

  from iutils.render import Animate
  from modules.fracture import Fractures

  # from dddUtils.ioOBJ import export_2d as export
  from fn import Fn
  fn = Fn(prefix='./res/',postfix='.2obj')

  F = Fractures(
    INIT_NUM,
    INIT_RAD,
    SOURCE_DST,
    FRAC_DOT,
    FRAC_DST,
    FRAC_STP,
    FRAC_SPD,
    FRAC_DIMINISH,
    FRAC_SPAWN_DIMINISH,
    domain = 'rect'
  )

  print(F.sources.shape)

  # uniform square distribution
  from numpy.random import random
  for _ in range(5):
    F.blow(2, random(size=2))

  # uniform circular distribution
  # for _ in xrange(5):
    # F.blow(3, random_uniform_circle(INIT_RAD, num=1))

  def wrap(render):

    if not F.i % 20:
      show(render,F)
      # vertices, paths = F.get_vertices_and_paths()
      # export('fractures', fn.name(), vertices, lines=paths)
      render.write_to_png(fn.name()+'.png')

    F.print_stats()
    res = F.step(dbg=False)
    n = F.spawn_front(factor=SPAWN_FACTOR, angle=SPAWN_ANGLE)
    print('spawned: {:d}'.format(n))

    # fn = './asdf_{:04d}.png'.format(F.i)
    # render.write_to_png(fn)

    # if not res:
      # vertices, paths = F.get_vertices_and_paths()
      # export('fractures', fn.name(), vertices, lines=paths)

    return res

  render = Animate(SIZE, BACK, FRONT, wrap)
  render.start()


if __name__ == '__main__':

  main()



!pip install iutils

import iutils

from iutils import render

!ls /home/jack/miniconda3/envs/cloned_base/lib/python3.9/site-packages/iutils/

# %load /home/jack/miniconda3/envs/cloned_base/lib/python3.9/site-packages/iutils/utils.py
def remove_last_n_chars(string: str, n: int):
    """Given a string, return the string with its last n characters removed."""
    if type(n) is not int:
        raise TypeError(f"`{n}' must be an integrer.")

    if n < 0:
        raise ValueError(f"`{n}' must be greater than or equal to 0.")

    if len(string) <= n:
        return ""

    return string[: len(string) - n]


def two_level_split(line, sep=" ", quote='"'):
    """Split a line by sep.

    The line may optionally contains fields that are quoted by the quote sign.
    """

    in_quotes = False
    results = []
    temp = []

    for field in line.split(sep):
        if not field:
            # append to temp if in_quotes, otherwise append to results
            temp.append(field) if in_quotes else results.append(field)
            continue

        if in_quotes:
            if field[0] == quote:
                raise ValueError(f"Non-matching `{quote}' quote: {line}")
            else:
                if field[-1] == quote:
                    temp.append(field.strip(quote))
                    results.append(sep.join(temp))
                    temp = []
                    in_quotes = False
                else:
                    temp.append(field)
        else:
            if field[0] == quote:
                if field[-1] == quote:
                    results.append(field.strip(quote))
                else:
                    in_quotes = True
                    temp.append(field.strip(quote))
            else:
                if field[-1] == quote:
                    raise ValueError(f"Non-matching `{quote}' quote: {line}")
                else:
                    results.append(field)

    return results


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
BACK = [0,0,0,1]
FRONT = [1,1,1,1]
SIZE = 2000
N = 40
W = int(SIZE/N)
ONE = 1.0/SIZE

def main():
    from iutils.render import Render
    render = Render(SIZE, BACK, FRONT)
    render.clear_canvas()
    from iutils.colors import get_colors
    colors = get_colors('10.gif') # point to your source image
    nc = len(colors)
    for i in range(N):
        for j in range(N):
            # random colors
            rgba = colors[(i*N+j)%nc] + [1]
            render.set_front(rgba)
            # bw checkers
            if not (i+j)%2:
                continue

            a = (i*W)*ONE
            b = (j*W)*ONE
            print(a,b, W*ONE)
            render.ctx.rectangle(a,b,W*ONE,W*ONE)
            render.ctx.fill()

    render.write_to_png('checkers.png')


if __name__ == '__main__':
    main()



from PIL import Image
im = Image.open("checkers.png")
im

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


BACK = [0,0,0,1]
FRONT = [1,1,1,1]
SIZE = 2000
N = 40
W = int(SIZE/N)
ONE = 1.0/SIZE

def main():

  from iutils.render import Render

  render = Render(SIZE, BACK, FRONT)
  render.clear_canvas()

  # from iutils.colors import get_colors
  # colors = get_colors('./colors/img.gif') # point to your source image
  # nc = len(colors)

  for i in range(N):
    for j in range(N):

      # random colors
      # rgba = colors[(i*N+j)%nc] + [1]
      # render.set_front(rgba)

      # bw checkers
      if not (i+j)%2:
        continue

      a = (i*W)*ONE
      b = (j*W)*ONE
      print(a,b, W*ONE)
      render.ctx.rectangle(a,b,W*ONE,W*ONE)
      render.ctx.fill()

  render.write_to_png('checkers.png')


if __name__ == '__main__':
  main()



import numpy as np


def interpolant(t):
    return t*t*t*(t*(t*6 - 15) + 10)


def generate_perlin_noise_2d(
        shape, res, tileable=(False, False), interpolant=interpolant
):
    """Generate a 2D numpy array of perlin noise.

    Args:
        shape: The shape of the generated array (tuple of two ints).
            This must be a multple of res.
        res: The number of periods of noise to generate along each
            axis (tuple of two ints). Note shape must be a multiple of
            res.
        tileable: If the noise should be tileable along each axis
            (tuple of two bools). Defaults to (False, False).
        interpolant: The interpolation function, defaults to
            t*t*t*(t*(t*6 - 15) + 10).

    Returns:
        A numpy array of shape shape with the generated noise.

    Raises:
        ValueError: If shape is not a multiple of res.
    """
    delta = (res[0] / shape[0], res[1] / shape[1])
    d = (shape[0] // res[0], shape[1] // res[1])
    grid = np.mgrid[0:res[0]:delta[0], 0:res[1]:delta[1]]\
             .transpose(1, 2, 0) % 1
    # Gradients
    angles = 2*np.pi*np.random.rand(res[0]+1, res[1]+1)
    gradients = np.dstack((np.cos(angles), np.sin(angles)))
    if tileable[0]:
        gradients[-1,:] = gradients[0,:]
    if tileable[1]:
        gradients[:,-1] = gradients[:,0]
    gradients = gradients.repeat(d[0], 0).repeat(d[1], 1)
    g00 = gradients[    :-d[0],    :-d[1]]
    g10 = gradients[d[0]:     ,    :-d[1]]
    g01 = gradients[    :-d[0],d[1]:     ]
    g11 = gradients[d[0]:     ,d[1]:     ]
    # Ramps
    n00 = np.sum(np.dstack((grid[:,:,0]  , grid[:,:,1]  )) * g00, 2)
    n10 = np.sum(np.dstack((grid[:,:,0]-1, grid[:,:,1]  )) * g10, 2)
    n01 = np.sum(np.dstack((grid[:,:,0]  , grid[:,:,1]-1)) * g01, 2)
    n11 = np.sum(np.dstack((grid[:,:,0]-1, grid[:,:,1]-1)) * g11, 2)
    # Interpolation
    t = interpolant(grid)
    n0 = n00*(1-t[:,:,0]) + t[:,:,0]*n10
    n1 = n01*(1-t[:,:,0]) + t[:,:,0]*n11
    return np.sqrt(2)*((1-t[:,:,1])*n0 + t[:,:,1]*n1)


def generate_fractal_noise_2d(
        shape, res, octaves=1, persistence=0.5,
        lacunarity=2, tileable=(False, False),
        interpolant=interpolant
):
    """Generate a 2D numpy array of fractal noise.

    Args:
        shape: The shape of the generated array (tuple of two ints).
            This must be a multiple of lacunarity**(octaves-1)*res.
        res: The number of periods of noise to generate along each
            axis (tuple of two ints). Note shape must be a multiple of
            (lacunarity**(octaves-1)*res).
        octaves: The number of octaves in the noise. Defaults to 1.
        persistence: The scaling factor between two octaves.
        lacunarity: The frequency factor between two octaves.
        tileable: If the noise should be tileable along each axis
            (tuple of two bools). Defaults to (False, False).
        interpolant: The, interpolation function, defaults to
            t*t*t*(t*(t*6 - 15) + 10).

    Returns:
        A numpy array of fractal noise and of shape shape generated by
        combining several octaves of perlin noise.

    Raises:
        ValueError: If shape is not a multiple of
            (lacunarity**(octaves-1)*res).
    """
    noise = np.zeros(shape)
    frequency = 1
    amplitude = 1
    for _ in range(octaves):
        noise += amplitude * generate_perlin_noise_2d(
            shape, (frequency*res[0], frequency*res[1]), tileable, interpolant
        )
        frequency *= lacunarity
        amplitude *= persistence
    return noise


!which python

%%writefile ani.py
#!/home/jack/miniconda3/envs/cloned_base/bin/python
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from perlin_numpy import generate_perlin_noise_3d

np.random.seed(0)
noise = generate_perlin_noise_3d(
    (32, 256, 256), (1, 4, 4), tileable=(True, False, False)
)

fig = plt.figure()
images = [
    [plt.imshow(
        layer, cmap='gray', interpolation='lanczos', animated=True
    )]
    for layer in noise
]
animation_3d = animation.ArtistAnimation(fig, images, interval=50, blit=True)
plt.show()

!mkdir newseries

%%writefile viddrawImage.py
"""
@author: The Absolute Tinkerer
"""

import os
import math
import time
import random

import numpy as np

from PIL import Image

from PyQt5.QtGui import QColor, QPen, QPixmap
from PyQt5.QtCore import QPointF, QRect

import Painter
from utils import QColor_HSV, save, Perlin2D


def draw_white_noise(width, height, fname):
    assert not os.path.exists(fname), 'File already exists!'

    # Create a matrix of random values between zero and one
    pixels = np.random.random(size=(height, width))

    # Now modify the random values to be 0-255 (pixel color range)
    pixels = 255*pixels

    # The function to write the array of pixels to an image requires integers, not float values
    pixels = pixels.astype(np.uint8)

    # We choose to make random values grayscale, so each RGB element is identical. This code adds the third dimension
    # to our pixels array
    pixels = pixels[:, :, np.newaxis]

    # We need to repeat each value to finalize the pixels arrays in the grayscale space
    pixels = np.repeat(pixels, 3, axis=2)

    # Now create the image from an array of pixels
    im = Image.fromarray(pixels)

    # Save the image to file
    im.save(fname)


def draw_perlin(nx, ny, width, height, fname):
    assert not os.path.exists(fname), 'File already exists'

    # Initialize Perlin Noise
    noise = (Perlin2D(width, height, nx, ny) + 1)/2

    # Convert to pixels
    pixels = 255 * noise
    pixels = pixels.astype(np.uint8)
    pixels = pixels[:, :, np.newaxis]
    pixels = np.repeat(pixels, 3, axis=2)

    # Create and save the image from pixels
    im = Image.fromarray(pixels)
    im.save(fname)

    return noise


def draw_vectors(nx, ny, width, height, seed=random.randint(0, 100000000), flow_length=100, n_vectors=50):
    p_path = f'{seed}_1_perlin_noise.jpg'
    v_path = f'{seed}_2_vectors'
    f_path = f'{seed}_3_flow_field'

    # Ensure we don't overwrite paths
    assert not os.path.exists(p_path), 'Perlin Noise image already exists!'
    assert not os.path.exists(v_path), 'Vectors image already exists!'
    assert not os.path.exists(f_path), 'Flow field image already exists!'

    # Set the random seed for repeatability
    np.random.seed(seed)

    # Create the Perlin Noise image
    noise = draw_perlin(nx, ny, width, height, p_path)

    # Initialize the painter object for drawing
    p = Painter.Painter(width, height)
    p.setRenderHint(p.Antialiasing)  # allow smooth drawing

    def draw_arrow(p, x_i, y_i, length=100, angle=0):
        # Compute the second points and draw the arrow body
        x_f = x_i + length*math.cos(math.radians(angle))
        y_f = y_i - length*math.sin(math.radians(angle))
        p.drawLine(x_i, y_i, x_f, y_f)

        # Compute the arrow head second points
        a_angle1, a_angle2 = math.radians(angle-30), math.radians(angle+30)
        x1 = x_f - (length/10)*math.cos(a_angle1)
        y1 = y_f + (length/10)*math.sin(a_angle1)
        x2 = x_f - (length/10)*math.cos(a_angle2)
        y2 = y_f + (length/10)*math.sin(a_angle2)
        p.drawLine(x_f, y_f, x1, y1)
        p.drawLine(x_f, y_f, x2, y2)

    # Load the Perlin Noise image and draw it with the painter
    p.drawPixmap(QRect(0, 0, width, height), QPixmap(p_path))

    # Now we're drawing red arrows for vectors, so set the pen color to red
    p.setPen(QColor(255, 0, 0))

    # We need arrow locations, so create a grid of n_vectors x n_vectors, excluding the image border
    _nx, _ny = n_vectors, n_vectors
    dx, dy = width / (_nx + 1), height / (_ny + 1)
    x_points = [dx + i*dx for i in range(_nx)]
    y_points = [dy + i*dy for i in range(_ny)]

    # Draw the arrows
    for x in x_points:
        for y in y_points:
            angle = 360*noise[int(x), int(y)]
            draw_arrow(p, x, y, length=min(dx, dy), angle=angle)

    # Save the vector image
    save(p, fname=v_path, folder='.')

    # Now draw the flow field. Start by initializing a new painter
    p = Painter.Painter(width, height)
    p.setRenderHint(p.Antialiasing)  # allow smooth drawing
    p.setPen(QColor(0, 0, 0))  # pen color set to black

    # Step size between points
    STEP_SIZE = 0.001 * max(width, height)

    # Draw the flow field
    for x in x_points:
        for y in y_points:
            # The starting position
            x_s, y_s = x, y
            # The current line length tracking variable
            c_len = 0
            while c_len < flow_length:
                # angle between 0 and 2*pi
                angle = 2 * noise[int(x_s), int(y_s)] * math.pi

                # Compute the new point
                x_f = x_s + STEP_SIZE * math.cos(angle)
                y_f = y_s - STEP_SIZE * math.sin(angle)

                # Draw the line
                p.drawLine(QPointF(x_s, y_s), QPointF(x_f, y_f))

                # Update the line length
                c_len += math.sqrt((x_f - x_s) ** 2 + (y_f - y_s) ** 2)

                # Break from the loop if the new point is outside our image bounds
                # or if we've exceeded the line length; otherwise update the point
                if x_f < 0 or x_f >= width or y_f < 0 or y_f >= height or c_len > flow_length:
                    break
                else:
                    x_s, y_s = x_f, y_f
    save(p, fname=f_path, folder='.')


def draw_flow_field(width, height, seed=random.randint(0, 100000000)):
    # Set the random seed for repeatability
    np.random.seed(seed)

    # These are color hues
    colors = [200, 140, 70, 340, 280]
    for i, mod in enumerate(colors):
        print('Starting Image %s/%s' % (i + 1, len(colors)))
        p = Painter.Painter(width, height)

        # Allow smooth drawing
        p.setRenderHint(p.Antialiasing)

        # Draw the background color
        p.fillRect(0, 0, width, height, QColor(0, 0, 0))

        # Set the pen color
        p.setPen(QPen(QColor(150, 150, 225, 5), 2))

        num = 1
        for j in range(num):
            print('Creating Noise... (%s/%s)' % (j + 1, num))
            p_noise = Perlin2D(width, height, 2, 2)
            print('Noise Generated! (%s/%s)' % (j + 1, num))

            MAX_LENGTH = 2 * width
            STEP_SIZE = 0.001 * max(width, height)
            NUM = int(width * height / 1000)
            POINTS = [(random.randint(0, width - 1), random.randint(0, height - 1)) for i in range(NUM)]

            for k, (x_s, y_s) in enumerate(POINTS):
                print(f'{100 * (k + 1) / len(POINTS):.1f}'.rjust(5) + '% Complete', end='\r')

                # The current line length tracking variable
                c_len = 0

                # Actually draw the flow field
                while c_len < MAX_LENGTH:
                    # Set the pen color for this segment
                    sat = 200 * (MAX_LENGTH - c_len) / MAX_LENGTH
                    hue = (mod + 130 * (height - y_s) / height) % 360
                    p.setPen(QPen(QColor_HSV(hue, sat, 255, 20), 2))

                    # angle between -pi and pi
                    angle = p_noise[int(x_s), int(y_s)] * math.pi

                    # Compute the new point
                    x_f = x_s + STEP_SIZE * math.cos(angle)
                    y_f = y_s + STEP_SIZE * math.sin(angle)

                    # Draw the line
                    p.drawLine(QPointF(x_s, y_s), QPointF(x_f, y_f))

                    # Update the line length
                    c_len += math.sqrt((x_f - x_s) ** 2 + (y_f - y_s) ** 2)

                    # Break from the loop if the new point is outside our image bounds
                    # or if we've exceeded the line length; otherwise update the point
                    if x_f < 0 or x_f >= width or y_f < 0 or y_f >= height or c_len > MAX_LENGTH:
                        break
                    else:
                        x_s, y_s = x_f, y_f

                    save(p, fname=f'image_{i}_{mod}_{num}_{seed}', folder='newseries/', overwrite=True)


def draw_perlin_rounding(width, height, fname, seed=random.randint(0, 100000000)):
    # Ensure we don't overwrite paths
    assert not os.path.exists(fname), 'Image already exists!'

    # Set the random seed for repeatability
    np.random.seed(seed)

    # Initialize a new painter
    p = Painter.Painter(width, height)
    p.setRenderHint(p.Antialiasing)

    # Draw the background color
    #p.fillRect(0, 0, width, height, QColor(0, 0, 0))
    p.fillRect(0, 0, width, height, QColor("darkRed"))

    # Set the pen color
    p.setPen(QColor(200, 200, 200))
    p.setPen(QColor("yellow"))

    print('Creating Noise...', end='', flush=True)
    noise = Perlin2D(width, height, 1, 1)
    print('Done!')

    # The maximum line length and step size
    MAX_LENGTH = 1000
    STEP_SIZE = 0.001 * max(width, height)

    # Compute a grid 200x200 points, centered in the screen
    dx, dy = width / (200 + 1), height / (200 + 1)
    POINTS = [[(i+1)*dx, (j+1)*dy] for i in range(200) for j in range(200)]

    for i, (x_s, y_s) in enumerate(POINTS):
        print(f'{100 * (i + 1) / len(POINTS):.1f}'.rjust(5) + '% Complete', end='\r')

        # The current line length tracking variable
        c_len = 0
        while c_len < MAX_LENGTH:
            # angle between -pi and pi
            angle = math.pi*noise[int(x_s), int(y_s)]

            # Round the angle to pi/4 increments
            angle = round(angle / (math.pi / 4)) * (math.pi / 4)

            # Compute the new point
            x_f = x_s + STEP_SIZE * math.cos(angle)
            y_f = y_s + STEP_SIZE * math.sin(angle)

            # Draw the line
            p.drawLine(x_s, y_s, x_f, y_f)

            # Update the line length
            c_len += math.sqrt((x_f - x_s) ** 2 + (y_f - y_s) ** 2)

            # Break from the loop if the new point is outside our image bounds
            # or if we've exceeded the line length; otherwise update the point
            if (x_f < 0 or x_f >= width or y_f < 0 or y_f >= height or
                    c_len > MAX_LENGTH):
                break
            else:
                x_s, y_s = x_f, y_f

            print('100% Complete!')
            save(p, fname=f'{i}_{fname}_{seed}', folder='.')


class Body:
    def __init__(self, x, y, vx, vy):
        self._position = np.array([x, y], dtype=np.float64)
        self._velocity = np.array([vx, vy], dtype=np.float64)

    @property
    def position(self):
        return self._position

    @property
    def velocity(self):
        return self._velocity

    def update(self, dt):
        # update the body position
        self._position = self._position + dt*self._velocity


class ExpandingCircleRandom:
    def __init__(self, radius, num_bodies, center=(0, 0), v_limits=(-2, 2)):
        self._bodies = [Body(center[0] + radius*math.cos(i*2*math.pi/num_bodies),
                             center[1] + radius*math.sin(i*2*math.pi/num_bodies),
                             v_limits[0]+(v_limits[1]-v_limits[0])*random.random(),
                             v_limits[0]+(v_limits[1]-v_limits[0])*random.random()) for i in range(num_bodies)]

    def draw(self, dt, Painter):
        # Connect the dots between each body
        for i in range(len(self._bodies)):
            # Handle the wrapping case
            if i == len(self._bodies) - 1:
                p1 = QPointF(*self._bodies[i].position)
                p2 = QPointF(*self._bodies[0].position)
            else:
                p1 = QPointF(*self._bodies[i].position)
                p2 = QPointF(*self._bodies[i+1].position)
            Painter.drawLine(p1, p2)

        # Update the position of each body
        for i in range(len(self._bodies)):
            self._bodies[i].update(dt)


class ExpandingCircleNoise:
    def __init__(self, radius, num_bodies, noise, center=(0, 0), v_max=2):
        self._bodies = [Body(center[0] + radius*math.cos(i*2*math.pi/num_bodies),
                             center[1] + radius*math.sin(i*2*math.pi/num_bodies),
                             0, 0) for i in range(num_bodies)]
        self._v_max = v_max
        self._noise = noise

    def draw(self, dt, painter):
        # Connect the dots between each body
        for i in range(len(self._bodies)):
            # Handle the wrapping case
            if i == len(self._bodies) - 1:
                p1 = QPointF(*self._bodies[i].position)
                p2 = QPointF(*self._bodies[0].position)
            else:
                p1 = QPointF(*self._bodies[i].position)
                p2 = QPointF(*self._bodies[i + 1].position)
            painter.drawLine(p1, p2)

            # Try to update the velocity for each body. If we can't its because the point is beyond the noise
            # field we've created, so at that point, just maintain velocity.
            try:
                a = math.pi*self._noise[int(p1.x()), int(p1.y())]
                v = np.array([self._v_max*math.cos(a), self._v_max*math.sin(a)])
                self._bodies[i]._velocity = v
            except IndexError:
                pass

        # Update the position of each body
        for i in range(len(self._bodies)):
            self._bodies[i].update(dt)

def draw_delta_body(width, height, iterations = 2000,seed=random.randint(0, 100000000), mode='noise'):
    #def draw_delta_body(width, height, seed=random.randint(0, 100000000), mode='noise'):
    assert mode in ['noise', 'random'], 'Mode must either be "noise" or "random"'

    # Set the random seed for repeatability
    np.random.seed(seed)
    random.seed(seed)

    # Initialize the painter
    p = Painter.Painter(width, height)
    p.setRenderHint(p.Antialiasing)  # Allow smooth drawing

    # Draw the background color
    p.fillRect(0, 0, width, height, QColor(0, 0, 0))

    # Set the pen color
    p.setPen(QPen(QColor(220, 220, 220, 5), 1))

    # Initialize the expanding circle centered in the canvas
    if mode == 'random':
        circle = ExpandingCircleRandom(width/8, 100, center=(width/2, height/2), v_limits=(-2, 2))
    elif mode == 'noise':
        noise = Perlin2D(width, height, 5, 5)
        circle = ExpandingCircleNoise(width/6, 200, noise, center=(width/4, height/2), v_max=5)
    else:
        circle = None

    # Initialize the delta time we're applying to each update
    dt = 0.3

    #iterations = 2000
    for i in range(iterations):
        circle.draw(dt, p)

        save(p, fname=f'delta_{i}_{mode}_{seed}', folder='series/', overwrite=True)
    #print("fname: ",fname)

from viddrawImage  import *
cnt=1
width= 1000
height=1000
fname = "VID"+str(cnt)+"-.png"
print(fname)
draw_perlin_rounding(width, height, fname, seed=random.randint(0, 100000000))

from viddrawImage import *
cnt = 123
width= 1000
height=1000
fname = "newseries/noiseZ"+str(cnt)+"-.png"
print(fname)
#draw_perlin_rounding(width, height, fname, seed=random.randint(0, 100000000))
draw_delta_body(width, height, iterations = 1000, seed=random.randint(0, 100000000), mode='noise')

from viddrawImage import *
#fname = "noiseZ"+str(0.1)+"-.png"
for cnt in range(0,2):
    width= 1000
    height=1000
    fname = "series/noiseZ"+str(cnt)+"-.png"
    print(fname)
    #draw_perlin_rounding(width, height, fname, seed=random.randint(0, 100000000))
    draw_delta_body(width, height, iterations = 300, seed=random.randint(0, 100000000), mode='noise')

width= 1000
cnt= 6
height=1000

fname = "noise"+str(cnt)+"_.png"
draw_white_noise(width, height, fname)

!mkdir series

from drawImage import *
#fname = "noiseZ"+str(0.1)+"-.png"
for cnt in range(166,170):
    width= 1000
    height=1000
    fname = "series/noiseZ"+str(cnt)+"-.png"
    print(fname)
    #draw_perlin_rounding(width, height, fname, seed=random.randint(0, 100000000))
    draw_delta_body(width, height, iterations = 2000, seed=random.randint(0, 100000000), mode='noise')

from drawImage import *
for cnt in range(141,160):
    width= 1000
    height=1000
    fname = "noise"+str(cnt)+"-.png"
    print(fname)
    draw_perlin_rounding(width, height, fname, seed=random.randint(0, 100000000))

from PIL import Image
im = Image.open(fname)

!ls mAk*

# %load mAke
#!/home/jack/miniconda3/envs/cloned_base/bin/python

"""
@author: The Absolute Tinkerer
"""

import os
import math
import numpy as np

from PyQt5.QtGui import QColor


def QColor_HSV(h, s, v, a=255):
    """
    Hue        : > -1 [wraps between 0-360]
    Saturation : 0-255
    Value      : 0-255
    Alpha      : 0-255
    """
    color = QColor()
    color.setHsv(*[int(e) for e in [h, s, v, a]])
    return color


def save(p, fname='image', folder='newseries/', extension='jpg', quality=100, overwrite=True):
    if not os.path.exists(folder):
        os.mkdir(folder)

    # The image name
    imageFile = f'{folder}/{fname}.{extension}'

    # Do not overwrite the image if it exists already
    if os.path.exists(imageFile):
        assert overwrite, 'File exists and overwrite is set to False!'

    # fileName, format, quality [0 through 100]
    p.saveImage(imageFile, imageFile[-3:], quality)


def Perlin2D(width, height, n_x, n_y, clampHorizontal=False, clampVertical=False):
    """
    Constructor

    Optimizations were gained from studying:
    https://github.com/pvigier/perlin-numpy/blob/master/perlin_numpy/perlin2d.py

    Parameters:
    -----------
    width : int
        The width of the canvas
    height : int
        The height of the canvas
    n_x : int
        The number of x tiles; must correspond to an integer x-edge length
    n_y : int
        The number of y tiles; must correspond to an integer y-edge length
    clampHorizontal : boolean
        Imagine the Perlin Noise on a sheet of paper - form a cylinder with
        the horizontal edges. If True, cylinder will be continuous noise
    clampVertical : boolean
        Imagine the Perlin Noise on a sheet of paper - form a cylinder with
        the vertical edges. If True, cylinder will be continuous noise

    Returns:
    --------
    <value> : numpy array
        noise values for array[width, height] between -1 and 1
    """
    # First ensure even number of n_x and n_y divide into the width and height,
    # respectively
    msg = 'n_x and n_y must evenly divide into width and height, respectively'
    assert width % n_x == 0 and height % n_y == 0, msg

    # We start off by defining our interpolation function
    def fade(t):
        return t * t * t * (t * (t * 6 - 15) + 10)

    # Next, we generate the gradients that we are using for each corner point
    # of the grid
    angles = 2 * np.pi * np.random.rand(n_x + 1, n_y + 1)
    r = math.sqrt(2)  # The radius of the unit circle
    gradients = np.dstack((r * np.cos(angles), r * np.sin(angles)))

    # Now, if the user has chosen to clamp at all, set the first and last row/
    # column equal to one another
    if clampHorizontal:
        gradients[-1, :] = gradients[0, :]
    if clampVertical:
        gradients[:, -1] = gradients[:, 0]

    # Now that gradient vectors are complete, we need to create the normalized
    # distance from each point to its starting grid point. In other words, this
    # is the normalized distance from the grid tile's origin based upon the
    # grid tile's width and height
    delta = (n_x / width, n_y / height)
    grid = np.mgrid[0:n_x:delta[0], 0:n_y:delta[1]].transpose(1, 2, 0) % 1

    # At this point, we need to compute the dot products for each corner of the
    # grid. To do this, we first need proper-dimensioned gradient vectors - do
    # this now. A computation for number of points per tile is needed as well
    px, py = int(width / n_x), int(height / n_y)
    gradients = gradients.repeat(px, 0).repeat(py, 1)
    g00 = gradients[:-px, :-py]
    g10 = gradients[px:, :-py]
    g01 = gradients[:-px, py:]
    g11 = gradients[px:, py:]

    # Compute dot products for each corner
    d00 = np.sum(g00 * grid, 2)
    d10 = np.sum(g10 * np.dstack((grid[:, :, 0] - 1, grid[:, :, 1])), 2)
    d01 = np.sum(g01 * np.dstack((grid[:, :, 0], grid[:, :, 1] - 1)), 2)
    d11 = np.sum(g11 * np.dstack((grid[:, :, 0] - 1, grid[:, :, 1] - 1)), 2)

    # We're doing improved perlin noise, so we use a fade function to compute
    # the x and y fractions used in the linear interpolation computation
    # t is the faded grid
    # u is the faded dot product between the top corners
    # v is the faded dot product between the bottom corners
    # _x and _y are the fractional (0-1) location of x, y in the tile
    t = fade(grid)
    u = d00 + t[:, :, 0] * (d10 - d00)
    v = d01 + t[:, :, 0] * (d11 - d01)

    # Now perform the second dimension's linear interpolation to return value
    return u + t[:, :, 1] * (v - u)


"""
@author: The Absolute Tinkerer
"""

import os
import math
import time
import random

import numpy as np

from PIL import Image

from PyQt5.QtGui import QColor, QPen, QPixmap
from PyQt5.QtCore import QPointF, QRect

import Painter
#from utils import QColor_HSV, save, Perlin2D


def draw_white_noise(width, height, fname):
    assert not os.path.exists(fname), 'File already exists!'

    # Create a matrix of random values between zero and one
    pixels = np.random.random(size=(height, width))

    # Now modify the random values to be 0-255 (pixel color range)
    pixels = 255*pixels

    # The function to write the array of pixels to an image requires integers, not float values
    pixels = pixels.astype(np.uint8)

    # We choose to make random values grayscale, so each RGB element is identical. This code adds the third dimension
    # to our pixels array
    pixels = pixels[:, :, np.newaxis]

    # We need to repeat each value to finalize the pixels arrays in the grayscale space
    pixels = np.repeat(pixels, 3, axis=2)

    # Now create the image from an array of pixels
    im = Image.fromarray(pixels)

    # Save the image to file
    im.save(fname)


def draw_perlin(nx, ny, width, height, fname):
    assert not os.path.exists(fname), 'File already exists'

    # Initialize Perlin Noise
    noise = (Perlin2D(width, height, nx, ny) + 1)/2

    # Convert to pixels
    pixels = 255 * noise
    pixels = pixels.astype(np.uint8)
    pixels = pixels[:, :, np.newaxis]
    pixels = np.repeat(pixels, 3, axis=2)

    # Create and save the image from pixels
    im = Image.fromarray(pixels)
    im.save(fname)

    return noise


def draw_vectors(nx, ny, width, height, seed=random.randint(0, 100000000), flow_length=100, n_vectors=50):
    p_path = f'{seed}_1_perlin_noise.jpg'
    v_path = f'{seed}_2_vectors'
    f_path = f'{seed}_3_flow_field'

    # Ensure we don't overwrite paths
    assert not os.path.exists(p_path), 'Perlin Noise image already exists!'
    assert not os.path.exists(v_path), 'Vectors image already exists!'
    assert not os.path.exists(f_path), 'Flow field image already exists!'

    # Set the random seed for repeatability
    np.random.seed(seed)

    # Create the Perlin Noise image
    noise = draw_perlin(nx, ny, width, height, p_path)

    # Initialize the painter object for drawing
    p = Painter.Painter(width, height)
    p.setRenderHint(p.Antialiasing)  # allow smooth drawing

    def draw_arrow(p, x_i, y_i, length=100, angle=0):
        # Compute the second points and draw the arrow body
        x_f = x_i + length*math.cos(math.radians(angle))
        y_f = y_i - length*math.sin(math.radians(angle))
        p.drawLine(x_i, y_i, x_f, y_f)

        # Compute the arrow head second points
        a_angle1, a_angle2 = math.radians(angle-30), math.radians(angle+30)
        x1 = x_f - (length/10)*math.cos(a_angle1)
        y1 = y_f + (length/10)*math.sin(a_angle1)
        x2 = x_f - (length/10)*math.cos(a_angle2)
        y2 = y_f + (length/10)*math.sin(a_angle2)
        p.drawLine(x_f, y_f, x1, y1)
        p.drawLine(x_f, y_f, x2, y2)

    # Load the Perlin Noise image and draw it with the painter
    p.drawPixmap(QRect(0, 0, width, height), QPixmap(p_path))

    # Now we're drawing red arrows for vectors, so set the pen color to red
    p.setPen(QColor(255, 0, 0))

    # We need arrow locations, so create a grid of n_vectors x n_vectors, excluding the image border
    _nx, _ny = n_vectors, n_vectors
    dx, dy = width / (_nx + 1), height / (_ny + 1)
    x_points = [dx + i*dx for i in range(_nx)]
    y_points = [dy + i*dy for i in range(_ny)]

    # Draw the arrows
    for x in x_points:
        for y in y_points:
            angle = 360*noise[int(x), int(y)]
            draw_arrow(p, x, y, length=min(dx, dy), angle=angle)

    # Save the vector image
    save(p, fname=v_path, folder='.')

    # Now draw the flow field. Start by initializing a new painter
    p = Painter.Painter(width, height)
    p.setRenderHint(p.Antialiasing)  # allow smooth drawing
    p.setPen(QColor(0, 0, 0))  # pen color set to black

    # Step size between points
    STEP_SIZE = 0.001 * max(width, height)

    # Draw the flow field
    for x in x_points:
        for y in y_points:
            # The starting position
            x_s, y_s = x, y
            # The current line length tracking variable
            c_len = 0
            while c_len < flow_length:
                # angle between 0 and 2*pi
                angle = 2 * noise[int(x_s), int(y_s)] * math.pi

                # Compute the new point
                x_f = x_s + STEP_SIZE * math.cos(angle)
                y_f = y_s - STEP_SIZE * math.sin(angle)

                # Draw the line
                p.drawLine(QPointF(x_s, y_s), QPointF(x_f, y_f))

                # Update the line length
                c_len += math.sqrt((x_f - x_s) ** 2 + (y_f - y_s) ** 2)

                # Break from the loop if the new point is outside our image bounds
                # or if we've exceeded the line length; otherwise update the point
                if x_f < 0 or x_f >= width or y_f < 0 or y_f >= height or c_len > flow_length:
                    break
                else:
                    x_s, y_s = x_f, y_f
    save(p, fname=f_path, folder='.')


def draw_flow_field(width, height, seed=random.randint(0, 100000000)):
    # Set the random seed for repeatability
    np.random.seed(seed)
    count=0
    # These are color hues
    colors = [200, 140, 70, 340, 280]
    for i, mod in enumerate(colors):
        print('Starting Image %s/%s' % (i + 1, len(colors)))
        p = Painter.Painter(width, height)

        # Allow smooth drawing
        p.setRenderHint(p.Antialiasing)

        # Draw the background color
        p.fillRect(0, 0, width, height, QColor(0, 0, 0))

        # Set the pen color
        p.setPen(QPen(QColor(150, 150, 225, 5), 2))

        num = 1
        for j in range(num):
            print('Creating Noise... (%s/%s)' % (j + 1, num))
            p_noise = Perlin2D(width, height, 2, 2)
            print('Noise Generated! (%s/%s)' % (j + 1, num))

            MAX_LENGTH = 2 * width
            STEP_SIZE = 0.001 * max(width, height)
            NUM = int(width * height / 1000)
            POINTS = [(random.randint(0, width - 1), random.randint(0, height - 1)) for i in range(NUM)]

            for k, (x_s, y_s) in enumerate(POINTS):
                print(f'{100 * (k + 1) / len(POINTS):.1f}'.rjust(5) + '% Complete', end='\r')

                # The current line length tracking variable
                c_len = 0

                # Actually draw the flow field
                while c_len < MAX_LENGTH:
                    # Set the pen color for this segment
                    sat = 200 * (MAX_LENGTH - c_len) / MAX_LENGTH
                    hue = (mod + 130 * (height - y_s) / height) % 360
                    p.setPen(QPen(QColor_HSV(hue, sat, 255, 20), 2))

                    # angle between -pi and pi
                    angle = p_noise[int(x_s), int(y_s)] * math.pi

                    # Compute the new point
                    x_f = x_s + STEP_SIZE * math.cos(angle)
                    y_f = y_s + STEP_SIZE * math.sin(angle)

                    # Draw the line
                    p.drawLine(QPointF(x_s, y_s), QPointF(x_f, y_f))

                    # Update the line length
                    c_len += math.sqrt((x_f - x_s) ** 2 + (y_f - y_s) ** 2)

                    # Break from the loop if the new point is outside our image bounds
                    # or if we've exceeded the line length; otherwise update the point
                    if x_f < 0 or x_f >= width or y_f < 0 or y_f >= height or c_len > MAX_LENGTH:
                        break
                    else:
                        x_s, y_s = x_f, y_f
                        count=count+1
                        scnt=str(count)
                    save(p, fname=f'image_i{scnt}_{mod}_{num}_{seed}', folder='newseries/', overwrite=True)


def draw_perlin_rounding(width, height, fname, seed=random.randint(0, 100000000)):
    # Ensure we don't overwrite paths
    count=0
    assert not os.path.exists(fname), 'Image already exists!'

    # Set the random seed for repeatability
    np.random.seed(seed)

    # Initialize a new painter
    p = Painter.Painter(width, height)
    p.setRenderHint(p.Antialiasing)

    # Draw the background color
    #p.fillRect(0, 0, width, height, QColor(0, 0, 0))
    p.fillRect(0, 0, width, height, QColor("darkRed"))

    # Set the pen color
    p.setPen(QColor(200, 200, 200))
    p.setPen(QColor("yellow"))

    print('Creating Noise...', end='', flush=True)
    noise = Perlin2D(width, height, 1, 1)
    print('Done!')

    # The maximum line length and step size
    MAX_LENGTH = 1000
    STEP_SIZE = 0.001 * max(width, height)

    # Compute a grid 200x200 points, centered in the screen
    dx, dy = width / (200 + 1), height / (200 + 1)
    POINTS = [[(i+1)*dx, (j+1)*dy] for i in range(200) for j in range(200)]

    for i, (x_s, y_s) in enumerate(POINTS):
        print(f'{100 * (i + 1) / len(POINTS):.1f}'.rjust(5) + '% Complete', end='\r')

        # The current line length tracking variable
        c_len = 0
        while c_len < MAX_LENGTH:
            # angle between -pi and pi
            angle = math.pi*noise[int(x_s), int(y_s)]

            # Round the angle to pi/4 increments
            angle = round(angle / (math.pi / 4)) * (math.pi / 4)

            # Compute the new point
            x_f = x_s + STEP_SIZE * math.cos(angle)
            y_f = y_s + STEP_SIZE * math.sin(angle)

            # Draw the line
            p.drawLine(x_s, y_s, x_f, y_f)

            # Update the line length
            c_len += math.sqrt((x_f - x_s) ** 2 + (y_f - y_s) ** 2)

            # Break from the loop if the new point is outside our image bounds
            # or if we've exceeded the line length; otherwise update the point
            if (x_f < 0 or x_f >= width or y_f < 0 or y_f >= height or
                    c_len > MAX_LENGTH):
                break
            else:
                x_s, y_s = x_f, y_f
                count=count+1
                scnt=str(count)

            
            save(p, fname=f'{scnt}_{fname}_{seed}', folder='newseries/')
            print("-",end=".")


class Body:
    def __init__(self, x, y, vx, vy):
        self._position = np.array([x, y], dtype=np.float64)
        self._velocity = np.array([vx, vy], dtype=np.float64)

    @property
    def position(self):
        return self._position

    @property
    def velocity(self):
        return self._velocity

    def update(self, dt):
        # update the body position
        self._position = self._position + dt*self._velocity


class ExpandingCircleRandom:
    def __init__(self, radius, num_bodies, center=(0, 0), v_limits=(-2, 2)):
        self._bodies = [Body(center[0] + radius*math.cos(i*2*math.pi/num_bodies),
                             center[1] + radius*math.sin(i*2*math.pi/num_bodies),
                             v_limits[0]+(v_limits[1]-v_limits[0])*random.random(),
                             v_limits[0]+(v_limits[1]-v_limits[0])*random.random()) for i in range(num_bodies)]

    def draw(self, dt, Painter):
        # Connect the dots between each body
        for i in range(len(self._bodies)):
            # Handle the wrapping case
            if i == len(self._bodies) - 1:
                p1 = QPointF(*self._bodies[i].position)
                p2 = QPointF(*self._bodies[0].position)
            else:
                p1 = QPointF(*self._bodies[i].position)
                p2 = QPointF(*self._bodies[i+1].position)
            Painter.drawLine(p1, p2)

        # Update the position of each body
        for i in range(len(self._bodies)):
            self._bodies[i].update(dt)


class ExpandingCircleNoise:
    def __init__(self, radius, num_bodies, noise, center=(0, 0), v_max=2):
        self._bodies = [Body(center[0] + radius*math.cos(i*2*math.pi/num_bodies),
                             center[1] + radius*math.sin(i*2*math.pi/num_bodies),
                             0, 0) for i in range(num_bodies)]
        self._v_max = v_max
        self._noise = noise

    def draw(self, dt, painter):
        # Connect the dots between each body
        for i in range(len(self._bodies)):
            # Handle the wrapping case
            if i == len(self._bodies) - 1:
                p1 = QPointF(*self._bodies[i].position)
                p2 = QPointF(*self._bodies[0].position)
            else:
                p1 = QPointF(*self._bodies[i].position)
                p2 = QPointF(*self._bodies[i + 1].position)
            painter.drawLine(p1, p2)

            # Try to update the velocity for each body. If we can't its because the point is beyond the noise
            # field we've created, so at that point, just maintain velocity.
            try:
                a = math.pi*self._noise[int(p1.x()), int(p1.y())]
                v = np.array([self._v_max*math.cos(a), self._v_max*math.sin(a)])
                self._bodies[i]._velocity = v
            except IndexError:
                pass

        # Update the position of each body
        for i in range(len(self._bodies)):
            self._bodies[i].update(dt)

def draw_delta_body(width, height, iterations = 1000,seed=random.randint(0, 100000000), mode='noise'):
    #def draw_delta_body(width, height, seed=random.randint(0, 100000000), mode='noise'):
    assert mode in ['noise', 'random'], 'Mode must either be "noise" or "random"'

    # Set the random seed for repeatability
    np.random.seed(seed)
    random.seed(seed)

    # Initialize the painter
    p = Painter.Painter(width, height)
    p.setRenderHint(p.Antialiasing)  # Allow smooth drawing

    # Draw the background color
    p.fillRect(0, 0, width, height, QColor("darkRed"))

    # Set the pen color
    p.setPen(QPen(QColor("yellow"), 1))

    # Initialize the expanding circle centered in the canvas
    if mode == 'random':
        circle = ExpandingCircleRandom(width/8, 100, center=(width/2, height/2), v_limits=(-2, 2))
    elif mode == 'noise':
        noise = Perlin2D(width, height, 5, 5)
        circle = ExpandingCircleNoise(width/6, 200, noise, center=(width/4, height/2), v_max=5)
    else:
        circle = None

    # Initialize the delta time we're applying to each update
    dt = 0.3

    #iterations = 2000
    for i in range(iterations):
        circle.draw(dt, p)
        save(p, fname=f'delta_{i}_{mode}_{seed}', folder='XXXX/', overwrite=True)
        print(".",end="-")


#cnt=1
#width= 1000
#height=1000
#fname = "newseries/VIDEO"+str(cnt)+"-.png"
#print(fname)
#draw_perlin_rounding(width, height, fname, seed=random.randint(0, 100000000))

width= 1000
height=1000
draw_delta_body(width, height, iterations = 1000,seed=random.randint(0, 100000000), mode='noise')

width= 1000
height=1000
draw_flow_field(width, height, seed=random.randint(0, 100000000))

draw_delta_body(width, height, iterations = 1000,seed=random.randint(0, 100000000), mode='noise')

