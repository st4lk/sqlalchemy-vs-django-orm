\c sqlal_project;

INSERT INTO fk_right select from generate_series(1, 100000);
INSERT INTO fk_left (right_id) select right_id from generate_series(1, 100000) right_id;
INSERT INTO fk_left_index (right_id) select right_id from generate_series(1, 100000) right_id;

-- deferred
INSERT INTO fk_left_deferred (right_id) select right_id from generate_series(1, 100000) right_id;

