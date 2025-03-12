#!/bin/bash

userListAsString=`getent passwd -s sss | awk -F':' '{ print $1 }' | tr '\n' ' '`

#check output
#echo $userListAsString

# Set the IFS (Internal Field Separator) to space
# Use read to bash convert string to array
IFS=' ' read -ra userListAsArray <<< "$userListAsString"


for username in "${userListAsArray[@]}"
do
	sacctmgr create account name=$username
	echo "----------------- Processing '$username' --------------"
	sacctmgr -i add user $username account=$username partition=debug,defq,gpu,compute,ice4hpc
	echo "----------------- '$username' processed --------------"
done
##sacctmgr add user <username> account=def_acct partition=debug,defq,gpu,compute



