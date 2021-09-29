#!/usr/bin/env python3

import os
import time
import sys
import getopt


def shutdownHNow(seconds):
    time.sleep(seconds)
    os.system("pkill -f firefox")
    time.sleep(5)
    os.system("shutdown -h now")


def main(argv):
    secFromHorMorS = 0
    try:
        opts, args = getopt.getopt(
            argv, "h:m:s:", ["hours=", "minutes=", "seconds="])
        if len(opts) == 0:
            raise
    except (getopt.GetoptError, Exception):
        print('sleepify.py -h <hours>  -m <minutes> -s <seconds> ')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '--help':
            print('sleepify.py -h <hours>  -m <minutes> -s <seconds> ')
            sys.exit()
        else:
            if opt in ("-h", "--hours"):
                secFromHorMorS += int(arg, 10) * 3600
                continue
            if opt in ("-m", "--minutes"):
                secFromHorMorS += int(arg, 10) * 60
                continue
            if opt in ("-s", "--seconds"):
                secFromHorMorS += int(arg, 10)
            else:
                print(
                    "Arguments not found : sleepify.py -h <hours>  -m <minutes> -s <seconds> ")
                sys.exit(2)

    shutdownHNow(secFromHorMorS)

if __name__ == "__main__":
    main(sys.argv[1:])
