%load_ext cython

%%cython

cdef int a = 0
for i in range(10):
    a += i
print(a)

%%cython --annotate

cdef int a = 0
for i in range(10):
    a += i
print(a)

