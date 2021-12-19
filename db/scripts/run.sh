#!/bin/bash

echo "Waiting for MySQL to start..."

for i in `seq 0 30`
do
  mysqladmin ping -h "$MYSQL_HOST" -P "$MYSQL_TCP_PORT" -u "$MYSQL_USER" -p"$MYSQL_PASSWORD" --silent
  echo "Waiting for MySQL retry ..."
  sleep 2
done

echo "MySQL is now ready"
