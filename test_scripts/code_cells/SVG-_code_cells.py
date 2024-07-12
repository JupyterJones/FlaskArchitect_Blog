from IPython.display import SVG, display
import mathsvg
image = mathsvg.SvgImage(pixel_density = 100, view_window = (( -1, -1 ), ( 1, 1 )))
image.draw_circle([0, 0], .1)
image.save("simple-example.svg")

def show_svg():
    display(SVG('simple-example.svg'))
    
    
show_svg()    


mathsvg’s documentation

The module defines the class SvgImage whose instances are used for creating SVG images.

The source code is hosted on GitHub.

Here is a simple example:

import mathsvg
image = mathsvg.SvgImage(pixel_density = 100, view_window = (( -1, -1 ), ( 1, 1 )))
image.draw_circle([0, 0], 1.1)
image.save("simple-example.svg")

The above example produces the following image:
A cropped circle centered on a square canvas

You can install mathsvg with pip:

pip install mathsvg

Example of how to use your SVG file

The SVG file can then be edited using programs such as Inkscape. For example you can convert them into pdf_tex files using the command:

inkscape -D math-svg-saved-image.svg  -o exported-name.pdf --export-latex

Then include the file in the LaTeX document with:

\begin{figure}
  \centering
  \def\svgwidth{\columnwidth}
  \input{exported-name.pdf_tex}
\end{figure}

Don’t forget to include the package graphicx.

See the documentations of the relevant programs for more details.
Examples

    cantor-bouquet.py
    iteration-graph.py
    selfsim-triforce.py
    torus.py

Click on the image to see the sources.
_images/compact-cantor-bouquet.svg _images/disconnected-straight-brush.svg _images/iteration-graph.svg _images/one-sided-hairy-circle.svg _images/selfsim-triforce.svg _images/torus.svg
The SvgImage class

