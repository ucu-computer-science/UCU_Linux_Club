#!/usr/bin/python
import os


def prgms():
    '''
    Returns list all installed programs which contain 'apps' or 'cs' or 'ba' case insensitive separated with ->.
    '''

    os.system('echo $(pacman -Q) > programs')

    with open('programs', 'r') as f:
        programs = f.readline()

    result = ''
    programs = programs.split()
    for i in range(0, len(programs), 2):
        if ('apps' in programs[i]) or ('cs' in programs[i]) or ('ba' in programs[i]):
            result += programs[i] + ' -> '

    print(result[:len(result)-4])

prgms()