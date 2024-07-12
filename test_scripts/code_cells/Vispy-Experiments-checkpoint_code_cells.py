import vispy
back = ['pyqt4', 'pyqt5', 'pyside','jupyter_rfb','pyglet', 'glfw', 'sdl2', 'wx', 'egl', 'osmesa', 'ipynb_webgl', '_test']
vispy.use('pyqt5')

import legacycontour
from legacycontour import _cntr as cntr

import sys

from vispy import app, gloo
from vispy.visuals import CubeVisual, transforms


class Canvas(app.Canvas):
    def __init__(self):
        app.Canvas.__init__(self, 'Cube', keys='interactive',
                            size=(400, 400))

        self.cube = CubeVisual((1.0, 0.5, 0.25), color='red', edge_color="k")
        self.theta = 0
        self.phi = 0

        # Create a TransformSystem that will tell the visual how to draw
        self.cube_transform = transforms.MatrixTransform()
        self.cube.transform = self.cube_transform

        self.timer = app.Timer('auto', connect=self.on_timer, start=True)

    def on_resize(self, event):
        # Set canvas viewport and reconfigure visual transforms to match.
        vp = (0, 0, self.physical_size[0], self.physical_size[1])
        self.context.set_viewport(*vp)
        self.cube.transforms.configure(canvas=self, viewport=vp)

    def on_draw(self, event):
        gloo.set_viewport(0, 0, *self.physical_size)
        gloo.clear('white', depth=True)

        self.cube.draw()

    def on_timer(self, event):
        self.theta += .5
        self.phi += .5
        self.cube_transform.reset()
        self.cube_transform.rotate(self.theta, (0, 0, 1))
        self.cube_transform.rotate(self.phi, (0, 1, 0))
        self.cube_transform.scale((100, 100, 0.001))
        self.cube_transform.translate((200, 200))
        self.update()


win = Canvas()
win.show()
win

from fractions import gcd

from math import gcd

# %load ~/miniconda3/envs/cloned_base/lib/python3.9/site-packages/vispy/app/canvas.py
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

from __future__ import division, print_function

import sys
import numpy as np
from time import sleep

from ..util.event import EmitterGroup, Event, WarningEmitter
from ..util.ptime import time
from ..util.dpi import get_dpi
from ..util import config as util_config
from ..ext.six import string_types
from . import Application, use_app
from ..gloo.context import (GLContext, set_current_canvas, forget_canvas)
from ..gloo import FrameBuffer, RenderBuffer


# todo: add functions for asking about current mouse/keyboard state
# todo: add hover enter/exit events
# todo: add focus events


