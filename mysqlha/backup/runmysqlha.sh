#$1 remote
#$2 master
master_server=$1
demote_server=$2
echo ' mysqlhaha need input master_server demote_server'
#echo "stop remote server"
#ssh root@$demote_server "service mysql stop"
echo "smysqlhah atarting backup remote server"
sleep 1
#mysql -uroot -phello -h$demote_server -e "STOP SLAVE;"
#mysql -uroot -phello -h$demote_server -e "RESET SLAVE ALL"
#mysqlreplicate --master=root:hello@$master_server:3306 --slave=root:hello@$demote_server:3306

echo "mysqlhaha stop slave"
mysql -uroot -phello -h$demote_server -e "STOP SLAVE;"

mysql -uroot -phello -h$master_server -e "flush privileges;"
echo "mysqlhaha start to copy db"
innobackupex-1.5.1 --user=root --password=hello --no-timestamp --remote-host=root@$demote_server /mnt/monga/db/mysql  --tmpdir=/tmp
echo "mysqlhaha change owner"
ssh root@$demote_server "chown -R mysql:mysql /mnt/monga/db/mysql/*"
echo "mysqlhaha start slave"
mysql -uroot -phello -h$demote_server -e "START SLAVE;"


echo "mysqlhaha done"
