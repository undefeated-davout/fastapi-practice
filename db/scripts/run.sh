#!/bin/bash

RETRY_COUNT=30
count=0

echo "Waiting for MySQL to start..."

while true
do
  mysqladmin ping -h "$MYSQL_HOST" -P "$MYSQL_TCP_PORT" -u "$MYSQL_USER" -p"$MYSQL_PASSWORD" --silent && break
  sleep 1
  echo $count
  count=`expr $count + 1`
  if [ $count -eq $RETRY_COUNT ]; then
    exit 1
  fi
done

echo "MySQL is now ready"
