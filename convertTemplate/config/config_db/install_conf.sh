#!/usr/bin/env bash
CWD=`pwd`
SCRIPT_DIR=`dirname $0`
#cd $CWD/$SCRIPT_DIR
cd $SCRIPT_DIR

mkdir -p /etc/rsyslog.d
cp rsyslog.conf /etc/rsyslog.conf
cp 50-default.conf /etc/rsyslog.d/.
cp install_conf.sh  /etc/rsyslog.d/.
cp monga.conf  /etc/rsyslog.d/.
cp mysql.conf  /etc/rsyslog.d/.

cp mongodb.conf /etc/.
