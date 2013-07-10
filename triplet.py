def triplet(num):
    return [(x,y,z) for x in range(num) for y in range(x,num) for z in range(y,num) if x+y==z]
