import sys

def center():
    if len(sys.argv) != 2:
        print "Format:  --\"filename\""
        exit()
    filename=sys.argv[1]
    f=open(filename,'r')
    lines=f.readlines()
    width=len(max(lines,key=lambda x:len(x)))
    for line in lines:
        offset=(width-len(line))/2
        print offset*" " + line,
    f.close()


if __name__=="__main__":
    center()
