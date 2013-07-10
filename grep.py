import sys

def grep():
    if len(sys.argv) != 3:
        print "Format:  --\"filename\" \"word\""
        exit()
    filename=sys.argv[1]
    wrd=sys.argv[2]
    f=open(filename,'r')
    lines=f.readlines()
    for line in lines:
        if wrd in line:
            print line,
    f.close()


if __name__=="__main__":
    grep()
