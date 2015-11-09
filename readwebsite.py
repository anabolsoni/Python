import urllib2

#gets url and check its status code
def download(address):
    website = urllib2.urlopen(address)
    if website.code == 200:
        html = website.read()
        print html
    else:
        print "Not found"

def main():
    download('http://library.poly.edu/')

main()
