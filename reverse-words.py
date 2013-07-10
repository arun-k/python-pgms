import sys

def reverse_lines():
    filename=sys.argv[1]
    f=open(filename,'r')
    for line in f.readlines():
	for i in range(len(line.split())-1,-1,-1):
            print line.split()[i],
        print "\n",

if __name__ == '__main__':
    reverse_lines()
