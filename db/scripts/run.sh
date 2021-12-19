#!/bin/bash

echo "Waiting for MySQL to start..."

until mysqladmin ping -h "$MYSQL_HOST" -P "$MYSQL_TCP_PORT" -u "$MYSQL_USER" -p"$MYSQL_PASSWORD" --silent; do
echo "Waiting for MySQL retry ..."
  sleep 1
done

echo "MySQL is now ready"
