psql commands
-------------

```sql
-- only once, if not created yet
CREATE USER appuser WITH password 'password';
ALTER USER appuser CREATEDB;

\c postgres;
drop database if exists sqlal_project;
CREATE DATABASE sqlal_project WITH TEMPLATE template0 OWNER appuser;
\c sqlal_project;

INSERT INTO m1 (field_a, field_b) values ('john', 'smith')
INSERT INTO m1 (field_a, field_b) values ('ivan', 'pupkin')


INSERT INTO m2 select from generate_series(1, 10000);
INSERT INTO m3 select from generate_series(1, 10000);
INSERT INTO m4 select from generate_series(1, 10000);
-- table size:
\dt+
-- index size:
\di+


explain analyse
select * from m2 where id=2345;

explain analyse
select * from m3 where id=2345;


# re-create db, i.e. clean it

INSERT INTO m4 select from generate_series(1, 100000);
INSERT INTO m5(m4_id) select m4_id from generate_series(1, 100000) m4_id;
INSERT INTO m6(m4_id) select m4_id from generate_series(1, 100000) m4_id;

explain analyse
select * from m5 inner join m4 on m4.id = m5.m4_id where m4.id = 8543;
explain analyse
select * from m6 inner join m4 on m4.id = m6.m4_id where m4.id = 8543;
```


Differences with django
-----------------------

- default nullable (not for PK)
	* Django: [False](https://docs.djangoproject.com/en/4.2/ref/models/fields/#django.db.models.Field.null)
	* SQLAlchemy: [True](https://docs.sqlalchemy.org/en/20/orm/mapping_api.html#sqlalchemy.orm.mapped_column.params.nullable)
