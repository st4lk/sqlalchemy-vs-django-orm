\c django_project;

select '------ left join right -----';

EXPLAIN ANALYSE
SELECT * from fk_fkleft
    left outer join fk_fkright on fk_fkleft.right_id = fk_fkright.id
    where fk_fkright.id = 618;


select '------ right join left -----';
EXPLAIN ANALYSE
SELECT * from fk_fkright
    left outer join fk_fkleft on fk_fkleft.right_id = fk_fkright.id
    where fk_fkleft.id = 512;
