-- CREATE USER appuser WITH password 'password';
-- ALTER USER appuser CREATEDB;

drop database if exists django_project;
CREATE DATABASE django_project WITH TEMPLATE template0 OWNER appuser;

drop database if exists sqlal_project;
CREATE DATABASE sqlal_project WITH TEMPLATE template0 OWNER appuser;
