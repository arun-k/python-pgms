def parse_csv(filename):
    f=open(filename,'r')
    lines=f.readlines()
    a=[]
    for line in lines:
        a.append([line.strip()])
    return a
    
