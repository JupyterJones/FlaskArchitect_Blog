lines = open("Classes.API").readlines()
search = input("SEARCH TERM: ")
for line in lines:
    if search in line:
        print(line)

import vsketch

dir(vsketch)

dir(vsketch.vsketch)

dir(vsketch.style)

dir(vsketch.vsketch.math)

dir(vsketch.vsketch.math.radians)



