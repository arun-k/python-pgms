import sys

def reverse(List):
    for i in range(len(List)/2):
        List[i],List[-(i+1)]=List[-(i+1)],List[i]
    return List

def reverse_lines():
    filename=sys.argv[1]
    f=open(filename,'r')
    rev=reverse(f.readlines())
    for i in range(len(rev)):
	    print rev[i],

if __name__ == '__main__':
    reverse_lines()
