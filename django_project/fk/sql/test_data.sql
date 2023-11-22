\c django_project;

INSERT INTO fk_fkright select from generate_series(1, 10000);
INSERT INTO fk_fkleft (right_id) select right_id from generate_series(1, 10000) right_id;

