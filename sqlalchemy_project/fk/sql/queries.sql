\c sqlal_project;

select '------ left join right -----';

EXPLAIN ANALYSE
SELECT * from fk_left
    left outer join fk_right on fk_left.right_id = fk_right.id
    where fk_right.id = 618;


EXPLAIN ANALYSE
SELECT * from fk_left_index
    left outer join fk_right on fk_left_index.right_id = fk_right.id
    where fk_right.id = 618;


select '------ right join left -----';

EXPLAIN ANALYSE
SELECT * from fk_right
    left outer join fk_left on fk_left.right_id = fk_right.id
    where fk_left.id = 512;


EXPLAIN ANALYSE
SELECT * from fk_right
    left outer join fk_left_index on fk_left_index.right_id = fk_right.id
    where fk_left_index.id = 512;


select '------ left join right deferred -----';

EXPLAIN ANALYSE
SELECT * from fk_left_deferred
    left outer join fk_right on fk_left_deferred.right_id = fk_right.id
    where fk_right.id = 618;
