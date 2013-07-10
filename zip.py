import zipfile
import sys

def main():
    if len(sys.argv) < 3:
        print 'Format --"archive name" "filenames"'
        sys.exit(0)
    archive=sys.argv[1]
    filenames=sys.argv[2:]
    z=zipfile.ZipFile(archive,'w')
    for f in filenames:
        z.write(f)
    z.close()


if __name__=='__main__':
    main()
