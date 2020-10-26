#! /usr/local/bin/bash
# > ./keylogger.sh output.log
# a keylogger that takes output file path as a command line argument and for every command
# entered by the user performs it and stores it with a timestamp in the output file


# get output file path
output_file=$1

# empty the output file
> $output_file

# display the first prompt
printf "> "

while read curr_command
do
    # construct current date in a format year:month:day|hours|minutes|seconds
    curr_time=`date +"%Y:%m:%d|%T"`

    # add date and command to the output file
    echo "[${curr_time}] ${curr_command}" >> $output_file

    # evaluate the command
    eval $curr_command

    # display the next prompt
    printf "> "
done < '/dev/stdin'