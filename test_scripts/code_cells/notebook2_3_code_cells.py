%matplotlib inline
import matplotlib
import matplotlib.pyplot as plt
print(matplotlib.backends.backend)

from IPython.display import set_matplotlib_formats
set_matplotlib_formats('png', 'pdf')
matplotlib.rcParams['figure.figsize'] = (2,1)

ip.display_formatter.formatters['application/pdf'].type_printers

import numpy as np

a = np.random.uniform(size=(100,100))

a.shape

evs = np.linalg.eigvals(a)

evs.shape

plt.hist(evs.real)

