import urllib
import sys

def wget():
    if len(sys.argv) != 2:
        print "Format --\"URL\""
        exit()
    url=sys.argv[1]
    filename=url.split("/")[-1]
    if not filename:
        filename='index.html'
    urllib.urlretrieve(url,filename)
    print "saving "+url+" as "+filename

if __name__=='__main__':
    wget()
