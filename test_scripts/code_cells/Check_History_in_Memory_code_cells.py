from IPython import get_ipython

ip = get_ipython()
assert ip.history_manager.hist_file == ':memory:'

