import time

def profile(f):
    def g(x):
        start=time.clock()
        value=f(x)
        excTime=time.clock()-start
        print "Execution time: "+str(excTime)
        print "Value: "+str(value)
    return g
