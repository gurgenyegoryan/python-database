#!/bin/bash

yum install mariadb-server -y
systemctl start mariadb


root_temp_pass=$(grep 'A temporary password' /var/log/mysqld.log |tail -1 |awk '{split($0,a,": "); print a[2]}')
echo "root_temp_pass:"$root_temp_pass

cat > mysql_secure_installation.sql << EOF
UPDATE mysql.user SET Password=PASSWORD('root_pass') WHERE User='root';
# Kill the anonymous users
DELETE FROM mysql.user WHERE User='';
# disallow remote login for root
#DELETE FROM mysql.user WHERE User='root' AND Host NOT IN ('localhost', '127.0.0.1', '::1');
# Make our changes take effect
FLUSH PRIVILEGES;
EOF
