#!/bin/bash

userListAsString=`getent group -s sss| grep grp_hpcclusterbocconiusers | cut -f 4 -d :`

#check output
echo $userListAsString
echo "-----------------  --------------"

# Set the IFS (Internal Field Separator) to space
# Use read to bash convert string to array
IFS=',' read -ra userListAsArray <<< "$userListAsString"


for username in "${userListAsArray[@]}"
do
	echo $username 
#        sacctmgr -i add user $username account=$username partition=stata

#	sacctmgr show user $username format=User,Account,Partition -p
	echo "-----------------  --------------"
done
##sacctmgr add user <username> account=def_acct partition=debug,defq,gpu,compute



