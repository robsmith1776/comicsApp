    truncate table comics.information_backup;

    INSERT INTO comics.information_backup(
	id, cost, title, "number", releasedate)
	SELECT inf.*
	FROM comics.information inf
	left join comics.information_backup bk
	on bk.number = inf.number
	where bk.number is null;
	
	select count(1), e from
	(select id,number, row_number() over (PARTITION BY "number" order by id) as e
	from comics.information) tmp
	group by e
	
	
	select count(distinct number), count(number)
	from comics.information_backup;