
FROM mysql

ENV MYSQL_DATABASE myCompany-notifications
ENV MYSQL_ROOT_PASSWORD myCompany-rocks

EXPOSE 3306
COPY ./sql-scripts/ /docker-entrypoint-initdb.d/
