#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER waves-user WITH PASSWORD T47CGcJXj40ME0pHs;
    CREATE DATABASE waves-db;
    GRANT ALL PRIVILEGES ON DATABASE waves-db TO waves-user;
EOSQL