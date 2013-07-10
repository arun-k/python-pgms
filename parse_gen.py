def parse_gen(filename,sep,cmnt):
    f=open(filename,'r')
    lines=f.readlines()
    a=[]
    for line in lines:
        if line[0]==cmnt:
            pass
        else:
            a.append([",".join(line.strip().split(sep))])
    return a
    
