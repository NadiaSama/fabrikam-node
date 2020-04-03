#!/usr/bin/python

import daemon
import time

if __name__ == "__main__":
    with daemon.DaemonContext():
        with open("/tmp/dst.txt", "w") as fp:
            while True:
                fp.write("%s message\n", time.strftime("%Y-%m-%d %H:%M:%S"))
                time.sleep(5)

