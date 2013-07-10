import sys

def readfile(filename):
    for line in open(filename):
        yield line

def main():
    if len(sys.argv) != 3:
        print 'Format --"limit" "filename"'
        sys.exit(0)
    filename=sys.argv[2]
    limit=int(sys.argv[1])
    f=open(filename,'r')
    tot_lines=len(f.readlines())
    f.close()
    parts=tot_lines / limit
    reminder=tot_lines%limit
    open_code="fw=open(\"%s_part%s.txt\",'w')"
    lines=readfile(filename)
    try:
        for i in range(parts):
            exec(open_code %(filename,str(i+1)))
            for j in range(limit):
                fw.write(lines.next())
            fw.close()
        fw=open("rest.txt",'w')
        for k in range(reminder):
            fw.write(lines.next())
        fw.close()
        print "Splitting of files done....!!!!"
    except StopIteration,e:
        print "An error occured!!!%s"%str(e)


if __name__=='__main__':
    main()
