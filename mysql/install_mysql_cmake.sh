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
tar_dir="${base_dir}mysql-5.7.17/"
ins_dir="${base_dir}mysql/"
mysqld="/etc/rc.d/init.d/mysqld"
db_user="admin"
db_pwd="7SlN*2AtWRzR%0mZ"

#Add user and group
g_info=`grep mysql /etc/group`
u_info=`grep mysql /etc/passwd`
if [ $g_info -ne " " ];then
	echo "The group already exists."
else;then
	groupadd mysql
fi

if [ $u_info -ne " " ]
	echo "The user already exists."
else;then
	useradd -r -g mysql mysql -s /sbin/nologin
fi

#create data catalog
mkdir -p $data_dir

#Installation dependency package
yum install -y ncurses-devel bison gcc gcc-c++ libaio

#download files
dl_dir="${base_dir}mysql-5.7.20-linux-glibc2.12-x86_64.tar.gz"
dl2_dir="${base_dir}boost_1_59_0.tar.gz"
if [ -d $dl_dir ];then
	wget http://mirrors.sohu.com/mysql/MySQL-5.7/mysql-5.7.17.tar.gz
else
	echo "$mysql tar file already exists."
fi

if [ -d $dl2_dir ];then
	wget https://nchc.dl.sourceforge.net/project/boost/boost/1.59.0/boost_1_59_0.tar.gz
else
	echo "boost_1_59_0.tar.gz already exist."

#unzip mysql

if [ -d "$ins_dir" ] && [ ! -d "$tar_dir" ] ;then
        echo mysql directory already exist !
elif [ ! -d "$ins_dir" ] && [ -d "$tar_dir" ];then
        mv $tar_dir $ins_dir
        echo Change catalog mysql-5.7.17 to mysql.
elif [ ! -d "$ins_dir" ] && [ ! -d "$tar_dir" ];then
        cd ${base_dir};tar xvf mysql-5.7.17.tar.gz
        mv $tar_dir $ins_dir
        echo  "unzip ...... done."
fi

#cmake compile
cd $ins_dir
sleep 1
cmake . -DCMAKE_INSTALL_PREFIX=$ins_dir \
-DMYSQL_DATADIR=/data/mysql \
-DMYSQL_TCP_PORT=2011 \
-DDEFAULT_CHARSET=utf8mb4 \
-DDEFAULT_COLLATION=utf8mb4_general_ci  \
-DEXTRA_CHARSETS=all  \
-DENABLED_LOCAL_INFILE=1 \
-DWITH_MYISAM_STORAGE_ENGINE=1 \
-DWITH_INNOBASE_STORAGE_ENGINE=1 \
-DWITH_MEMORY_STORAGE_ENGINE=1 \
-DWITH_ARCHIVE_STORAGE_ENGINE=1 \
-DWITH_BLACKHOLE_STORAGE_ENGINE=1 \
-DWITH_FEDERATED_STORAGE_ENGINE=1 \
-DDOWNLOAD_BOOST=1 \
-DWITH_BOOST=$base_dir
sleep 2
make && make install
sleep 1

#Modify the catalog
chown -R mysql.mysql $ins_dir
chown -R mysql.mysql $data_dir
#cd ${ins_dir}support-files


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

#register service
rm -rf ${data_dir}
killall mysqld
yes|cp ${ins_dir}support-files/mysql.server /etc/rc.d/init.d/mysqld

chmod 755 /etc/rc.d/init.d/mysqld
chkconfig --add mysqld
chkconfig mysqld on

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
mysql --defaults-file=/tmp/mysqluser --connect-expired-password <<EOF
set password = password('${db_pwd}');
grant all privileges on *.* to '${db_user}'@'%' identified by '${db_pwd}';
flush privileges;
EOF

echo "username:root   password:$db_pwd"
echo "username:$db_user  password:$db_pwd"
rm -rf /tmp/mysqluser
                    