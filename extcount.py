import sys
import os

def extcount():
    if len(sys.argv) != 2:
        print "Format --\"dir-name\""
        exit()
    try:
        dic={}
        dir_name=sys.argv[1]
        files=os.listdir(dir_name)
        for f in files:
            ext=f.split(".")[-1]
            dic[ext]=dic.get(ext,0)+1
        for key,values in sorted(dic.items(),key=lambda x:x[1],reverse=True):
            print values,key
    except OSError:
        print "Directory  \"%s\" doesn't exsist"%dir_name

if __name__=='__main__':
    extcount()
