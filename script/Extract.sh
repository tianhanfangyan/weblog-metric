#!/bin/bash


#prime number 691, 751, 941, 1103, 1327, 1559, 1783
#extract seven days weblog for example

path=/Users/yhzm/Desktop/daiyang/project-dy/weblog/script
mkdir -p $path/ods/

awk 'NR%691==1' $path/coolshell.log > $path/ods/coolshell_20140101_ods.log
awk 'NR%751==1' $path/coolshell.log > $path/ods/coolshell_20140102_ods.log
awk 'NR%941==1' $path/coolshell.log > $path/ods/coolshell_20140103_ods.log
awk 'NR%1103==1' $path/coolshell.log > $path/ods/coolshell_20140104_ods.log
awk 'NR%1327==1' $path/coolshell.log > $path/ods/coolshell_20140105_ods.log
awk 'NR%1559==1' $path/coolshell.log > $path/ods/coolshell_20140106_ods.log
awk 'NR%1783==1' $path/coolshell.log > $path/ods/coolshell_20140107_ods.log


#replace the date

function replace_date(){
    date=$1
    day=$2
    mkdir -p $path/test
    #[12/Feb/2014:03:08:11 +0800] 
    sed -e "s#12/Feb/2014#0$day/Jan/2014#g"  $path/ods/coolshell_$date\_ods.log > $path/test/coolshell_$date.log
}

replace_date 20140101 1
replace_date 20140102 2
replace_date 20140103 3
replace_date 20140104 4
replace_date 20140105 5
replace_date 20140106 6
replace_date 20140107 7