#
# server_xinetd_put
# DataMover
#
# Created by Nehir Poyraz on 28.10.2018
# Copyright © 2018 Nehir Poyraz. All rights reserved.

import os
import hashlib
import sys


def loop():
    global sermd5
    while True:
        while True:
            m = hashlib.md5()
            filename = sys.stdin()
            try:
                file = open(filename)
                content = file.read()
                sys.stdout(True)
            except:
                sys.stdout(False)
                content = sys.stdin()
            finally:
                m.update(content)
                sermd5 = m.digest()


