#!/bin/sh

echo "CREATE DATABASE IF NOT EXISTS \`test_kodomo\` ;" | "${mysql[@]}"
echo "GRANT ALL ON \`test_kodomo\`.* TO '"$MYSQL_USER"'@'%' ;" | "${mysql[@]}"
echo 'FLUSH PRIVILEGES ;' | "${mysql[@]}"
