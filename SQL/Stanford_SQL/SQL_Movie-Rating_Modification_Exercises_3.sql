update movie
set year = year + 25
where mID in (
  select mID from (
  select AVG(stars) as astar, mID from Rating
  where mID=rating.mID
  group by mID
  having astar >=4)
)
