\c sqlal_project;

select '-----pk_only-----';
explain analyse
    select * from pk_only where id=555;

select '-----pk_index-----';
explain analyse
    select * from pk_index where id=555;

select '-----pk_unique-----';
explain analyse
    select * from pk_unique where id=555;

select '-----pk_index_unique-----';
explain analyse
    select * from pk_index_unique where id=555;


select '---- insert duplicate into pk_only------';
insert into pk_only (id) values (555);
