#!/usr/bin/python
import os

def ip_adress():
    '''
    Returns ip adress

    >>> ip_adress()
    127.0.1.1
    '''
    os.system('hostname -i')


ip_adress()