class Canvas(object):
    """Representation of a GUI element with an OpenGL context

    Parameters
    ----------
    title : str
        The widget title
    size : (width, height)
        The size of the window.
    position : (x, y)
        The position of the window in screen coordinates.
    show : bool
        Whether to show the widget immediately. Default False.
    autoswap : bool
        Whether to swap the buffers automatically after a draw event.
        Default True. If True, the ``swap_buffers`` Canvas method will
        be called last (by default) by the ``canvas.draw`` event handler.
    app : Application | str
        Give vispy Application instance to use as a backend.
        (vispy.app is used by default.) If str, then an application
        using the chosen backend (e.g., 'pyglet') will be created.
        Note the canvas application can be accessed at ``canvas.app``.
    create_native : bool
        Whether to create the widget immediately. Default True.
    vsync : bool
        Enable vertical synchronization.
    resizable : bool
        Allow the window to be resized.
    decorate : bool
        Decorate the window. Default True.
    fullscreen : bool | int
        If False, windowed mode is used (default). If True, the default
        monitor is used. If int, the given monitor number is used.
    config : dict
        A dict with OpenGL configuration options, which is combined
        with the default configuration options and used to initialize
        the context. See ``canvas.context.config`` for possible
        options.
    shared : Canvas | GLContext | None
        An existing canvas or context to share OpenGL objects with.
    keys : str | dict | None
        Default key mapping to use. If 'interactive', escape and F11 will
        close the canvas and toggle full-screen mode, respectively.
        If dict, maps keys to functions. If dict values are strings,
        they are assumed to be ``Canvas`` methods, otherwise they should
        be callable.
    parent : widget-object
        The parent widget if this makes sense for the used backend.
    dpi : float | None
        Resolution in dots-per-inch to use for the canvas. If dpi is None,
        then the value will be determined by querying the global config first,
        and then the operating system.
    always_on_top : bool
        If True, try to create the window in always-on-top mode.
    px_scale : int > 0
        A scale factor to apply between logical and physical pixels in addition
        to the actual scale factor determined by the backend. This option
        allows the scale factor to be adjusted for testing.

    Notes
    -----
    The `Canvas` receives the following events:

        * initialize
        * resize
        * draw
        * mouse_press
        * mouse_release
        * mouse_double_click
        * mouse_move
        * mouse_wheel
        * key_press
        * key_release
        * stylus
        * touch
        * close

    The ordering of the mouse_double_click, mouse_press, and mouse_release
    events are not guaranteed to be consistent between backends. Only certain
    backends natively support double-clicking (currently Qt and WX); on other
    backends, they are detected manually with a fixed time delay.
    This can cause problems with accessibility, as increasing the OS detection
    time or using a dedicated double-click button will not be respected.
    """

    def __init__(self, title='VisPy canvas', size=(800, 600), position=None,
                 show=False, autoswap=True, app=None, create_native=True,
                 vsync=False, resizable=True, decorate=True, fullscreen=False,
                 config=None, shared=None, keys=None, parent=None, dpi=None,
                 always_on_top=False, px_scale=1):

        size = tuple(int(s) * px_scale for s in size)
        if len(size) != 2:
            raise ValueError('size must be a 2-element list')
        title = str(title)
        if not isinstance(fullscreen, (bool, int)):
            raise TypeError('fullscreen must be bool or int')

        # Initialize some values
        self._autoswap = autoswap
        self._title = title
        self._frame_count = 0
        self._fps = 0
        self._basetime = time()
        self._fps_callback = None
        self._backend = None
        self._closed = False
        self._fps_window = 0.
        self._px_scale = int(px_scale)

        if dpi is None:
            dpi = util_config['dpi']
        if dpi is None:
            dpi = get_dpi(raise_error=False)
        self.dpi = dpi

        # Create events
        self.events = EmitterGroup(source=self,
                                   initialize=Event,
                                   resize=ResizeEvent,
                                   draw=DrawEvent,
                                   mouse_press=MouseEvent,
                                   mouse_release=MouseEvent,
                                   mouse_double_click=MouseEvent,
                                   mouse_move=MouseEvent,
                                   mouse_wheel=MouseEvent,
                                   key_press=KeyEvent,
                                   key_release=KeyEvent,
                                   stylus=Event,
                                   touch=Event,
                                   close=Event)

        # Deprecated paint emitter
        emitter = WarningEmitter('Canvas.events.paint and Canvas.on_paint are '
                                 'deprecated; use Canvas.events.draw and '
                                 'Canvas.on_draw instead.',
                                 source=self, type='draw',
                                 event_class=DrawEvent)
        self.events.add(paint=emitter)
        self.events.draw.connect(self.events.paint)

        # Get app instance
        if app is None:
            self._app = use_app(call_reuse=False)
        elif isinstance(app, Application):
            self._app = app
        elif isinstance(app, string_types):
            self._app = Application(app)
        else:
            raise ValueError('Invalid value for app %r' % app)

        # Check shared and context
        if shared is None:
            pass
        elif isinstance(shared, Canvas):
            shared = shared.context.shared
        elif isinstance(shared, GLContext):
            shared = shared.shared
        else:
            raise TypeError('shared must be a Canvas, not %s' % type(shared))
        config = config or {}
        if not isinstance(config, dict):
            raise TypeError('config must be a dict, not %s' % type(config))

        # Create new context
        self._context = GLContext(config, shared)

        # Deal with special keys
        self._set_keys(keys)

        # store arguments that get set on Canvas init
        kwargs = dict(title=title, size=size, position=position, show=show,
                      vsync=vsync, resizable=resizable, decorate=decorate,
                      fullscreen=fullscreen, context=self._context,
                      parent=parent, always_on_top=always_on_top)
        self._backend_kwargs = kwargs

        # Create widget now (always do this *last*, after all err checks)
        if create_native:
            self.create_native()

            # Now we're ready to become current
            self.set_current()

        if '--vispy-fps' in sys.argv:
            self.measure_fps()

    def create_native(self):
        """ Create the native widget if not already done so. If the widget
        is already created, this function does nothing.
        """
        if self._backend is not None:
            return
        # Make sure that the app is active
        assert self._app.native
        # Instantiate the backend with the right class
        self._app.backend_module.CanvasBackend(self, **self._backend_kwargs)
        # self._backend = set by BaseCanvasBackend
        self._backend_kwargs = None  # Clean up

        # Connect to draw event (append to the end)
        # Process GLIR commands at each paint event
        self.events.draw.connect(self.context.flush_commands, position='last')
        if self._autoswap:
            self.events.draw.connect((self, 'swap_buffers'),
                                     ref=True, position='last')

    def _set_keys(self, keys):
        if keys is not None:
            if isinstance(keys, string_types):
                if keys != 'interactive':
                    raise ValueError('keys, if string, must be "interactive", '
                                     'not %s' % (keys,))

                def toggle_fs():
                    self.fullscreen = not self.fullscreen
                keys = dict(escape='close', F11=toggle_fs)
        else:
            keys = {}
        if not isinstance(keys, dict):
            raise TypeError('keys must be a dict, str, or None')
        if len(keys) > 0:
            # ensure all are callable
            for key, val in keys.items():
                if isinstance(val, string_types):
                    new_val = getattr(self, val, None)
                    if new_val is None:
                        raise ValueError('value %s is not an attribute of '
                                         'Canvas' % val)
                    val = new_val
                if not hasattr(val, '__call__'):
                    raise TypeError('Entry for key %s is not callable' % key)
                # convert to lower-case representation
                keys.pop(key)
                keys[key.lower()] = val
            self._keys_check = keys

            def keys_check(event):
                if event.key is not None:
                    use_name = event.key.name.lower()
                    if use_name in self._keys_check:
                        self._keys_check[use_name]()
            self.events.key_press.connect(keys_check, ref=True)

    @property
    def context(self):
        """ The OpenGL context of the native widget

        It gives access to OpenGL functions to call on this canvas object,
        and to the shared context namespace.
        """
        return self._context

    @property
    def app(self):
        """ The vispy Application instance on which this Canvas is based.
        """
        return self._app

    @property
    def native(self):
        """ The native widget object on which this Canvas is based.
        """
        return self._backend._vispy_get_native_canvas()

    @property
    def dpi(self):
        """ The physical resolution of the canvas in dots per inch.
        """
        return self._dpi

    @dpi.setter
    def dpi(self, dpi):
        self._dpi = float(dpi)
        self.update()

    def connect(self, fun):
        """ Connect a function to an event

        The name of the function
        should be on_X, with X the name of the event (e.g. 'on_draw').

        This method is typically used as a decorator on a function
        definition for an event handler.

        Parameters
        ----------
        fun : callable
            The function.
        """
        # Get and check name
        name = fun.__name__
        if not name.startswith('on_'):
            raise ValueError('When connecting a function based on its name, '
                             'the name should start with "on_"')
        eventname = name[3:]
        # Get emitter
        try:
            emitter = self.events[eventname]
        except KeyError:
            raise ValueError(
                'Event "%s" not available on this canvas.' %
                eventname)
        # Connect
        emitter.connect(fun)

    # ---------------------------------------------------------------- size ---
    @property
    def size(self):
        """ The size of canvas/window """
        size = self._backend._vispy_get_size()
        return (size[0] // self._px_scale, size[1] // self._px_scale)

    @size.setter
    def size(self, size):
        return self._backend._vispy_set_size(size[0] * self._px_scale,
                                             size[1] * self._px_scale)

    @property
    def physical_size(self):
        """ The physical size of the canvas/window, which may differ from the
        size property on backends that expose HiDPI """
        return self._backend._vispy_get_physical_size()

    @property
    def pixel_scale(self):
        """ The ratio between the number of logical pixels, or 'points', and
        the physical pixels on the device. In most cases this will be 1.0,
        but on certain backends this will be greater than 1. This should be
        used as a scaling factor when writing your own visualisations
        with gloo (make a copy and multiply all your logical pixel values
        by it). When writing Visuals or SceneGraph visualisations, this value
        is exposed as `TransformSystem.px_scale`."""
        return self.physical_size[0] // self.size[0]

    @property
    def fullscreen(self):
        return self._backend._vispy_get_fullscreen()

    @fullscreen.setter
    def fullscreen(self, fullscreen):
        return self._backend._vispy_set_fullscreen(fullscreen)

    # ------------------------------------------------------------ position ---
    @property
    def position(self):
        """ The position of canvas/window relative to screen """
        return self._backend._vispy_get_position()

    @position.setter
    def position(self, position):
        assert len(position) == 2
        return self._backend._vispy_set_position(position[0], position[1])

    # --------------------------------------------------------------- title ---
    @property
    def title(self):
        """ The title of canvas/window """
        return self._title

    @title.setter
    def title(self, title):
        self._title = title
        self._backend._vispy_set_title(title)

    # ----------------------------------------------------------------- fps ---
    @property
    def fps(self):
        """The fps of canvas/window, as the rate that events.draw is emitted
        """
        return self._fps

    def set_current(self, event=None):
        """Make this the active GL canvas

        Parameters
        ----------
        event : None
            Not used.
        """
        self._backend._vispy_set_current()
        set_current_canvas(self)

    def swap_buffers(self, event=None):
        """Swap GL buffers such that the offscreen buffer becomes visible

        Parameters
        ----------
        event : None
            Not used.
        """
        self._backend._vispy_swap_buffers()

    def show(self, visible=True, run=False):
        """Show or hide the canvas

        Parameters
        ----------
        visible : bool
            Make the canvas visible.
        run : bool
            Run the backend event loop.
        """
        self._backend._vispy_set_visible(visible)
        if run:
            self.app.run()

    def update(self, event=None):
        """Inform the backend that the Canvas needs to be redrawn

        Parameters
        ----------
        event : None
            Not used.
        """
        if self._backend is not None:
            self._backend._vispy_update()

    def close(self):
        """Close the canvas

        Notes
        -----
        This will usually destroy the GL context. For Qt, the context
        (and widget) will be destroyed only if the widget is top-level.
        To avoid having the widget destroyed (more like standard Qt
        behavior), consider making the widget a sub-widget.
        """
        if self._backend is not None and not self._closed:
            self._closed = True
            self.events.close()
            self._backend._vispy_close()
        forget_canvas(self)

    def _update_fps(self, event):
        """Update the fps after every window"""
        self._frame_count += 1
        diff = time() - self._basetime
        if (diff > self._fps_window):
            self._fps = self._frame_count / diff
            self._basetime = time()
            self._frame_count = 0
            self._fps_callback(self.fps)

    def measure_fps(self, window=1, callback='%1.1f FPS'):
        """Measure the current FPS

        Sets the update window, connects the draw event to update_fps
        and sets the callback function.

        Parameters
        ----------
        window : float
            The time-window (in seconds) to calculate FPS. Default 1.0.
        callback : function | str
            The function to call with the float FPS value, or the string
            to be formatted with the fps value and then printed. The
            default is ``'%1.1f FPS'``. If callback evaluates to False, the
            FPS measurement is stopped.
        """
        # Connect update_fps function to draw
        self.events.draw.disconnect(self._update_fps)
        if callback:
            if isinstance(callback, string_types):
                callback_str = callback  # because callback gets overwritten

                def callback(x):
                    print(callback_str % x)

            self._fps_window = window
            self.events.draw.connect(self._update_fps)
            self._fps_callback = callback
        else:
            self._fps_callback = None

    # ---------------------------------------------------------------- misc ---
    def __repr__(self):
        return ('<%s (%s) at %s>'
                % (self.__class__.__name__,
                   self.app.backend_name, hex(id(self))))

    def __enter__(self):
        self.show()
        self._backend._vispy_warmup()
        return self

    def __exit__(self, type, value, traceback):
        # ensure all GL calls are complete
        if not self._closed:
            self._backend._vispy_set_current()
            self.context.finish()
            self.close()
        sleep(0.1)  # ensure window is really closed/destroyed

    def render(self):
        """ Render the canvas to an offscreen buffer and return the image
        array.

        Returns
        -------
        image : array
            Numpy array of type ubyte and shape (h, w, 4). Index [0, 0] is the 
            upper-left corner of the rendered region.
        
        """
        self.set_current()
        size = self.physical_size
        fbo = FrameBuffer(color=RenderBuffer(size[::-1]),
                          depth=RenderBuffer(size[::-1]))

        try:
            fbo.activate()
            self.events.draw()
            return fbo.read()
        finally:
            fbo.deactivate()


# Event subclasses specific to the Canvas
class MouseEvent(Event):
    """Mouse event class

    Note that each event object has an attribute for each of the input
    arguments listed below, as well as a "time" attribute with the event's
    precision start time.

    Parameters
    ----------
    type : str
       String indicating the event type (e.g. mouse_press, key_release)
    pos : (int, int)
        The position of the mouse (in screen coordinates).
    button : int | None
        The button that generated this event (can be None).
        Left=1, right=2, middle=3. During a mouse drag, this
        will return the button that started the drag (same thing as
        ``event.press_event.button``).
    buttons : [int, ...]
        The list of buttons depressed during this event.
    modifiers : tuple of Key instances
        Tuple that specifies which modifier keys were pressed down at the
        time of the event (shift, control, alt, meta).
    delta : (float, float)
        The amount of scrolling in horizontal and vertical direction. One
        "tick" corresponds to a delta of 1.0.
    press_event : MouseEvent
        The press event that was generated at the start of the current drag,
        if any.
    last_event : MouseEvent
        The MouseEvent immediately preceding the current event. During drag
        operations, all generated events retain their last_event properties,
        allowing the entire drag to be reconstructed.
    native : object (optional)
       The native GUI event object
    **kwargs : keyword arguments
        All extra keyword arguments become attributes of the event object.
    """

    def __init__(self, type, pos=None, button=None, buttons=None,
                 modifiers=None, delta=None, last_event=None, press_event=None,
                 **kwargs):
        Event.__init__(self, type, **kwargs)
        self._pos = np.array([0, 0]) if (pos is None) else np.array(pos)
        self._button = int(button) if (button is not None) else None
        self._buttons = [] if (buttons is None) else buttons
        self._modifiers = tuple(modifiers or ())
        self._delta = np.zeros(2) if (delta is None) else np.array(delta)
        self._last_event = last_event
        self._press_event = press_event
        self._time = time()

    @property
    def pos(self):
        return self._pos

    @property
    def button(self):
        return self._button

    @property
    def buttons(self):
        return self._buttons

    @property
    def modifiers(self):
        return self._modifiers

    @property
    def delta(self):
        return self._delta

    @property
    def press_event(self):
        return self._press_event

    @property
    def last_event(self):
        return self._last_event

    @property
    def time(self):
        return self._time

    def _forget_last_event(self):
        # Needed to break otherwise endless last-event chains
        self._last_event = None

    @property
    def is_dragging(self):
        """ Indicates whether this event is part of a mouse drag operation.
        """
        return self.press_event is not None

    def drag_events(self):
        """ Return a list of all mouse events in the current drag operation.

        Returns None if there is no current drag operation.
        """
        if not self.is_dragging:
            return None

        event = self
        events = []
        while True:
            # mouse_press events can only be the start of a trail
            if event is None or event.type == 'mouse_press':
                break
            events.append(event)
            event = event.last_event

        return events[::-1]

    def trail(self):
        """ Return an (N, 2) array of mouse coordinates for every event in the
        current mouse drag operation.

        Returns None if there is no current drag operation.
        """
        events = self.drag_events()
        if events is None:
            return None

        trail = np.empty((len(events), 2), dtype=int)
        for i, ev in enumerate(events):
            trail[i] = ev.pos

        return trail


class KeyEvent(Event):
    """Key event class

    Note that each event object has an attribute for each of the input
    arguments listed below.

    Parameters
    ----------
    type : str
       String indicating the event type (e.g. mouse_press, key_release)
    key : vispy.keys.Key instance
        The Key object for this event. Can be compared to string names.
    text : str
        The text representation of the key (can be an empty string).
    modifiers : tuple of Key instances
        Tuple that specifies which modifier keys were pressed down at the
        time of the event (shift, control, alt, meta).
    native : object (optional)
       The native GUI event object
    **kwargs : keyword arguments
        All extra keyword arguments become attributes of the event object.
    """

    def __init__(self, type, key=None, text='', modifiers=None, **kwargs):
        Event.__init__(self, type, **kwargs)
        self._key = key
        self._text = text
        self._modifiers = tuple(modifiers or ())

    @property
    def key(self):
        return self._key

    @property
    def text(self):
        return self._text

    @property
    def modifiers(self):
        return self._modifiers


class ResizeEvent(Event):
    """Resize event class

    Note that each event object has an attribute for each of the input
    arguments listed below.

    Parameters
    ----------
    type : str
       String indicating the event type (e.g. mouse_press, key_release)
    size : (int, int)
        The new size of the Canvas, in points (logical pixels).
    physical_size : (int, int)
        The new physical size of the Canvas, in pixels.
    native : object (optional)
       The native GUI event object
    **kwargs : extra keyword arguments
        All extra keyword arguments become attributes of the event object.
    """

    def __init__(self, type, size=None, physical_size=None, **kwargs):
        Event.__init__(self, type, **kwargs)
        self._size = tuple(size)
        if physical_size is None:
            self._physical_size = self._size
        else:
            self._physical_size = tuple(physical_size)

    @property
    def size(self):
        return self._size

    @property
    def physical_size(self):
        return self._physical_size


class DrawEvent(Event):
    """Draw event class

    This type of event is sent to Canvas.events.draw when a redraw
    is required.

    Note that each event object has an attribute for each of the input
    arguments listed below.

    Parameters
    ----------
    type : str
       String indicating the event type (e.g. mouse_press, key_release)
    region : (int, int, int, int) or None
        The region of the canvas which needs to be redrawn (x, y, w, h).
        If None, the entire canvas must be redrawn.
    native : object (optional)
       The native GUI event object
    **kwargs : extra keyword arguments
        All extra keyword arguments become attributes of the event object.
    """

    def __init__(self, type, region=None, **kwargs):
        Event.__init__(self, type, **kwargs)
        self._region = region

    @property
    def region(self):
        return self._region


# %load /home/jack/miniconda3/envs/cloned_base/lib/python3.9/fractions.py
# Originally contributed by Sjoerd Mullender.
# Significantly modified by Jeffrey Yasskin <jyasskin at gmail.com>.

"""Fraction, infinite-precision, real numbers."""

from decimal import Decimal
import math
import numbers
import operator
import re
import sys

__all__ = ['Fraction']


# Constants related to the hash implementation;  hash(x) is based
# on the reduction of x modulo the prime _PyHASH_MODULUS.
_PyHASH_MODULUS = sys.hash_info.modulus
# Value to be used for rationals that reduce to infinity modulo
# _PyHASH_MODULUS.
_PyHASH_INF = sys.hash_info.inf

_RATIONAL_FORMAT = re.compile(r"""
    \A\s*                      # optional whitespace at the start, then
    (?P<sign>[-+]?)            # an optional sign, then
    (?=\d|\.\d)                # lookahead for digit or .digit
    (?P<num>\d*)               # numerator (possibly empty)
    (?:                        # followed by
       (?:/(?P<denom>\d+))?    # an optional denominator
    |                          # or
       (?:\.(?P<decimal>\d*))? # an optional fractional part
       (?:E(?P<exp>[-+]?\d+))? # and optional exponent
    )
    \s*\Z                      # and optional whitespace to finish
""", re.VERBOSE | re.IGNORECASE)


class Fraction(numbers.Rational):
    """This class implements rational numbers.

    In the two-argument form of the constructor, Fraction(8, 6) will
    produce a rational number equivalent to 4/3. Both arguments must
    be Rational. The numerator defaults to 0 and the denominator
    defaults to 1 so that Fraction(3) == 3 and Fraction() == 0.

    Fractions can also be constructed from:

      - numeric strings similar to those accepted by the
        float constructor (for example, '-2.3' or '1e10')

      - strings of the form '123/456'

      - float and Decimal instances

      - other Rational instances (including integers)

    """

    __slots__ = ('_numerator', '_denominator')

    # We're immutable, so use __new__ not __init__
    def __new__(cls, numerator=0, denominator=None, *, _normalize=True):
        """Constructs a Rational.

        Takes a string like '3/2' or '1.5', another Rational instance, a
        numerator/denominator pair, or a float.

        Examples
        --------

        >>> Fraction(10, -8)
        Fraction(-5, 4)
        >>> Fraction(Fraction(1, 7), 5)
        Fraction(1, 35)
        >>> Fraction(Fraction(1, 7), Fraction(2, 3))
        Fraction(3, 14)
        >>> Fraction('314')
        Fraction(314, 1)
        >>> Fraction('-35/4')
        Fraction(-35, 4)
        >>> Fraction('3.1415') # conversion from numeric string
        Fraction(6283, 2000)
        >>> Fraction('-47e-2') # string may include a decimal exponent
        Fraction(-47, 100)
        >>> Fraction(1.47)  # direct construction from float (exact conversion)
        Fraction(6620291452234629, 4503599627370496)
        >>> Fraction(2.25)
        Fraction(9, 4)
        >>> Fraction(Decimal('1.47'))
        Fraction(147, 100)

        """
        self = super(Fraction, cls).__new__(cls)

        if denominator is None:
            if type(numerator) is int:
                self._numerator = numerator
                self._denominator = 1
                return self

            elif isinstance(numerator, numbers.Rational):
                self._numerator = numerator.numerator
                self._denominator = numerator.denominator
                return self

            elif isinstance(numerator, (float, Decimal)):
                # Exact conversion
                self._numerator, self._denominator = numerator.as_integer_ratio()
                return self

            elif isinstance(numerator, str):
                # Handle construction from strings.
                m = _RATIONAL_FORMAT.match(numerator)
                if m is None:
                    raise ValueError('Invalid literal for Fraction: %r' %
                                     numerator)
                numerator = int(m.group('num') or '0')
                denom = m.group('denom')
                if denom:
                    denominator = int(denom)
                else:
                    denominator = 1
                    decimal = m.group('decimal')
                    if decimal:
                        scale = 10**len(decimal)
                        numerator = numerator * scale + int(decimal)
                        denominator *= scale
                    exp = m.group('exp')
                    if exp:
                        exp = int(exp)
                        if exp >= 0:
                            numerator *= 10**exp
                        else:
                            denominator *= 10**-exp
                if m.group('sign') == '-':
                    numerator = -numerator

            else:
                raise TypeError("argument should be a string "
                                "or a Rational instance")

        elif type(numerator) is int is type(denominator):
            pass # *very* normal case

        elif (isinstance(numerator, numbers.Rational) and
            isinstance(denominator, numbers.Rational)):
            numerator, denominator = (
                numerator.numerator * denominator.denominator,
                denominator.numerator * numerator.denominator
                )
        else:
            raise TypeError("both arguments should be "
                            "Rational instances")

        if denominator == 0:
            raise ZeroDivisionError('Fraction(%s, 0)' % numerator)
        if _normalize:
            g = math.gcd(numerator, denominator)
            if denominator < 0:
                g = -g
            numerator //= g
            denominator //= g
        self._numerator = numerator
        self._denominator = denominator
        return self

    @classmethod
    def from_float(cls, f):
        """Converts a finite float to a rational number, exactly.

        Beware that Fraction.from_float(0.3) != Fraction(3, 10).

        """
        if isinstance(f, numbers.Integral):
            return cls(f)
        elif not isinstance(f, float):
            raise TypeError("%s.from_float() only takes floats, not %r (%s)" %
                            (cls.__name__, f, type(f).__name__))
        return cls(*f.as_integer_ratio())

    @classmethod
    def from_decimal(cls, dec):
        """Converts a finite Decimal instance to a rational number, exactly."""
        from decimal import Decimal
        if isinstance(dec, numbers.Integral):
            dec = Decimal(int(dec))
        elif not isinstance(dec, Decimal):
            raise TypeError(
                "%s.from_decimal() only takes Decimals, not %r (%s)" %
                (cls.__name__, dec, type(dec).__name__))
        return cls(*dec.as_integer_ratio())

    def as_integer_ratio(self):
        """Return the integer ratio as a tuple.

        Return a tuple of two integers, whose ratio is equal to the
        Fraction and with a positive denominator.
        """
        return (self._numerator, self._denominator)

    def limit_denominator(self, max_denominator=1000000):
        """Closest Fraction to self with denominator at most max_denominator.

        >>> Fraction('3.141592653589793').limit_denominator(10)
        Fraction(22, 7)
        >>> Fraction('3.141592653589793').limit_denominator(100)
        Fraction(311, 99)
        >>> Fraction(4321, 8765).limit_denominator(10000)
        Fraction(4321, 8765)

        """
        # Algorithm notes: For any real number x, define a *best upper
        # approximation* to x to be a rational number p/q such that:
        #
        #   (1) p/q >= x, and
        #   (2) if p/q > r/s >= x then s > q, for any rational r/s.
        #
        # Define *best lower approximation* similarly.  Then it can be
        # proved that a rational number is a best upper or lower
        # approximation to x if, and only if, it is a convergent or
        # semiconvergent of the (unique shortest) continued fraction
        # associated to x.
        #
        # To find a best rational approximation with denominator <= M,
        # we find the best upper and lower approximations with
        # denominator <= M and take whichever of these is closer to x.
        # In the event of a tie, the bound with smaller denominator is
        # chosen.  If both denominators are equal (which can happen
        # only when max_denominator == 1 and self is midway between
        # two integers) the lower bound---i.e., the floor of self, is
        # taken.

        if max_denominator < 1:
            raise ValueError("max_denominator should be at least 1")
        if self._denominator <= max_denominator:
            return Fraction(self)

        p0, q0, p1, q1 = 0, 1, 1, 0
        n, d = self._numerator, self._denominator
        while True:
            a = n//d
            q2 = q0+a*q1
            if q2 > max_denominator:
                break
            p0, q0, p1, q1 = p1, q1, p0+a*p1, q2
            n, d = d, n-a*d

        k = (max_denominator-q0)//q1
        bound1 = Fraction(p0+k*p1, q0+k*q1)
        bound2 = Fraction(p1, q1)
        if abs(bound2 - self) <= abs(bound1-self):
            return bound2
        else:
            return bound1

    @property
    def numerator(a):
        return a._numerator

    @property
    def denominator(a):
        return a._denominator

    def __repr__(self):
        """repr(self)"""
        return '%s(%s, %s)' % (self.__class__.__name__,
                               self._numerator, self._denominator)

    def __str__(self):
        """str(self)"""
        if self._denominator == 1:
            return str(self._numerator)
        else:
            return '%s/%s' % (self._numerator, self._denominator)

    def _operator_fallbacks(monomorphic_operator, fallback_operator):
        """Generates forward and reverse operators given a purely-rational
        operator and a function from the operator module.

        Use this like:
        __op__, __rop__ = _operator_fallbacks(just_rational_op, operator.op)

        In general, we want to implement the arithmetic operations so
        that mixed-mode operations either call an implementation whose
        author knew about the types of both arguments, or convert both
        to the nearest built in type and do the operation there. In
        Fraction, that means that we define __add__ and __radd__ as:

            def __add__(self, other):
                # Both types have numerators/denominator attributes,
                # so do the operation directly
                if isinstance(other, (int, Fraction)):
                    return Fraction(self.numerator * other.denominator +
                                    other.numerator * self.denominator,
                                    self.denominator * other.denominator)
                # float and complex don't have those operations, but we
                # know about those types, so special case them.
                elif isinstance(other, float):
                    return float(self) + other
                elif isinstance(other, complex):
                    return complex(self) + other
                # Let the other type take over.
                return NotImplemented

            def __radd__(self, other):
                # radd handles more types than add because there's
                # nothing left to fall back to.
                if isinstance(other, numbers.Rational):
                    return Fraction(self.numerator * other.denominator +
                                    other.numerator * self.denominator,
                                    self.denominator * other.denominator)
                elif isinstance(other, Real):
                    return float(other) + float(self)
                elif isinstance(other, Complex):
                    return complex(other) + complex(self)
                return NotImplemented


        There are 5 different cases for a mixed-type addition on
        Fraction. I'll refer to all of the above code that doesn't
        refer to Fraction, float, or complex as "boilerplate". 'r'
        will be an instance of Fraction, which is a subtype of
        Rational (r : Fraction <: Rational), and b : B <:
        Complex. The first three involve 'r + b':

            1. If B <: Fraction, int, float, or complex, we handle
               that specially, and all is well.
            2. If Fraction falls back to the boilerplate code, and it
               were to return a value from __add__, we'd miss the
               possibility that B defines a more intelligent __radd__,
               so the boilerplate should return NotImplemented from
               __add__. In particular, we don't handle Rational
               here, even though we could get an exact answer, in case
               the other type wants to do something special.
            3. If B <: Fraction, Python tries B.__radd__ before
               Fraction.__add__. This is ok, because it was
               implemented with knowledge of Fraction, so it can
               handle those instances before delegating to Real or
               Complex.

        The next two situations describe 'b + r'. We assume that b
        didn't know about Fraction in its implementation, and that it
        uses similar boilerplate code:

            4. If B <: Rational, then __radd_ converts both to the
               builtin rational type (hey look, that's us) and
               proceeds.
            5. Otherwise, __radd__ tries to find the nearest common
               base ABC, and fall back to its builtin type. Since this
               class doesn't subclass a concrete type, there's no
               implementation to fall back to, so we need to try as
               hard as possible to return an actual value, or the user
               will get a TypeError.

        """
        def forward(a, b):
            if isinstance(b, (int, Fraction)):
                return monomorphic_operator(a, b)
            elif isinstance(b, float):
                return fallback_operator(float(a), b)
            elif isinstance(b, complex):
                return fallback_operator(complex(a), b)
            else:
                return NotImplemented
        forward.__name__ = '__' + fallback_operator.__name__ + '__'
        forward.__doc__ = monomorphic_operator.__doc__

        def reverse(b, a):
            if isinstance(a, numbers.Rational):
                # Includes ints.
                return monomorphic_operator(a, b)
            elif isinstance(a, numbers.Real):
                return fallback_operator(float(a), float(b))
            elif isinstance(a, numbers.Complex):
                return fallback_operator(complex(a), complex(b))
            else:
                return NotImplemented
        reverse.__name__ = '__r' + fallback_operator.__name__ + '__'
        reverse.__doc__ = monomorphic_operator.__doc__

        return forward, reverse

    def _add(a, b):
        """a + b"""
        da, db = a.denominator, b.denominator
        return Fraction(a.numerator * db + b.numerator * da,
                        da * db)

    __add__, __radd__ = _operator_fallbacks(_add, operator.add)

    def _sub(a, b):
        """a - b"""
        da, db = a.denominator, b.denominator
        return Fraction(a.numerator * db - b.numerator * da,
                        da * db)

    __sub__, __rsub__ = _operator_fallbacks(_sub, operator.sub)

    def _mul(a, b):
        """a * b"""
        return Fraction(a.numerator * b.numerator, a.denominator * b.denominator)

    __mul__, __rmul__ = _operator_fallbacks(_mul, operator.mul)

    def _div(a, b):
        """a / b"""
        return Fraction(a.numerator * b.denominator,
                        a.denominator * b.numerator)

    __truediv__, __rtruediv__ = _operator_fallbacks(_div, operator.truediv)

    def _floordiv(a, b):
        """a // b"""
        return (a.numerator * b.denominator) // (a.denominator * b.numerator)

    __floordiv__, __rfloordiv__ = _operator_fallbacks(_floordiv, operator.floordiv)

    def _divmod(a, b):
        """(a // b, a % b)"""
        da, db = a.denominator, b.denominator
        div, n_mod = divmod(a.numerator * db, da * b.numerator)
        return div, Fraction(n_mod, da * db)

    __divmod__, __rdivmod__ = _operator_fallbacks(_divmod, divmod)

    def _mod(a, b):
        """a % b"""
        da, db = a.denominator, b.denominator
        return Fraction((a.numerator * db) % (b.numerator * da), da * db)

    __mod__, __rmod__ = _operator_fallbacks(_mod, operator.mod)

    def __pow__(a, b):
        """a ** b

        If b is not an integer, the result will be a float or complex
        since roots are generally irrational. If b is an integer, the
        result will be rational.

        """
        if isinstance(b, numbers.Rational):
            if b.denominator == 1:
                power = b.numerator
                if power >= 0:
                    return Fraction(a._numerator ** power,
                                    a._denominator ** power,
                                    _normalize=False)
                elif a._numerator >= 0:
                    return Fraction(a._denominator ** -power,
                                    a._numerator ** -power,
                                    _normalize=False)
                else:
                    return Fraction((-a._denominator) ** -power,
                                    (-a._numerator) ** -power,
                                    _normalize=False)
            else:
                # A fractional power will generally produce an
                # irrational number.
                return float(a) ** float(b)
        else:
            return float(a) ** b

    def __rpow__(b, a):
        """a ** b"""
        if b._denominator == 1 and b._numerator >= 0:
            # If a is an int, keep it that way if possible.
            return a ** b._numerator

        if isinstance(a, numbers.Rational):
            return Fraction(a.numerator, a.denominator) ** b

        if b._denominator == 1:
            return a ** b._numerator

        return a ** float(b)

    def __pos__(a):
        """+a: Coerces a subclass instance to Fraction"""
        return Fraction(a._numerator, a._denominator, _normalize=False)

    def __neg__(a):
        """-a"""
        return Fraction(-a._numerator, a._denominator, _normalize=False)

    def __abs__(a):
        """abs(a)"""
        return Fraction(abs(a._numerator), a._denominator, _normalize=False)

    def __trunc__(a):
        """trunc(a)"""
        if a._numerator < 0:
            return -(-a._numerator // a._denominator)
        else:
            return a._numerator // a._denominator

    def __floor__(a):
        """math.floor(a)"""
        return a.numerator // a.denominator

    def __ceil__(a):
        """math.ceil(a)"""
        # The negations cleverly convince floordiv to return the ceiling.
        return -(-a.numerator // a.denominator)

    def __round__(self, ndigits=None):
        """round(self, ndigits)

        Rounds half toward even.
        """
        if ndigits is None:
            floor, remainder = divmod(self.numerator, self.denominator)
            if remainder * 2 < self.denominator:
                return floor
            elif remainder * 2 > self.denominator:
                return floor + 1
            # Deal with the half case:
            elif floor % 2 == 0:
                return floor
            else:
                return floor + 1
        shift = 10**abs(ndigits)
        # See _operator_fallbacks.forward to check that the results of
        # these operations will always be Fraction and therefore have
        # round().
        if ndigits > 0:
            return Fraction(round(self * shift), shift)
        else:
            return Fraction(round(self / shift) * shift)

    def __hash__(self):
        """hash(self)"""

        # To make sure that the hash of a Fraction agrees with the hash
        # of a numerically equal integer, float or Decimal instance, we
        # follow the rules for numeric hashes outlined in the
        # documentation.  (See library docs, 'Built-in Types').

        try:
            dinv = pow(self._denominator, -1, _PyHASH_MODULUS)
        except ValueError:
            # ValueError means there is no modular inverse.
            hash_ = _PyHASH_INF
        else:
            # The general algorithm now specifies that the absolute value of
            # the hash is
            #    (|N| * dinv) % P
            # where N is self._numerator and P is _PyHASH_MODULUS.  That's
            # optimized here in two ways:  first, for a non-negative int i,
            # hash(i) == i % P, but the int hash implementation doesn't need
            # to divide, and is faster than doing % P explicitly.  So we do
            #    hash(|N| * dinv)
            # instead.  Second, N is unbounded, so its product with dinv may
            # be arbitrarily expensive to compute.  The final answer is the
            # same if we use the bounded |N| % P instead, which can again
            # be done with an int hash() call.  If 0 <= i < P, hash(i) == i,
            # so this nested hash() call wastes a bit of time making a
            # redundant copy when |N| < P, but can save an arbitrarily large
            # amount of computation for large |N|.
            hash_ = hash(hash(abs(self._numerator)) * dinv)
        result = hash_ if self._numerator >= 0 else -hash_
        return -2 if result == -1 else result

    def __eq__(a, b):
        """a == b"""
        if type(b) is int:
            return a._numerator == b and a._denominator == 1
        if isinstance(b, numbers.Rational):
            return (a._numerator == b.numerator and
                    a._denominator == b.denominator)
        if isinstance(b, numbers.Complex) and b.imag == 0:
            b = b.real
        if isinstance(b, float):
            if math.isnan(b) or math.isinf(b):
                # comparisons with an infinity or nan should behave in
                # the same way for any finite a, so treat a as zero.
                return 0.0 == b
            else:
                return a == a.from_float(b)
        else:
            # Since a doesn't know how to compare with b, let's give b
            # a chance to compare itself with a.
            return NotImplemented

    def _richcmp(self, other, op):
        """Helper for comparison operators, for internal use only.

        Implement comparison between a Rational instance `self`, and
        either another Rational instance or a float `other`.  If
        `other` is not a Rational instance or a float, return
        NotImplemented. `op` should be one of the six standard
        comparison operators.

        """
        # convert other to a Rational instance where reasonable.
        if isinstance(other, numbers.Rational):
            return op(self._numerator * other.denominator,
                      self._denominator * other.numerator)
        if isinstance(other, float):
            if math.isnan(other) or math.isinf(other):
                return op(0.0, other)
            else:
                return op(self, self.from_float(other))
        else:
            return NotImplemented

    def __lt__(a, b):
        """a < b"""
        return a._richcmp(b, operator.lt)

    def __gt__(a, b):
        """a > b"""
        return a._richcmp(b, operator.gt)

    def __le__(a, b):
        """a <= b"""
        return a._richcmp(b, operator.le)

    def __ge__(a, b):
        """a >= b"""
        return a._richcmp(b, operator.ge)

    def __bool__(a):
        """a != 0"""
        # bpo-39274: Use bool() because (a._numerator != 0) can return an
        # object which is not a bool.
        return bool(a._numerator)

    # support for pickling, copy, and deepcopy

    def __reduce__(self):
        return (self.__class__, (str(self),))

    def __copy__(self):
        if type(self) == Fraction:
            return self     # I'm immutable; therefore I am my own clone
        return self.__class__(self._numerator, self._denominator)

    def __deepcopy__(self, memo):
        if type(self) == Fraction:
            return self     # My components are also immutable
        return self.__class__(self._numerator, self._denominator)


win.timer.stop()

win.timer.start()

%%writefile  ~/miniconda3/envs/cloned_base/lib/python3.9/site-packages/vispy/geometry/torusknot.py
from __future__ import division

import numpy as np
#Python 3.9 changed from: from fractions import gdc
from math import gcd


class TorusKnot(object):
    """Representation of a torus knot or link.

    A torus knot is one that can be drawn on the surface of a
    torus. It is parameterised by two integers p and q as below; in
    fact this returns a single knot (a single curve) only if p and q
    are coprime, otherwise it describes multiple linked curves.

    Parameters
    ----------
    p : int
        The number of times the knot winds around the outside of the
        torus. Defaults to 2.
    q : int
        The number of times the knot passes through the hole in the
        centre of the torus. Defaults to 3.
    num_points : int
        The number of points in the returned piecewise linear
        curve. If there are multiple curves (i.e. a torus link), this
        is the number of points in *each* curve.  Defaults to 100.
    major_radius : float
        Distance from the center of the torus tube to the center of the torus.
        Defaults to 10.
    minor_radius : float
        The radius of the torus tube. Defaults to 5.

    """

    def __init__(self, p=3, q=2, num_points=100, major_radius=10.,
                 minor_radius=5.):
        self._p = p
        self._q = q
        self._num_points = num_points
        self._major_radius = major_radius
        self._minor_radius = minor_radius

        self._calculate_vertices()

    def _calculate_vertices(self):
        angles = np.linspace(0, 2*np.pi, self._num_points)

        num_components = self.num_components

        divisions = (np.max([self._q, self._p]) *
                     np.min([self._q, self._p]) / self.num_components)
        starting_angles = np.linspace(
            0, 2*np.pi, divisions + 1)[
            :num_components]
        q = self._q / num_components
        p = self._p / num_components

        components = []
        for starting_angle in starting_angles:
            vertices = np.zeros((self._num_points, 3))
            local_angles = angles + starting_angle
            radii = (self._minor_radius * np.cos(q * angles) +
                     self._major_radius)
            vertices[:, 0] = radii * np.cos(p * local_angles)
            vertices[:, 1] = radii * np.sin(p * local_angles)
            vertices[:, 2] = (self._minor_radius * -1 *
                              np.sin(q * angles))
            components.append(vertices)

        self._components = components

    @property
    def first_component(self):
        '''The vertices of the first component line of the torus knot or link.
        '''
        return self._components[0]

    @property
    def components(self):
        '''A list of the vertices in each line of the torus knot or link.
        Even if p and q are coprime, this is a list with just one
        entry.
        '''
        return self._components

    @property
    def num_components(self):
        '''The number of component lines in the torus link. This is equal
        to the greatest common divisor of p and q.
        '''
        return gcd(self._p, self._q)

    @property
    def q(self):
        '''The q parameter of the torus knot or link.'''
        return self._q

    @q.setter
    def q(self, q):
        self._q = q
        self._calculate_vertices()

    @property
    def p(self):
        '''The p parameter of the torus knot or link.'''
        return self._p

    @p.setter
    def p(self, p):
        self._p = p
        self._calculate_vertices()

    @property
    def minor_radius(self):
        '''The minor radius of the torus.'''
        return self._minor_radius

    @minor_radius.setter
    def minor_radius(self, r):
        self._minor_radius = r
        self._calculate_vertices()

    @property
    def major_radius(self):
        '''The major radius of the torus.'''
        return self._major_radius

    @major_radius.setter
    def major_radius(self, r):
        self._major_radius = r
        self._calculate_vertices()

    @property
    def num_points(self):
        '''The number of points in the vertices returned for each knot/link
        component'''
        return self._num_points

    @num_points.setter
    def num_points(self, r):
        self._num_points = r
        self._calculate_vertices()




