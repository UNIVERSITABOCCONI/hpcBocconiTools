
mv table* last* remove/ 

#!/bin/bash
# read-multiple: read multiple values from keyboard
echo -n "Enter year(YYYY) month(MM) and day(DD) of starting date of the stats (2 weeks ago): "
read YYYY MM DD

#echo "YYYY = '$YYYY'"
#echo "MM = '$MM'"
#echo "DD = '$DD'"

last -s ${YYYY}${MM}${DD}000000 --time-format iso > last_timeformat_iso_today.txt

python maketable_1.py
python maketable_2.py
python maketable_3.py
python maketable_4.py
python maketable_5.py

echo " "
cat table_5.txt
echo " "

echo "table_5.txt ready to be copied from your laptop" 
echo "go to folder: cd /Users/argia/playground/python_/loginCount/newtable"
echo " "
echo "use the command:"
echo "scp root@lnode01-da.hpc.unibocconi.it:/root/utilities/hpcBocconiTools/loginCount/newtable/table_5.txt ."
echo " "