class mathsvg.mathsvg.SvgImage(view_window=((-1, -1), (1, 1)), pixel_density=100.0, _svgwrite_debug=False)[source]

    Main class used for creating SVG images.

    In order to make SVG graphics using mathsvg, you need first to create an instance of SvgImage. Then do your drawings by calling a few members functions of this object. Finally call save() to save the result.

    The constructor has the following optional arguments:

            view_window (tuple): is a tuple of tuple values characterizing the drawing area.
                The first tuple contains the minima values for x and y and the last one the corresponding maxima.

            pixel_density (float): number of pixels per unit length. Coordinates in the SVG file are rescaled accordingly.
            _svgwrite_debug (boolean): to create the svgwrite object with a specific debug mode (default is False).

    draw_arrow(start_point, end_point, curvedness=0.0, asymmetry=0.0)[source]

        Draws either a straight or curved arrow.

        Args:

                start_point (tuple): coordinates of where the arrow starts
                end_point (tuple): coordinates of where the arrow ends
                curvedness (float or None): height of the bump making the arrow curve, if is None then will draw a straight arrow (asymmetry will be ignored)
                asymmetry (float or None): where the bump should be located: 0 is the middle, negative: towards the first point, positive: towards the last point. A value between -0.5 and 0.5 guarantees that the bump is between the two end points.

        Examples: see graphs.py, arrows.py

    draw_arrow_tip(tip, arrow_direction_angle)[source]

        Draws the tip of an arrow.

        Args:

                tip (tuple): coordinates of the position of the tip
                arrow_direction_angle (float): angle where the arrow is pointing in radians

        Examples: see arrows.py

    draw_circle(center, radius)[source]

        Draws a circle.

        Args:

                center (tuple): coordinates of the center of the circle
                radius (float): radius of the circle

        Examples: see points-crosses-circles-ellipses.py, potato-regions.py

    draw_circle_arc(center, radius, start_angle, end_angle)[source]

        Draws an of a circle (in anticlockwise direction).

        Args:

                center (tuple): coordinates of the center of the circle
                radius (float): radius of the circle
                start_angle (float): angle where the arc starts in radians
                end_angle (float): angle where the arc ends in radians

        Examples: see points-crosses-circles-ellipses.py

    draw_cross(position)[source]

        Draws a small X cross.

        Args:

                position (tuple): position of the center of the cross

        Examples: see points-crosses-circles-ellipses.py

    draw_curved_arrow(start_point, end_point, curvedness=0.25, asymmetry=0.0)[source]

        Draws an arrow as a curved line joining two points with an arrow tip at the last point.

        Args:

                start_point (tuple): coordinates of where the arrow starts
                end_point (tuple): coordinates of where the arrow ends
                curvedness (float or None): height of the bump making the arrow curve (0 for a straight arrow)
                asymmetry (float or None): where the bump should be located: 0 is the middle, negative: towards the first point, positive: towards the last point. A value between -0.5 and 0.5 guarantees that the bump is between the two end points.

        Examples (see also: curved-arrows.py and more-curved-arrows.py):

        image = mathsvg.SvgImage(pixel_density = 20, view_window = (( -4, -4 ), ( 4, 4 )))

        image.draw_curved_arrow([ -2, -1 ], [ 2, -1 ], curvedness = -.2)
        image.draw_curved_arrow([ -2.7, 2 ], [ -0.3, 2 ], asymmetry = - 0.8)
        image.draw_curved_arrow([ -2.7, 1 ], [ -0.3, 1 ], asymmetry = - 0.2)
        image.draw_curved_arrow([ -2.7, 0 ], [ -0.3, 0 ], asymmetry = 0.2)
        image.draw_curved_arrow([ -2.7, -1 ], [ -0.3, -1 ], asymmetry = 0.5)
        image.draw_curved_arrow([ -2.7, -2 ], [ -0.3, -2 ], curvedness = -0.2, asymmetry = 1.2)

        image.save("draw-curved-arrow-example.svg")

    draw_ellipse(focuses, semi_minor_axis)[source]

        Draws an ellipse with axis parallel to the x and y axis.

        Args:

                focuses (list): list of two tuples of coordinates of the focuses of the ellipse
                semi_minor_axis (float): semi minor axis

        Examples (see also points-crosses-circles-ellipses.py and torus.py):

        import math
        two_pi = 2. * math.pi

        import mathsvg

        image = mathsvg.SvgImage(pixel_density = 20, view_window = (( -4, -4 ), ( 4, 4 )))

        focuses = [ [-1.33, 0.61], [1.33, -0.61] ]

        image.draw_ellipse(focuses, 0.68)

        image.save("draw-ellipse-example.svg")

    draw_ellipse_arc(focuses, semi_minor_axis, start_angle, end_angle)[source]

        Draws an arc of an ellipse (in anticlockwise direction) with axis parallel to the x and y axis. The ellipse is parametrised in the form “c + (a cos t, b sin t)” where t varies from start_angle to end_angle (a, b and c are the parameters of the ellipse computed from the coordinates of the focuses and the semi minor axis).

        Args:

                focuses (list): list of two tuples of coordinates of the focuses of the ellipse
                semi_minor_axis (float): semi minor axis
                start_angle (float): angle where the arc starts in radians
                end_angle (float): angle where the arc ends in radians

        Examples (see also points-crosses-circles-ellipses.py and torus.py):

        import math
        two_pi = 2. * math.pi

        import mathsvg

        image = mathsvg.SvgImage(pixel_density = 20, view_window = (( -4, -4 ), ( 4, 4 )))

        focuses = [ [-1.33, 0.61], [1.33, -0.61] ]

        image.draw_ellipse_arc(focuses, 0.412, two_pi * 0.1, two_pi * 0.8)

        image.save("draw-ellipse-arc-example.svg")

    draw_function_graph(eval_function, x_start, x_end, nb_x, *function_params, curve_type='polyline')[source]

        Draws the graph of a function f, that is, an interpolation of a set of nb_x points (x, y) with y = f (x) and with x between x_start and x_end. The default interpolation is by straight lines. It is also possible to have some type of smooth interpolation. The nb_x points have regularly spaced x coordinates starting from x_start and ending at x_end.

        Args:

                eval_function: a function (or lambda) that takes x as an argument and returns y = f (x). The function will be called with eval_function (x, * function_params) allowing extra parameters to be passed.
                x_start (float): start of the graph domain
                x_end (float): end of the graph domain
                nb_x (int): number of points x at which the function is computed
                function_params (variadic arguments): optionally, arguments to pass to eval_function in addition to the value for x
                curve_type (str or None): if "polyline" then the point are interpolated by line segments, if "autosmooth" the interpolation is smoother

        Examples (see also graphs.py):

        image = mathsvg.SvgImage(pixel_density = 20, view_window = ((0, -5), (10, 5)))

        function = lambda x : math.sin (5 * x)

        image.set_svg_options(stroke_color = "blue")
        image.draw_function_graph(function, 0, 10, 33, curve_type = "polyline")
        image.set_svg_options(stroke_color = "black")
        image.draw_function_graph(function, 0, 10, 214, curve_type = "autosmooth")

        image.save("draw-function-graph-example.svg")

    draw_line_segment(start_point, end_point)[source]

        Draws the line segment between two points.

        Args:

                start_point (tuple): coordinates of the first end point of the line segment
                end_point (tuple): coordinates of the second end point of the line segment

        Examples: see lines.py, dashes.py, interpolated-curves.py

    draw_parametric_graph(eval_point, t_start, t_end, nb_t, *function_params, curve_type='polyline', is_closed=False)[source]

        Draws a parametric graph given by the functions x(t) and y(t), that is, an interpolation of a set of nb_t points (x, y) with x = x(t) and y = y(t) and with t between t_start and t_end. The default interpolation is by straight lines. It is also possible to have some type of smooth interpolation. The nb_t parameters are regularly spaced starting from t_start and ending at t_end.

        If is_closed is set to True the two endpoints of the curve will be joined according to the choice of interpolation.

            Args:

                    eval_point: a function (or a lambda) that takes the parameter t as an argument and returns the tuple of coordinates (x,y) corresponding to the pameter t. The function will be called with eval_point(t, * function_params) allowing extra parameters to be passed.
                    t_start (float): start of the parameter domain
                    t_end (float): end of the parameter domain
                    nb_t (int): number of parameters t at which the functions x and y are computed
                    function_params (variadic arguments): optionally, arguments to pass to eval_point in addition to the value for the parameter t
                    curve_type (str or None): if 'polyline' then the point are interpolated by line segments, if 'autosmooth' the interpolation is smoother
                    is_closed (str or None): whether the parametric curve should be closed (True) or not (False)

            Examples (see also parametric-graphs.py):

            import math

            image = mathsvg.SvgImage(pixel_density = 20, view_window = ((-1.1, -1.5), (2.9, 1.5)))

            eval_point = lambda t : (math.sin(10 * math.pi * t) + 0.1, math.cos(6 * math.pi *  t))
            image.set_svg_options(stroke_color = 'blue')
            image.draw_parametric_graph(eval_point, 0, 1, 40, curve_type = 'polyline', is_closed = False)

            eval_point = lambda t : (math.sin(10 * math.pi * t) + 1.1, math.cos(6 * math.pi * t))
            image.set_svg_options(stroke_color = 'black')
            image.set_dash_mode("dash")
            image.draw_parametric_graph(eval_point, 0, 1, 40, curve_type = "autosmooth", is_closed = True)

            image.save('draw-parametric-graph-example.svg')

    draw_planar_potato(center, inner_radius, outer_radius, nb_vertexes)[source]

        Draws some randomly generated smooth shape in the form of a smooth closed curve.

        A set of radomly generated set of nb_vertexes points is generated. Both angles and distances with respect to center are generated according to a uniform law. The distance from the center is chosen uniformly between the values of inner_radius and outer_radius.

        Args:

                center (tuple): coordinates of the center of the potato
                inner_radius (float): roughly the closest the curve comes from the center
                outer_radius (float): roughly the farthest the curve comes from the center
                nb_vertexes (int): number of points to generate (more points means that it is more likely that the curve will have selfintersections)

        Example (see also: potato.py, potato-3v.py, dashes.py, wiggly-potato.py, wigglier-potato.py, potato-regions.py):

        image = mathsvg.SvgImage(pixel_density = 20, view_window = (( -2, -2), (2, 2)))
        image.draw_planar_potato([0, 0], 0.5, 1.5, 3)
        image.save("draw-planar-potato-example.svg")

    draw_plus(position)[source]

        Draws a small + cross.

        Args:

                position (tuple): position of the center of the cross

        Examples: see points-crosses-circles-ellipses.py

    draw_point(position)[source]

        Draws a small circle.

        Args:

                position (tuple): position of the center of the circle

        Examples: see points-crosses-circles-ellipses.py

    draw_polygon(point_list)[source]

        Draws a polygon using straight lines.

        Args:

                point_list (list): ordered list of points (coordinates) to connect with line segments (at least three points required).

        Example:

        image = mathsvg.SvgImage(pixel_density = 20, view_window = ((0, 0), (8, 8)))
        point_list = [ (2.5,5), (4.5,7), (2.5,4), (0.5,3), (6,2) ]
        image.draw_polygon(point_list)
        image.save("draw-polygon-example.svg")

    draw_polyline(point_list)[source]

        Draws a sequence of connected lins segments.

        Args:

                point_list (list): ordered list of points (coordinates) to connect with line segments (at least two points required).

        Example (see also interpolated-curves.py):

        image = mathsvg.SvgImage(pixel_density = 20, view_window = ((0, 0), (8, 8)))
        point_list = [ (2.5,5), (4.5,7), (2.5,4), (0.5,3), (6,2) ]
        image.draw_polyline(point_list)
        image.save("draw-polyline-example.svg")

    draw_random_wavy_line(start_point, end_point, wave_len, amplitude)[source]

        Draws a smooth line with randomly generated bumps perpendicularly to its direction.

        Regularly separated points are computed along the straight line segment between the two end points. The distance between two consecutive points is equal to wave_len. Then for each of these points, a point is picked randomly on the corresponding perpendicular line according to a uniform law, symmetrically with respect to the directing line and with maximum distance equal to the value of amplitude. Finally a smooth interpolating curve is drawn. This curve goes from the first end point to the last and passes along the randomly generated points.

        Args:

                start_point (tuple): coordinates of the first end point of the line
                end_point (tuple): coordinates of the second end point of the line
                wave_len (float): distance between two consecutive disturbances (smaller values yield more bumps)
                amplitude (float): size of the bumps

        Raises some error text exception when the value of wave_len is larger or equal to the distance between the two end points.

        Example (see also lines.py and scribble.py):

        image = mathsvg.SvgImage(pixel_density = 20, view_window = (( -4, -4 ), ( 4, 4 )))

        image.set_dash_mode("dot")
        image.draw_line_segment([-3., -2.9], [3., 3.1])
        image.draw_line_segment([-3., -2.7], [3., 3.3])
        image.set_dash_mode("none")
        image.draw_random_wavy_line([-3., -2.8], [3., 3.2], 0.1, 0.1)

        image.save("draw-random-wavy-line-example.svg")

    draw_rectangle(top, left, bottom, right)[source]

        Draws a rectangle.

        Args:
            *top (float): top coordinate of the rectangle *left (float): left coordinate of the rectangle *bottom (float): bottom coordinate of the rectangle *right (float): right coordinate of the rectangle

    draw_smoothly_interpolated_closed_curve(points)[source]

        Draws a smooth closed curve that interpolates the points given as parameter.

        Args:

                points (list): list of point coordinates to interpolate (at least two points)

        Example (see also interpolated-curves.py):

        image = mathsvg.SvgImage(pixel_density = 20, view_window = ((0, 0), (10, 10)))
        point_list = [ [7.4, 2], [5.6, 4], [7.3, 6], [ 4.3, 5.2], [ 8.3, 9.1 ] ]
        image.draw_smoothly_interpolated_closed_curve(point_list)
        image.save("draw-smoothly-interpolated-closed-curve-example.svg")

    draw_smoothly_interpolated_open_curve(points)[source]

        Draws a smooth open curve that interpolates the points given as parameter.

        The coordinates of the endpoints of the curve are the first and last set of coordinates from the list given as argument.

        Args:

                points (list): list of point coordinates to interpolate (at least two points)

        Example (see also interpolated-curves.py):

        image = mathsvg.SvgImage(pixel_density = 20, view_window = ((0, 0), (10, 10)))
        point_list = [ [7.4, 2], [5.6, 4], [7.3, 6], [ 4.3, 5.2], [ 8.3, 9.1 ] ]
        image.draw_smoothly_interpolated_open_curve(point_list)
        image.save("draw-smoothly-interpolated-open-curve-example.svg")

    draw_square(center, side_length)[source]

        Draws a square.

        Args:
            *center: coordinates of the center *side_length: length of the side of the square

    draw_straight_arrow(start_point, end_point)[source]

        Draws an arrow as a straight line segment between two points and an arrow tip at the last point.

            Equivalent to self.draw_arrow(start_point, end_point).

        Args:

                start_point (tuple): coordinates of where the arrow starts
                end_point (tuple): coordinates of where the arrow ends

    insert_svg_path_command(svg_path_command)[source]

        Insert a path command given in the form of a string into the SVG.

            The resulting SVG command will be of the form <path d="..." style="..." />, where the first "..." stands for the content of the argument svg_path_command and the second "..." is an automatically generated style option string based on the current state of the SvgImage object (including: stroke color, width, filling color, dash array, etc.). The validity of the argument as a path command is not checked. Errors might or might not raise an exception, depending on the behavior of the module svgwrite.

            Args:

                    svg_path_command (str): the string to be inserted.

            Example:

            image = mathsvg.SvgImage(pixel_density = 100, view_window = (( -4, -4 ), ( 4, 4 )))
            image.insert_svg_path_command("M 650, 650 C 650, 650 443, 693 275, 525 107, 357 150, 150 150, 150")
            image.save("svg-command-example.svg")

            The result is the following image:

        A portion of a Bezier curve

    project_complex_point_to_canvas(z)[source]

        Compute the coordinates of a complex number projected onto the SVG canvas (equivalent to project_point_to_canvas([ z.real, z.imag ])).

    project_complex_vector_to_canvas(dz)[source]

        Compute the coordinates of a complex vector attached at 0 on the SVG canvas (rescaling without translation).

    project_point_to_canvas(point)[source]

        Compute the coordinate of a point on the SVG canvas.

    project_vector_to_canvas(vector)[source]

        Compute the coordinates of a vector attached at 0 on the SVG canvas (rescaling without translation).

    put_text(text, text_position, font_size=None, units='math')[source]

        Insert text on the canvas at the given position

        Args:

                text (str): text to insert
                text_position (tuple): coordinates of the bottom left of the text
                font_size (``int or None): font size, if None use the default font size (see set_font_options and reset_font_options)
                units (default: 'math'): units for the size. The valid values are 'math' for math units, 'svg' for pixels

        Example:

        import mathsvg

        image = mathsvg.SvgImage(view_window = ((0., 0.), (4., 4.)), pixel_density = 100)
        image.draw_circle((1., 3.), 0.6)
        image.draw_circle((3., 3.), 0.6)
        image.draw_circle((1., 1.), 0.6)
        image.draw_arrow((1., 1.7), (1., 2.3))
        image.draw_arrow((1.5, 1.5), (2.5, 2.5))
        image.draw_arrow((1.7, 3.), (2.3, 3.))
        image.put_text("Z", (.9, .9), font_size = .3)
        image.put_text("A", (.9, 2.9), font_size = .3)
        image.put_text("B", (2.9, 2.9), font_size = .3)

        image.save("put-text-example.svg")

    reset_arrow_options()[source]

        Sets the width, opening angle and curvature of arrows to default values depending eventually on the size of the canvas.

    reset_dash_and_dot_structures()[source]

        Sets the dash, dot and dasharray structures to default values depending on the size of the canvas.

    reset_font_options()[source]

        Reset the font size to the default value (depends on the size of the window)

    reset_svg_options()[source]

        Sets the stroke color to "black", the stroke width to 1 pixel and the fill color to "none".

    save(file_name, do_overwrite=False)[source]

        Save the drawings into a SVG file.

        Args:

                    file_name (str): name of the file to save.
                    do_overwrite: optional boolean to allow overwrite over already existing file (default value is False), raise an exception if this is False and the file already exists.

            See an example in multiple-save.py

    set_arrow_options(width=None, opening_angle=None, curvature=None, units='math')[source]

        Sets some values governing the shape and geometry of the arrows.

        Args:

                width (float or None): width of the arrow tip, in math units (not pixels)
                opening_angle (float or None): opening angle of the arrow tip
                curvature (float or None): curving for the back of the tip of the arrow, 0 for a straight arrow tip
                units (default:'math'): units for the size. The valid values are 'math' for math units and 'svg' for pixels

        Examples (see also arrows.py):

        image = mathsvg.SvgImage(pixel_density = 20, view_window = ((-4, -4), (4, 4)))

        image.set_arrow_options(curvature = 0.55)
        image.draw_arrow([ -2, -2 ], [ 2, 1.7 ])

        image.set_arrow_options(width = 4 * image.arrow_width_svgpx, units='svg')
        image.draw_arrow([ -2, -2 ], [ 2, 1.2 ])

        image.reset_arrow_options()
        image.set_arrow_options(curvature = 0)
        image.draw_arrow([ -2, -2 ], [ 2, 0.6 ])

        image.save("set-arrow-options-example.svg")

    set_dash_dash_structure(black_len, white_len, units='math')[source]

        Sets the size of the dashes and space for the dash mode

        Args:

                black_len (int or float): length of the dash
                white_len (int or float): length of the space between dashes
                units (default:'math'): units for the size. The valid values are 'math' for math units and 'svg' for pixels

    set_dash_dot_structure(dot_sep, units='math')[source]

        Sets the separations between dots for dotted stroke

        Args:

                dot_sep (int or float): separation between the dots in pixels
                units (default:'math'): units for the size. The valid values are 'math' for math units and 'svg' for pixels

    set_dash_mode(mode)[source]

        Choose the type of stroke.

        Args:

                mode (str): the type of stroke, should be either "none" (solid line), "dash", "dot" (or "dots") or "dasharray" (customized dash/dot, see SVG specifications for more details on dash arrays)

        Example (see also lines.py, dashes.py, more-curved-arrows.py, torus.py, points-crosses-circles-ellipses.py, arrows.py, curved-arrows.py, potato-regions.py):

        image = mathsvg.SvgImage(pixel_density = 20, view_window = ((0, 0), (10, 10)))

        image.set_dash_mode("dash")
        image.draw_line_segment([0, 0], [10, 10])

        image.set_dash_mode("dot")
        image.draw_line_segment([0, 10], [10, 0])

        image.set_svg_options(dash_array = [18, 3, 1, 3, 7, 3, 1, 3], units='svg')
        image.set_dash_mode("dasharray")
        image.draw_planar_potato([5, 5], 2, 4, 8)

        image.save("set-dash-mode-example.svg")

    set_font_options(font_size=None, units='math')[source]

        Set some font options, so far only the font size.

        Args:

                font_size (default:None): font size
                units (default:'math'): units for the size. The valid values are 'math' for math units and 'svg' for pixels

    set_point_size(point_size, units='math')[source]

        Set the size of points, pluses and crosses.

        Args:

                point_size: half diameter of the points/pluses/crosses
                units (default:'math'): units for the size. The valid values are 'math' for math units and 'svg' for pixels

    set_svg_options(stroke_color=None, stroke_width=None, fill_color=None, dash_array=None, units='math')[source]

        Sets the stroke width, color, fill color and dash array options

        Args:

                stroke_color (str or None): stroke color (default is "black")
                stroke_width (float or None): stroke width
                fill_color (str or None): fill color (default is "none")
                dash_array (tuple or None): list of stroke/space lengths describing the customize dash stroke
                units (default:'math'): units for the sizes. The valid values are 'math' for math units and 'svg' for pixels

        Note it might increase the value of stroke_width to make sure that it is at least 1.

        Examples: To do some drawings in red, then restore back to the default options:

        image.set_svg_options(stroke_color = "red")
        (etc.)
        image.reset_svg_options()

