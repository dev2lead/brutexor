#!/usr/bin/python
##
# Nicolas THIBAUT
# http://dev2lead.com
##

import sys

class BRUTEXOR:
    def __init__(self, xorfile, cmpfile):
        self.xorfile = open(xorfile, "r+b")
        self.cmpfile = open(cmpfile, "r+b")
    def __del__(self):
        self.xorfile.close()
        self.cmpfile.close()
    def bruteforce(self, keysize):
        keydata = []
        xordata = list(self.xorfile.read())
        cmpdata = list(self.cmpfile.read())
        for index in range(0, keysize):
            for element in range(0, 256):
                if chr(ord(xordata[index]) ^ ord(chr(element))) == cmpdata[index]:
                    keydata.append(chr(element))
        for index in range(0, len(xordata)):
            xordata[index] = chr(ord(xordata[index]) ^ ord(keydata[index % len(keydata)]))
        return self.save(xordata)
    def save(self, data):
        self.xorfile.seek(0)
        self.xorfile.write(str().join(data))
        self.xorfile.flush()
        return 0

def main():
    keysize = 256
    if "--keysize" in sys.argv:
        keysize = sys.argv[sys.argv.index("--keysize") + 1]
    if "--xorfile" in sys.argv and "--cmpfile" in sys.argv:
        xorfile = sys.argv[sys.argv.index("--xorfile") + 1]
        cmpfile = sys.argv[sys.argv.index("--cmpfile") + 1]
        BRUTEXOR(xorfile, cmpfile).bruteforce(keysize)
    return 0

if __name__ == "__main__":
    main()
