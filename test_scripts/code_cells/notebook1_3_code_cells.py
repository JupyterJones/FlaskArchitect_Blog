from sympy import init_printing
from sympy import *
init_printing()

x,y,z = symbols('x y z')

e = x**2 + 2.0*y + sin(z); e

diff(e, x)

integrate(e, z)



