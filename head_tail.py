import sys

def head(filename):
    f=open(filename,'r')
    lines=f.readlines()
    for i in range(min(10,len(lines))):
        print lines[i]
    f.close()

def tail(filename):
    f=open(filename,'r')
    lines=f.readlines()
    for i in range(min(10,len(lines)),0,-1):
        print lines[len(lines)-i]
    f.close()

def main():
    if len(sys.argv) != 3:
        print "Format:  --[head or tail] \"filename\""
        exit()
    filename=sys.argv[2]
    if sys.argv[1]=='head':
        head(filename)
    elif sys.argv[1]=='tail':
        tail(filename)
    else:
        print "Format:  --[head or tail] \"filename\""

if __name__ == '__main__':
    main()
