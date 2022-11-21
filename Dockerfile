FROM centos:centos7.9.2009
#RUN cd /etc/yum.repos.d/ 
#RUN sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-* \
#    sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*
#RUN yum install update -y
RUN yum install wget -y
RUN wget https://downloads.mariadb.com/MariaDB/mariadb_repo_setup
RUN echo "367a80b01083c34899958cdd62525104a3de6069161d309039e84048d89ee98b  mariadb_repo_setup" \
    | sha256sum -c -

RUN chmod +x mariadb_repo_setup
RUN ./mariadb_repo_setup \
   --mariadb-server-version="mariadb-10.6"

  
RUN yum install MariaDB-shared MariaDB-devel -y
