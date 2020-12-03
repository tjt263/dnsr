#!/usr/bin/env python3

import sys
import socket

inputFile = sys.argv[1]

def longestLine(inputFile=inputFile):
    with open(inputFile, 'r') as f:
        return(len(max(f, key=len)))

def resolveHosts(columnWidth):
    with open(inputFile, 'r') as f:
        for line in f:
            host = line.strip()
            try:
                print(host.ljust(columnWidth) + socket.gethostbyname(host))
            except KeyboardInterrupt:
                sys.exit(0)
            except: #socket.gaierror:
                print(host.ljust(columnWidth) + '???')

def main():
    columnWidth = longestLine(inputFile)
    resolveHosts(columnWidth)
    
if __name__ == '__main__':
    main()
