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
RUN chmod +x python_installer.sh
RUN ./python_installer.sh
#RUN apt-get update -y
#RUN apt-get install -y libmariadb-dev
#RUN apt install libmariadb3 libmariadb-dev -y

WORKDIR /app
COPY . .

#RUN chmod +x ./mariadbSserver_install_configure.sh

# RUN ./mariadbSserver_install_configure.sh


# CMD [ "python3", "main.py" ]
