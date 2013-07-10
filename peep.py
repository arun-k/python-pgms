import itertools

def peep(it):
	first=it.next()
	it=itertools.chain(iter([first]),it)
	return first,it
