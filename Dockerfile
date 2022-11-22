FROM mariadb:latest

RUN apt update -y
RUN apt upgrade -y
RUN apt install wget curl -y
#RUN cd /etc/yum.repos.d/
#RUN sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-* \
#    sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*
#RUN yum install update -y
RUN wget https://downloads.mariadb.com/MariaDB/mariadb_repo_setup
RUN echo "367a80b01083c34899958cdd62525104a3de6069161d309039e84048d89ee98b  mariadb_repo_setup" \
    | sha256sum -c -

RUN chmod +x mariadb_repo_setup
RUN ./mariadb_repo_setup \
   --mariadb-server-version="mariadb-10.6"

RUN apt-get update -y
RUN apt-get install -y libmariadb3

COPY python_installer.sh python_installer.sh
RUN chmod +x python_installer.sh
RUN ./python_installer.sh

RUN wget http://archive.ubuntu.com/ubuntu/pool/universe/m/mariadb-10.6/libmariadb-dev_10.6.7-2ubuntu1_amd64.deb
RUN dpkg -i libmariadb-dev_10.6.7-2ubuntu1_amd64.deb
RUN wget http://archive.ubuntu.com/ubuntu/pool/main/g/glibc/libc6_2.35-0ubuntu3.1_amd64.deb
RUN dpkg -i libc6_2.35-0ubuntu3.1_amd64.deb
RUN apt-get install libc6
RUN wget http://archive.ubuntu.com/ubuntu/pool/universe/m/mariadb-10.6/libmariadb3_10.6.7-2ubuntu1_amd64.deb
RUN dpkg -i libmariadb3_10.6.7-2ubuntu1_amd64.deb
RUN wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl-dev_3.0.2-0ubuntu1_amd64.deb
RUN dpkg -i libssl-dev_3.0.2-0ubuntu1_amd64.deb
RUN rm -Rf /etc/apt/sources.list.d/mariadb.list.old_1
RUN apt-get update
RUN apt-get install libssl-dev
RUN apt-get install libmariadb-dev
RUN pip3 install mariadb
#RUN apt install libmariadb3 libmariadb-dev -y

COPY mariadbSserver_install_configure.sh mariadbSserver_install_configure.sh
RUN chmod +x ./mariadbSserver_install_configure.sh
RUN ./mariadbSserver_install_configure.sh
WORKDIR /app
COPY . .

# CMD [ "python3", "main.py" ]
