# coding: utf-8
import os
import time

def playwav():
    time.sleep(1)
    os.system("cvlc 0.wav >& /dev/null &")

if __name__ == "__main__":
    t = 0.1
    lst = os.listdir(".")
    lst = filter(lambda x: x[-3:] == "txt", lst)
    playwav()
    for n in xrange(1, len(lst) + 1):
        os.system("clear")
        with open(str(n) + ".txt") as f:
            for x in f: print x,
            print n
            time.sleep(t)
