#!/bin/bash

path=/Users/yhzm/Desktop/daiyang/project-dy/weblog/script

function parse() {
    date=$1
    mkdir -p $path/$date/
    python Trac.py $path/test/coolshell_$date.log  $path/$date/output.log $path/$date/dirty.log

}


# parse 20140301
# exit 0
# parse 20140212

parse 20140101
parse 20140102
parse 20140103
parse 20140104
parse 20140105
parse 20140106
parse 20140107