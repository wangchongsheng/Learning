#!/bin/bash
#copyright
#
#wang_chongsheng@163.com
#
#2017-07-05
#
#MySQL Automatic deployment of script files
echo "==========================================="
echo "            MySQL installation             "
echo "==========================================="

base_dir="/opt/sygamer/src/"
data_dir="/data/mysql/"
tar_dir="${base_dir}mysql-5.7.20-linux-glibc2.12-x86_64/"
ins_dir="${base_dir}mysql/"
mysqld="/etc/rc.d/init.d/mysqld"
db_user="admin"
db_pwd="7SlN*2AtWRzR%0mZ"

#Add user and group
g_info=`grep mysql /etc/group`
u_info=`grep mysql /etc/passwd`
if [ $g_info == "" ];then
	groupadd mysql
else
	echo "The group already exists."
fi

if [ $u_info == "" ];then
	useradd -r -g mysql mysql -s /sbin/nologin
else
	echo "The user already exists."
fi

#create data catalog
#mkdir -p $data_dir

#Installation dependency package
yum install -y ncurses-devel bison gcc gcc-c++ libaio


#download files
dl_dir="${base_dir}mysql-5.7.20-linux-glibc2.12-x86_64.tar.gz"
if [ -d $dl_dir  ] ;then
	wget -P ${base_dir} https://cdn.mysql.com//Downloads/MySQL-5.7/mysql-5.7.20-linux-glibc2.12-x86_64.tar.gz 
else
	echo "File already exists."
fi

#unzip mysql

if [ -d "$ins_dir" ] && [ ! -d "$tar_dir" ] ;then
        echo mysql directory already exist !
elif [ ! -d "$ins_dir" ] && [ -d "$tar_dir" ];then
        mv $tar_dir $ins_dir
        echo Change catalog name to mysql.
elif [ ! -d "$ins_dir" ] && [ ! -d "$tar_dir" ];then
        cd ${base_dir};tar xvf mysql-5.7.20-linux-glibc2.12-x86_64.tar.gz 
        mv $tar_dir $ins_dir
        echo The file name is changed to MySQL.
fi


#Modify the catalog
#cd $ins_dir
chown -R mysql.mysql $ins_dir
chown -R mysql.mysql $data_dir
#cd ${ins_dir}support-files

#Soft link file

rm -rf /usr/bin/mysql*
ln -s /opt/sygamer/src/mysql/bin/mysql /usr/bin/mysql
ln -s /opt/sygamer/src/mysql/bin/mysqladmin /usr/bin/mysqladmin
ln -s /opt/sygamer/src/mysql/bin/mysqldump /usr/bin/mysqldump

#Modify my.cnf file
cat > /etc/my.cnf <<EOF
[mysqld]
port = 3306
socket = /tmp/mysql.sock
 
basedir = ${ins_dir}
datadir = ${data_dir}
pid-file = ${data_dir}mysql.pid
user = mysql
#The server ID must be modified
server-id = 91
 
log_bin = mysql-bin
relay-log = mysql-relay-bin
log-slave-updates
 
sync_binlog=1
#setting offset
auto_increment_offset=1
auto_increment_increment=1
 
#setting log path
 
log_error = ${data_dir}mysql-error.log
slow_query_log_file = ${data_dir}mysql-slow.log
EOF

#register mysql service
rm -rf ${data_dir}
killall mysqld
${ins_dir}bin/mysqld --initialize --user=mysql --basedir=${ins_dir} --datadir=${data_dir}

yes|cp ${ins_dir}support-files/mysql.server /etc/rc.d/init.d/mysqld

chmod 755 /etc/rc.d/init.d/mysqld
chkconfig --add mysqld
chkconfig mysqld on

#create user file
tmp_pwd=`grep "A temporary password is generated for root@localhost" /data/mysql/mysql-error.log |awk -F "t: " '{print$2}'`
cat > /tmp/mysqluser << EOF
[client]

user=root

password="${tmp_pwd}"

port=3306
EOF

#
service mysqld start

#setting  user info
mysql --defaults-file=/tmp/mysqluser --connect-expired-password <<EOF
set password = password('${db_pwd}');
grant all privileges on *.* to '${db_user}'@'%' identified by '${db_pwd}';
flush privileges;
EOF

echo "username:root   password:$db_pwd"
echo "username:$db_user  password:$db_pwd"
rm -rf /tmp/mysqluser
