psql commands
-------------

```sql
-- only once, if not created yet
CREATE USER appuser WITH password 'password';
ALTER USER appuser CREATEDB;

\c postgres;
drop database if exists django_project;
CREATE DATABASE django_project WITH TEMPLATE template0 OWNER appuser;
\c django_project;
```
