import sys

def wrap():
    if len(sys.argv) != 3:
        print "Format:  --\"filename\" \"width\""
        exit()
    filename=sys.argv[1]
    width=int(sys.argv[2])
    f=open(filename,'r')
    lines=f.readlines()
    for line in lines:
        if len(line) < width:
            print line,
        else:
            print line[:width]
            print line[width:]
    f.close()


if __name__=="__main__":
    wrap()
