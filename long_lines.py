import sys

def readfiles(filenames):
    for f in filenames:
        for line in open(f):
            yield line

def long_lines(lines):
    return (line for line in lines if len(line)>40)

def printlines(lines):
    for line in lines:
        print line,

def main():
    if len(sys.argv)<2:
        print 'Format --"filename(s)"'
    try:
        filenames=sys.argv[1:]
        lines = readfiles(filenames)
        lines = long_lines(lines)
        printlines(lines)
    except IOError, e:
        print >> sys.stderr, "Unable to open the file.\n%s" %str(e)

if __name__=='__main__':
    main()
