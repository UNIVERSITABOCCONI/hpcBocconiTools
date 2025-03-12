#!/bin/bash

userListAsString=`getent passwd -s sss | awk -F':' '{ print $1 }' | tr '\n' ' '`

#check output
#echo $userListAsString

# Set the IFS (Internal Field Separator) to space
# Use read to bash convert string to array
IFS=' ' read -ra userListAsArray <<< "$userListAsString"


for username in "${userListAsArray[@]}"
do
	echo "-----------------  --------------"
	sacctmgr show user $username format=User,Account -p
	echo "-----------------  --------------"
done
##sacctmgr add user <username> account=def_acct partition=debug,defq,gpu,compute



