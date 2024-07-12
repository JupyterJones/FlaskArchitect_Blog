import ipywidgets as widgets
from IPython.display import clear_output
output1 = widgets.Output()
output1

print("hi")
with output1:
    print("in output")

with output1:
    raise ValueError("trigger msg_type=error")

import ipywidgets as widgets
output2 = widgets.Output()
output2

print("hi2")
with output2:
    print("in output2")
    clear_output(wait=True)

import ipywidgets as widgets
output3 = widgets.Output()
output3

print("hi3")
with output3:
    print("hello")
    clear_output(wait=True)
    print("world")

import ipywidgets as widgets
output4 = widgets.Output()
output4

print("hi4")
with output4:
    print("hello world")
    clear_output()

import ipywidgets as widgets
output5 = widgets.Output()
output5

print("hi5")
with output5:
    display("hello world") # this is not a stream but plain text
clear_output()

import ipywidgets as widgets
output_outer = widgets.Output()
output_inner = widgets.Output()
output_inner

output_outer

with output_inner:
    print('in inner')
    with output_outer:
        print('in outer')
    print('also in inner')

