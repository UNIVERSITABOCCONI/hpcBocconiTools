#!/bin/bash

basePath="/root/utilities/hpcBocconiTools/loginCount/newtable/"
rm -rf ${basePath}remove/*
mv ${basePath}table_* ${basePath}last* ${basePath}remove/ 

start_day=$(date --date="${date} -14 day" +%Y%m%d)

/bin/last -s ${start_day}000000 --time-format iso > ${basePath}last_timeformat_iso_today.txt

/software/miniconda3/bin/python ${basePath}maketable_1.py $basePath
/software/miniconda3/bin/python ${basePath}maketable_2.py $basePath
/software/miniconda3/bin/python ${basePath}maketable_3.py $basePath
/software/miniconda3/bin/python ${basePath}maketable_4.py $basePath
/software/miniconda3/bin/python ${basePath}maketable_5.py $basePath


