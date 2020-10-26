#!/bin/env python
# Return the list of programs which have ba cs or apps in them
import os
# Write the programs list in a file
os.system('echo $(pacman -Q) > programs.txt')

with open('programs.txt', 'r') as f:
    # Read it into a string
    programs_str = f.read()
    f.close()

# Split it by spaces
programs_list = programs_str.split()
# We only take even arguments becouse odd are versions
for i in range(0, len(programs_list), 2):
    if 'ba' in programs_list[i]:
        print(programs_list[i], end=' -> ')
    elif 'cs' in programs_list[i]:
        print(programs_list[i], end=' -> ')
    elif 'apps' in programs_list[i]:
        print(programs_list[i], end=' -> ')

# Remove the last arrow
print('\b'*4, end='')
print(' '*4)

