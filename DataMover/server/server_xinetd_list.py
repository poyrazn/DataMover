"#
# server_xinetd_list
# DataMover
#
# Created by Nehir Poyraz on 28.10.2018
# Copyright © 2018 Nehir Poyraz. All rights reserved.


import os
import sys


if __name__ == '__main__':
    print("Wellcome")
    print("please enter the string")
    sys.stdout.flush()
    line = sys.stdin.readline().strip()
    print("You entered %d characters." % len(line))
    sys.stdout.flush()
    # while True:
    #
    #     directory = '/Users/nehir/Desktop/test'
    #     if os.path.exists(directory) and os.path.isdir(directory):
    #         dirs = os.scandir(directory)
    #         if not dirs:
    #             print("There are no stored files.", flush=True)
    #         else:
    #             print('ls -la')
    #
    #     else:
    #         try:
    #             os.makedirs(directory)
    #             print("Data directory is created.")
    #         except OSError:
    #             print('Error: Directory couldn\'t been created. ' + directory)
