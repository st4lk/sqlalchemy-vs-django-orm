\c django_project;

INSERT INTO pk_pkonly select from generate_series(1, 10000);
