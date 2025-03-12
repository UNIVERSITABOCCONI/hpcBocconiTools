#!/bin/bash

userListAsString=`getent group -s sss| grep grp_hpcclusterbocconiusers | cut -f 4 -d :`

#check output
#echo $userListAsString
#echo "-----------------  --------------"

# Set the IFS (Internal Field Separator) to space
# Use read to bash convert string to array
IFS=',' read -ra userListAsArray <<< "$userListAsString"

for username in "${userListAsArray[@]}";
do
	echo "$username"
        sreport cluster UserUtilizationByAccount user $username -T mem,cpu,gres/gpu Start=10/01 End=11/01
	echo "-----------------  --------------"

done

userListAsString_2=`getent group -s sss| grep grp_hpcclusterbocconiadmins | cut -f 4 -d :`
#check output
#echo $userListAsString_2

# Set the IFS (Internal Field Separator) to space
# Use read to bash convert string to array
IFS=',' read -ra userListAsArray_2 <<< "$userListAsString_2"

for username in "${userListAsArray_2[@]}"; 
do
        sreport cluster UserUtilizationByAccount user $username -T mem,cpu,gres/gpu Start=10/01 End=11/01
        echo "$username"
        echo "-----------------  --------------"

done


