insert into Friend (id1, id2)
select DISTINCT i1, i2 from (
  select F1.id1 as i1, F2.id2 as i2
  from friend F1  join friend F2 on F1.id2 = F2.id1
) as t
where t.i1 != t.i2
and not exists (select 1 from Friend where id1=i1 and id2=i2)
and not exists (select 1 from Friend where id2=i1 and id1=i2)
