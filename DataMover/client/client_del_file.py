#
# client_del_file
# DataMover
#
# Created by Nehir Poyraz on 28.10.2018
# Copyright © 2018 Nehir Poyraz. All rights reserved.


def delete(file):
    """
        create a file on server
        :param file:
        :return:
    """
    """
    get file via stdin
    calculate MD5 
    if file exists locally:
        if file exists @server:
            calculate MD5 @server
            if MD5 and filesize match:
                delete
            else:
                "File found, unable to authenticate"
        else:
            "File can not be found"
    else:
        file delete is not permitted. 

    """