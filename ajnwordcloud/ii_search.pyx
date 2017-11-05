# cython: boundscheck=False
# cython: wraparound=False
 
def ii_search(unsigned int[:,:] sat, int w, int h, int step):
    l = []
    cdef Py_ssize_t x = sat.shape[0]
    cdef Py_ssize_t y = sat.shape[1]
    cdef int i, j
    cdef long S
    for i in range(0, x - h, step):
        for j in range(0, y - w, step): 
            S = sat[i + h, j + w]
            if i > 0 and j > 0:
                S += sat[i - 1, j - 1]
            if j > 0:
                S -= sat[i + h, j - 1]
            if i > 0:
                S -= sat[i - 1, j + w]
            if S == 0:
                l.append((i, j))
    return l
    
def ii_search_nostep(unsigned int[:,:] sat, int w, int h):
    l = []
    l = []
    cdef Py_ssize_t x = sat.shape[0]
    cdef Py_ssize_t y = sat.shape[1]
    cdef int i, j
    cdef long S
    for i in range(0, x - h):
        for j in range(0, y - w): 
            S = sat[i + h, j + w]
            if i > 0 and j > 0:
                S += sat[i - 1, j - 1]
            if j > 0:
                S -= sat[i + h, j - 1]
            if i > 0:
                S -= sat[i - 1, j + w]
            if S == 0:
                l.append((i, j))
    return l