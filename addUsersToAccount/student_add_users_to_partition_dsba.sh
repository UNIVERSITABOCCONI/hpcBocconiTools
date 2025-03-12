#!/bin/bash

userListAsString=`getent group -s sss| grep grp_hpcclusterstudentsbocconiusers | cut -f 4 -d :`

#check output
#echo $userListAsString
#echo "-----------------  --------------"

# Set the IFS (Internal Field Separator) to space
# Use read to bash convert string to array
IFS=',' read -ra userListAsArray <<< "$userListAsString"


for username in "${userListAsArray[@]}"
do
	echo $username 
        sacctmgr -i add user $username account=$username partition=dsba

#	sacctmgr show user $username format=User,Account,Partition -p
	echo "-----------------  added to dsba partition --------------"
done
##sacctmgr add user <username> account=def_acct partition=debug,defq,gpu,compute



