#
# client_put_file
# DataMover
#
# Created by Nehir Poyraz on 28.10.2018
# Copyright © 2018 Nehir Poyraz. All rights reserved.


def put(file):
    """
    create a file on server
    :param file:
    :return:
    """
    """
    get file via stdin
    calculate MD5
    if file exists @server:
        calculate MD5 @server
        if MD5 checksum matches:
            "file exists"
        else:
            "file is found but either corrupted, interrupted or outdated."

        if filesize matches:
            (This is the current implementation.)
            transfer file / calculate MD5
        else:
            transfer file / calculate MD5
            if MD5 mathes:
                "file is succesfully stores"
            else:
                "store failed"
                "retry recommended"


    else:
        "file is being stored"
        transfer file / calculate MD5
        if MD5 mathes:
            "file is succesfully stores"
        else:
            "store failed"
            "retry recommended"

    """