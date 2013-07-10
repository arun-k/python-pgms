import sys
import os

def list_files():
    if len(sys.argv) != 2:
        print "Format --\"dir-name\""
        exit()
    try:
        dir_name=sys.argv[1]
        print os.listdir(dir_name)
    except OSError:
        print "Directory  \"%s\" doesn't exsist"%dir_name

if __name__=='__main__':
    list_files()
