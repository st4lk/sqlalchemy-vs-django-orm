\c sqlal_project;

INSERT INTO pk_only select from generate_series(1, 10000);
INSERT INTO pk_index select from generate_series(1, 10000);
INSERT INTO pk_unique select from generate_series(1, 10000);
INSERT INTO pk_index_unique select from generate_series(1, 10000);
INSERT INTO pk_identity select from generate_series(1, 10000);
