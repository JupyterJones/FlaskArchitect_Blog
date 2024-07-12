from imp import reload

import matplotlib
reload(matplotlib)

matplotlib.use('nbagg')

import matplotlib.backends.backend_nbagg
reload(matplotlib.backends.backend_nbagg)

import matplotlib.backends.backend_webagg_core
reload(matplotlib.backends.backend_webagg_core)

import matplotlib.pyplot as plt
plt.interactive(False)

fig1 = plt.figure()
plt.plot(range(10))

plt.show()

plt.plot([3, 2, 1])
plt.show()

print(matplotlib.backends.backend_nbagg.connection_info())

plt.close(fig1)

plt.plot(range(10))

print(matplotlib.backends.backend_nbagg.connection_info())

plt.show()
plt.figure()
plt.plot(range(5))
plt.show()

plt.interactive(True)
plt.figure()
plt.plot([3, 2, 1])

plt.plot(range(3))

print(matplotlib.backends.backend_nbagg.connection_info())

plt.interactive(False)

plt.gcf().canvas.manager.reshow()

fig = plt.figure()
plt.axes()
plt.show()

plt.plot([1, 2, 3])
plt.show()

from matplotlib.backends.backend_nbagg import new_figure_manager,show

manager = new_figure_manager(1000)
fig = manager.canvas.figure
ax = fig.add_subplot(1,1,1)
ax.plot([1,2,3])
fig.show()

import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)        # x-array
line, = ax.plot(x, np.sin(x))

def animate(i):
    line.set_ydata(np.sin(x+i/10.0))  # update the data
    return line,

#Init only required for blitting to give a clean slate.
def init():
    line.set_ydata(np.ma.array(x, mask=True))
    return line,

ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), init_func=init,
                              interval=32., blit=True)
plt.show()

import matplotlib
matplotlib.rcParams.update({'figure.facecolor': 'red',
                            'savefig.facecolor': 'yellow'})
plt.figure()
plt.plot([3, 2, 1])

plt.show()

import itertools
fig, ax = plt.subplots()
x = np.linspace(0,10,10000)
y = np.sin(x)
ln, = ax.plot(x,y)
evt = []
colors = iter(itertools.cycle(['r', 'g', 'b', 'k', 'c']))
def on_event(event):
    if event.name.startswith('key'):
        fig.suptitle('%s: %s' % (event.name, event.key))
    elif event.name == 'scroll_event':
        fig.suptitle('%s: %s' % (event.name, event.step))
    else:
        fig.suptitle('%s: %s' % (event.name, event.button))
    evt.append(event)
    ln.set_color(next(colors))
    fig.canvas.draw()
    fig.canvas.draw_idle()

fig.canvas.mpl_connect('button_press_event', on_event)
fig.canvas.mpl_connect('button_release_event', on_event)
fig.canvas.mpl_connect('scroll_event', on_event)
fig.canvas.mpl_connect('key_press_event', on_event)
fig.canvas.mpl_connect('key_release_event', on_event)

plt.show()

import time

fig, ax = plt.subplots()
text = ax.text(0.5, 0.5, '', ha='center')

def update(text):
    text.set(text=time.ctime())
    text.axes.figure.canvas.draw()
    
timer = fig.canvas.new_timer(500, [(update, [text], {})])
timer.start()
plt.show()

fig, ax = plt.subplots()
text = ax.text(0.5, 0.5, '', ha='center') 
timer = fig.canvas.new_timer(500, [(update, [text], {})])

timer.single_shot = True
timer.start()

plt.show()

fig, ax = plt.subplots()
text = ax.text(0.5, 0.5, '', ha='center')
timer = fig.canvas.new_timer(500, [(update, [text], {})])

timer.start()
timer.stop()

plt.show()

fig, ax = plt.subplots()
text = ax.text(0.5, 0.5, '', ha='center')
timer = fig.canvas.new_timer(500, [(update, [text], {})])

timer.single_shot = True
timer.start()
timer.stop()

plt.show()

fig, ax = plt.subplots()
ax.plot(range(5))
plt.show()

fig.canvas.manager.reshow()



