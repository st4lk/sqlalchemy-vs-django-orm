\c sqlal_project;

DELETE FROM relations_one_to_one_child;
DELETE FROM relations_child;
DELETE FROM relations_sub_child;
DELETE FROM relations_parent;

INSERT INTO relations_parent (id, value) values (1, 'math');
INSERT INTO relations_child (id, parent_id, value) values (1, 1, 'algebra');
INSERT INTO relations_child (id, parent_id, value) values (2, 1, 'geometry');
INSERT INTO relations_one_to_one_child (id, child_id, value) values (1, 1, 'plus');
INSERT INTO relations_one_to_one_child (id, child_id, value) values (2, 2, 'multiply');


INSERT INTO relations_parent (id, value) values (2, 'literature');
INSERT INTO relations_sub_child (id, value) values (1, 'Sergey Esenin');
INSERT INTO relations_sub_child (id, value) values (2, 'Leo Tolstoy');
INSERT INTO relations_child (id, parent_id, child_id, value) values (3, 2, 1, 'poetry');
INSERT INTO relations_child (id, parent_id, child_id, value) values (4, 2, 2, 'prose');
INSERT INTO relations_one_to_one_child (id, child_id, value) values (3, 3, 'rhyme');
INSERT INTO relations_one_to_one_child (id, child_id, value) values (4, 4, 'word');
