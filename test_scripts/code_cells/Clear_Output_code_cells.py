from __future__ import print_function
from IPython.display import clear_output

for i in range(10):
    clear_output()
    print(i)

print("Hello world")
clear_output()

print("Hello world", end='')
clear_output(wait=True)  # no output after this

print("Hello", end='')
clear_output(wait=True)  # here we have new output after wait=True
print("world", end='')

handle0 = display("Hello world", display_id="id0")

handle1 = display("Hello", display_id="id1")

handle1.update('world')

handle2 = display("Hello world", display_id="id2")
clear_output()  # clears all output, also with display_ids

handle3 = display("Hello world", display_id="id3")
clear_output(wait=True)

handle4 = display("Hello", display_id="id4")
clear_output(wait=True)
print('world', end='')

handle4.update('Hello world')  # it is cleared, so it should not show up in the above cell

