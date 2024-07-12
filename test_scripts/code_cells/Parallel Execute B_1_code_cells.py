import os
import os.path
import tempfile
import time

# the variable this_notebook is injectected in a cell above by the test framework.
this_notebook = 'B'
other_notebook = 'A'
directory = os.environ['NBEXECUTE_TEST_PARALLEL_TMPDIR']
with open(os.path.join(directory, 'test_file_{}.txt'.format(this_notebook)), 'w') as f:
    f.write('Hello from {}'.format(this_notebook))

start = time.time()
timeout = 5
end = start + timeout
target_file = os.path.join(directory, 'test_file_{}.txt'.format(other_notebook))
while time.time() < end:
    time.sleep(0.1)
    if os.path.exists(target_file):
        with open(target_file, 'r') as f:
            text = f.read()
        if text == 'Hello from {}'.format(other_notebook):
            break
else:
    assert False, "Timed out – didn't get a message from {}".format(other_notebook)

