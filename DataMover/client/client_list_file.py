#
# client_list_file
# DataMover
#
# Created by Nehir Poyraz on 28.10.2018
# Copyright © 2018 Nehir Poyraz. All rights reserved.

import sys
import os


def list(directory):
    """
    :param directory:
    :return:
    """
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
            os.listdir(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


if __name__ == '__main__':
    list()