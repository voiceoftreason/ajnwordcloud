# cython: boundscheck=False
# cython: wraparound=False
cdef extern from "stdlib.h":
     int c_libc_rand "rand"()

#https://computersciencesource.wordpress.com/2010/09/03/computer-vision-the-integral-image/
     
def ii_search(unsigned int[:,:] sat, int areawidth, int areaheight, int step):
    """
    Find empty area of specified size
    
    Arguments:
    sat -- integral image
    areawidth -- width of area to find
    areaheight -- height of area to find
    step -- size of step to use for sliding window
    
    Returns:
    List of available spots
    """
    spots = []
    cdef Py_ssize_t imheight = sat.shape[0]
    cdef Py_ssize_t imwidth = sat.shape[1]
    cdef int i, j
    cdef long areasum
    cdef int starti = c_libc_rand() % step
    cdef int startj = c_libc_rand() % step
    for i in range(starti, imheight - areaheight, step):
        for j in range(startj, imwidth - areawidth, step): 
            areasum = sat[i + areaheight, j + areawidth]
            if i > 0 and j > 0:
                areasum += sat[i - 1, j - 1]
            if j > 0:
                areasum -= sat[i + areaheight, j - 1]
            if i > 0:
                areasum -= sat[i - 1, j + areawidth]
            if areasum == 0:
                spots.append((i, j))
    return spots
    
def ii_search_nostep(unsigned int[:,:] sat, int areawidth, int areaheight):
    """
    Find empty area of specified size - faster when step size is 1
    
    Arguments:
    sat -- integral image
    w -- width of area to find
    h -- height of area to find
    
    Returns:
    List of available spots
    """
    spots = []
    cdef Py_ssize_t imheight = sat.shape[0]
    cdef Py_ssize_t imwidth = sat.shape[1]
    cdef int i, j
    cdef long areasum
    for i in range(imheight - areaheight):
        for j in range(imwidth - areawidth): 
            areasum = sat[i + areaheight, j + areawidth]
            if i > 0 and j > 0:
                areasum += sat[i - 1, j - 1]
            if j > 0:
                areasum -= sat[i + areaheight, j - 1]
            if i > 0:
                areasum -= sat[i - 1, j + areawidth]
            if areasum == 0:
                spots.append((i, j))
    return spots