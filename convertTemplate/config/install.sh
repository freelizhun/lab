#!/usr/bin/env bash
CWD=`pwd`
SCRIPT_DIR=`dirname $0`
#cd $CWD/$SCRIPT_DIR
cd $SCRIPT_DIR

cp -rf keystone /etc/.
sleep 1
cp -rf apache2 /etc/.
sleep 1
cp php5/apache2/* /etc/php5/apache2/.
sleep 1
a2ensite admin-portal-ssl
sleep 1
a2ensite user-portal-ssl
sleep 1
a2enmod ssl
sleep 1
#cd config_db
./config_db/install_conf.sh
sleep 1
#cd ..
./config_monga/install_conf.sh
#bash install_conf.sh
sleep 1
cp haproxy/haproxy /etc/default/haproxy -f
cp haproxy/haproxy.cfg /etc/haproxy/haproxy.cfg -f
sleep 1
./backup/install_conf.sh
sleep 1
#cd ..
mkdir -p /mnt/monga/mongo
chown -R mongodb:nogroup /mnt/monga/mongo
mkdir -p /mnt/monga/db/mysql
chown -R mysql:nogroup /mnt/monga/db/mysql
ln -fs /etc/apache2/sites-available/user-portal /etc/apache2/sites-enabled/.

