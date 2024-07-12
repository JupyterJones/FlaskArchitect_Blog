%pylab inline

import numpy as np

a = np.random.uniform(size=(100,100))

a.shape

evs = np.linalg.eigvals(a)

evs.shape

hist(evs.real)

