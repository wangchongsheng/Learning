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
tar_dir="${base_dir}mysql-5.7.17-linux-glibc2.5-x86_64/"
ins_dir="${base_dir}mysql/"
mysqld="/etc/rc.d/init.d/mysqld"

#Add user and group
g_info=`grep mysql /etc/group`
u_info=`grep mysql /etc/passwd`
if [ $g_info -ne " " ];then
	echo "The group already exists."
else
	groupadd mysql
fi

if [ $u_info -ne " " ]
	echo "The user already exists."
else
	useradd -r -g mysql mysql -s /sbin/nologin
fi

#create data catalog
mkdir -p $data_dir

#Installation dependency package
yum install -y ncurses-devel bison gcc gcc-c++

#download files
wget https://cdn.mysql.com//Downloads/MySQL-5.7/mysql-5.7.20-linux-glibc2.12-x86_64.tar.gz 

#unzip mysql

if [ -d "$ins_dir" ] && [ ! -d "$tar_dir" ] ;then
        echo mysql directory already exist !
elif [ ! -d "$ins_dir" ] && [ -d "$tar_dir" ];then
        mv $tar_dir $ins_dir
        echo Change catalog mysql-5.7.17 to mysql.
elif [ ! -d "$ins_dir" ] && [ ! -d "$tar_dir" ];then
        tar xvf ${base_dir}mysql-5.7.20-linux-glibc2.12-x86_64.tar.gz -C ${base_dir}
        mv $tar_dir $ins_dir
        echo The MySQL directory name is mysql.
fi


#Modify the catalog
cd $ins_dir
chown -R mysql.mysql $ins_dir
chown -R mysql.mysql $data_dir
#cd ${ins_dir}support-files

#register service
if [ -x "$mysqld" ];then
        echo File already exist !
elif [ ! -x "$mysqld" ];then
        cp ${ins_dir}support-files/mysql.server /etc/rc.d/init.d/mysqld
fi
chmod 755 /etc/rc.d/init.d/mysqld
chkconfig --add mysqld
chkconfig mysqld on
sleep 2
ln -s /opt/sygamer/src/mysql/bin/mysql /usr/bin/mysql
ln -s /opt/sygamer/src/mysql/bin/mysqladmin /usr/bin/mysqladmin
ln -s /opt/sygamer/src/mysql/bin/mysqldump /usr/bin/mysqldump
#Modify my.cnf file
cat > /etc/my.cnf <<EOF
[mysqld]
port = 3306
socket = /tmp/mysql.sock
 
basedir = ${base_dir}
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

#initialize msyql
/opt/sygamer/src/mysql/bin/mysqld --initialize

#建立临时账户文件
tmp_pwd=`grep "A temporary password is generated for root@localhost" /data/mysql/mysql-error.log |awk -F "t: " '{print$2}'`
cat > /tmp/mysqluser << EOF
[client]

user=root

password="${tmp_pwd}"
EOF

#
service mysqld start

#setting  user info
mysql  --defaults-file=/tmp/mysqluser -e "SET PASSWORD = PASSWORD('7SlN*2AtWRzR%0mZ');"
mysql  --defaults-file=/tmp/mysqluser -e "grant all privileges on *.* to admin@"%" identified by '7SlN*2AtWRzR%0mZ';"
flush privileges;
                    