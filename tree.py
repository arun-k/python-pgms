import sys
import os

def tree(dir_name,offset=0):
    List=os.listdir(dir_name)
    for ele in List:
        print offset*" "+"|--"+ele
        if len(ele.split("."))==1:
            tree("/".join([dir_name,ele]),offset+3)
            

def list_files():
    if len(sys.argv) != 2:
        print "Format --\"dir-name\""
        exit()
    try:
        dir_name=sys.argv[1]
        print dir_name
        tree(dir_name)
    except OSError:
        print "Directory  \"%s\" doesn't exsist"%dir_name

if __name__=='__main__':
    list_files()
