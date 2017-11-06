# cython: boundscheck=False
# cython: wraparound=False
cdef extern from "stdlib.h":
     int c_libc_rand "rand"()
     
def ii_search(unsigned int[:,:] sat, int w, int h, int step):
    """
    Find empty area of specified size
    
    Arguments:
    sat -- integral image
    w -- width of area to find
    h -- height of area to find
    step -- size of step to use for sliding window
    
    Returns:
    List of available spots
    """
    l = []
    cdef Py_ssize_t x = sat.shape[0]
    cdef Py_ssize_t y = sat.shape[1]
    cdef int i, j
    cdef long S
    cdef int startx = c_libc_rand() % step
    cdef int starty = c_libc_rand() % step
    for i in range(startx, x - h, step):
        for j in range(starty, y - w, step): 
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
    """
    Find empty area of specified size - faster when step size is 1
    
    Arguments:
    sat -- integral image
    w -- width of area to find
    h -- height of area to find
    
    Returns:
    List of available spots
    """
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