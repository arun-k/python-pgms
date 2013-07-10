import itertools

def my_enumerate(it):
    return itertools.izip(itertools.count(),it)
