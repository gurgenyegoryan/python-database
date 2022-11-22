#!/bin/bash

service mariadb start

aptitude -y install expect

// Not required in actual script
MYSQL_ROOT_PASSWORD=abcd1234

SECURE_MYSQL=$(expect -c "
set timeout 10
spawn mysql_secure_installation
expect \"Enter current password for root (enter for none):\"
send \"$MYSQL\r\"
expect \"Change the root password?\"
send \"n\r\"
expect \"Remove anonymous users?\"
send \"y\r\"
expect \"Disallow root login remotely?\"
send \"y\r\"
expect \"Remove test database and access to it?\"
send \"y\r\"
expect \"Reload privilege tables now?\"
send \"y\r\"
expect eof
")

echo "$SECURE_MYSQL"

aptitude -y purge expect
#apt update
#apt install mariadb-server -y
#service mariadb start
#root_temp_pass=Yeg.1995
#echo "root_temp_pass:"$root_temp_pass

#cat > mysql_secure_installation.sql << EOF
#UPDATE mysql.user SET Password=PASSWORD('Yeg.1995') WHERE User='root';
## Kill the anonymous users
#DELETE FROM mysql.user WHERE User='';
## disallow remote login for root
##DELETE FROM mysql.user WHERE User='root' AND Host NOT IN ('localhost', '127.0.0.1', '::1');
## Make our changes take effect
#FLUSH PRIVILEGES;
#EOF
#mysql -uroot -p"$Yeg.1995" --connect-expired-password <mysql_secure_installation.sql
