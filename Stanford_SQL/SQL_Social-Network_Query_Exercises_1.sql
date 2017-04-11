select distinct name 
from Highschooler
inner join Friend
    on ID=ID1
where (ID1 in (select ID from Highschooler where name = 'Gabriel')
or ID2 in (select ID from Highschooler where name = 'Gabriel'))
and name != 'Gabriel';
