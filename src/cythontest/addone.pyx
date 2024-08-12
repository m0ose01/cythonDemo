import cython

@cython.ccall
def addone(x: cython.int) -> cython.int:
    return x + 1