Feature examples

    arrows.py
    curved-arrows.py
    dashes.py
    graphs.py
    interpolated-curves.py
    lines.py
    more-curved-arrows.py
    multiple-save.py
    parametric-graphs.py
    points-crosses-circles-ellipses.py
    potato.py
    potato-3v.py
    potato-regions.py
    put-text-example.py
    scribble.py
    wigglier-potato.py
    wiggly-potato.py

Click on the image to see the sources.
_images/arrows1.svg _images/curved-arrows1.svg _images/dashes1.svg _images/graphs1.svg _images/interpolated-curves1.svg _images/lines1.svg _images/more-curved-arrows1.svg _images/multiple-save1.svg _images/parametric-graphs1.svg _images/points-crosses-circles-ellipses1.svg _images/potato1.svg _images/potato-3v1.svg _images/potato-regions1.svg _images/put-text-example1.svg _images/scribble1.svg _images/wigglier-potato1.svg _images/wiggly-potato1.svg
Indices and tables

    Index
    Module Index
    Search Page

Table of Contents

    mathsvg’s documentation
        Example of how to use your SVG file
        Examples
        The SvgImage class
        Feature examples
    Indices and tables

Next topic

cantor-bouquet.py
This Page

    Show Source

Quick search

    index
    modules |
    next |


