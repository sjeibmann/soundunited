#!/usr/bin/ksh

PROCESSCOUNT=$(ps -ef |grep -v grep |grep shairport)

if [ $PROCESSCOUNT -eq 1 ]
then
	echo "daemon not found or is not running"
else
	echo "daemon is running"
fi
