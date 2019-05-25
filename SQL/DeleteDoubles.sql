with cte as (
	select id,number, row_number() over (PARTITION BY "number" order by id) as e
	from comics.information
			)
	
delete from comics.information inf
using cte
where cte.id = inf.id
and cte.e = 2