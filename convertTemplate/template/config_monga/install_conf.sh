#!/usr/bin/env bash
CWD=`pwd`
SCRIPT_DIR=`dirname $0`
#cd $CWD/$SCRIPT_DIR
cd $SCRIPT_DIR

mkdir /etc/swift
cp monga.conf /etc/swift/.
cp notify-server.conf /etc/swift/.
cp swift.conf /etc/swift/.

