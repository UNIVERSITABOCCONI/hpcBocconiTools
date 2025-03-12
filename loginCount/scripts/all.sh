# clean
mv logins_* data_logins/
rm -f data.txt


echo -n "Enter year(YYYY) month(MM) and day(DD) of STARTdate and ENDdate of the stats: "
read YYYYs MMs DDs YYYYe MMe DDe

#echo "YYYYs = '$YYYYs'"
#echo "MMs = '$MMs'"
#echo "DDs = '$DDs'"
#echo "YYYYe = '$YYYYe'"
#echo "MMe = '$MMe'"
#echo "DDe = '$DDe'"

echo "python logins.py ${YYYYs}-${MMs}-${DDs} ${YYYYe}-${MMe}-${DDe}" 
#2024-04-08 2024-04-11 (startdate enddate)
#python process_files.py > data.txt
#python make_histo.py

#echo "histogram ready to be copied from your PC"
#echo "use the command:"
#echo "scp root@lnode01-da.hpc.unibocconi.it:/root/utilities/hpcBocconiTools/loginCount/scripts/logins_histo.png ."

