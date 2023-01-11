#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER music-app-user WITH PASSWORD T47CGcJXj40ME0pHs;
    CREATE DATABASE music-app;
    GRANT ALL PRIVILEGES ON DATABASE music-app TO music-app-user;
EOSQL