

def vectorize(f):
    def apply_f(lst):
        return [f(x) for x in lst]
    return apply_f
