DELETE FROM likes
where exists (select 1 from friend where friend.id1 = likes.id1 and friend.id2=likes.id2)
and not exists (select 1 from likes as L2 where L2.id1 = likes.id2 and L2.id2=likes.id1)
