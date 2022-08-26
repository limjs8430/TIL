-- https://school.programmers.co.kr/learn/courses/30/lessons/59034
SELECT * from ANIMAL_INS order by ANIMAL_ID;


-- https://school.programmers.co.kr/learn/courses/30/lessons/59035
SELECT NAME, DATETIME from ANIMAL_INS order by ANIMAL_ID desc;

-- https://school.programmers.co.kr/learn/courses/30/lessons/59036
SELECT ANIMAL_ID, NAME from ANIMAL_INS where INTAKE_CONDITION = 'Sick' order by ANIMAL_ID;

-- https://school.programmers.co.kr/learn/courses/30/lessons/59037
SELECT ANIMAL_ID, NAME from ANIMAL_INS  where INTAKE_CONDITION != 'Aged' order by ANIMAL_ID;

-- https://school.programmers.co.kr/learn/courses/30/lessons/59403
SELECT ANIMAL_ID, NAME from ANIMAL_INS order by ANIMAL_ID;

-- https://school.programmers.co.kr/learn/courses/30/lessons/59404
SELECT ANIMAL_ID, NAME, DATETIME from ANIMAL_INS 
order by NAME asc, DATETIME desc;

-- https://school.programmers.co.kr/learn/courses/30/lessons/59405
SELECT NAME from ANIMAL_INS order by DATETIME limit 1;

-- https://school.programmers.co.kr/learn/courses/30/lessons/59415
SELECT max(DATETIME) from ANIMAL_INS ;

-- https://school.programmers.co.kr/learn/courses/30/lessons/59038
SELECT min(DATETIME) from ANIMAL_INS ;

-- https://school.programmers.co.kr/learn/courses/30/lessons/59406
SELECT count(*) from ANIMAL_INS ;

-- https://school.programmers.co.kr/learn/courses/30/lessons/59408
SELECT count(distinct(name)) from ANIMAL_INS ;

-- https://school.programmers.co.kr/learn/courses/30/lessons/59040
SELECT ANIMAL_TYPE, count(*) from ANIMAL_INS group by ANIMAL_TYPE order by ANIMAL_TYPE;

-- https://school.programmers.co.kr/learn/courses/30/lessons/59041
SELECT NAME, COUNT(*) from ANIMAL_INS where NAME is not NULL
group by NAME having COUNT(*) >= 2 order by NAME;

-- https://school.programmers.co.kr/learn/courses/30/lessons/59412
SELECT hour(DATETIME) as HOUR, COUNT(*) from ANIMAL_OUTS 
group by HOUR having HOUR between 9 and 19
order by HOUR;

-- https://school.programmers.co.kr/learn/courses/30/lessons/59413
-- 실패!!


-- https://school.programmers.co.kr/learn/courses/30/lessons/59039
SELECT ANIMAL_ID from ANIMAL_INS where NAME is NULL order by ANIMAL_ID;

-- https://school.programmers.co.kr/learn/courses/30/lessons/59407
SELECT ANIMAL_ID from ANIMAL_INS where NAME is not NULL order by ANIMAL_ID;

-- https://school.programmers.co.kr/learn/courses/30/lessons/59410
SELECT  ANIMAL_TYPE, 
CASE WHEN NAME IS NOT NULL THEN NAME 
ELSE 'No name' END AS "NAME", 
SEX_UPON_INTAKE
FROM    ANIMAL_INS
ORDER BY ANIMAL_ID;


-- https://school.programmers.co.kr/learn/courses/30/lessons/59042
SELECT ANIMAL_OUTS.ANIMAL_ID , ANIMAL_OUTS.NAME from ANIMAL_OUTS 
left join ANIMAL_INS  on ANIMAL_OUTS.ANIMAL_ID = ANIMAL_INS.ANIMAL_ID
where ANIMAL_INS.ANIMAL_ID IS NULL order by ANIMAL_ID;

-- https://school.programmers.co.kr/learn/courses/30/lessons/59043
SELECT ANIMAL_INS.ANIMAL_ID, ANIMAL_INS.NAME from ANIMAL_INS 
join ANIMAL_OUTS on ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID
where ANIMAL_INS.DATETIME > ANIMAL_OUTS.DATETIME order by ANIMAL_INS.DATETIME;

-- https://school.programmers.co.kr/learn/courses/30/lessons/59044
SELECT ANIMAL_INS.NAME, ANIMAL_INS.DATETIME
from ANIMAL_INS left join ANIMAL_OUTS  on ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID
where ANIMAL_OUTS.DATETIME is null order by ANIMAL_INS.DATETIME limit 3;

-- https://school.programmers.co.kr/learn/courses/30/lessons/59045
SELECT ANIMAL_INS.ANIMAL_ID, ANIMAL_INS.ANIMAL_TYPE, ANIMAL_INS.NAME from ANIMAL_INS 
join ANIMAL_OUTS on ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID
where (ANIMAL_INS.SEX_UPON_INTAKE = 'Intact Male' or ANIMAL_INS.SEX_UPON_INTAKE = 'Intact Female')
and (ANIMAL_OUTS.SEX_UPON_OUTCOME = 'Neutered Male' or ANIMAL_OUTS.SEX_UPON_OUTCOME = 'Spayed Female')
order by ANIMAL_INS.ANIMAL_ID;

-- https://school.programmers.co.kr/learn/courses/30/lessons/59046
SELECT  ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM    ANIMAL_INS
WHERE   NAME IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
ORDER BY ANIMAL_ID;

-- https://school.programmers.co.kr/learn/courses/30/lessons/59047
SELECT ANIMAL_ID, NAME from ANIMAL_INS where NAME like '%el%' and ANIMAL_TYPE ='Dog' order by NAME;

-- https://school.programmers.co.kr/learn/courses/30/lessons/59409
SELECT ANIMAL_ID, NAME, 
case when SEX_UPON_INTAKE like '%Neutered%' or SEX_UPON_INTAKE like '%Spayed%' then 'O'
else 'X'
end as '중성화'
from ANIMAL_INS
order by ANIMAL_ID;

-- https://school.programmers.co.kr/learn/courses/30/lessons/59411
SELECT ANIMAL_INS.ANIMAL_ID, ANIMAL_INS.NAME 
from ANIMAL_INS join ANIMAL_OUTS on ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID
order by ANIMAL_OUTS.DATETIME - ANIMAL_INS.DATETIME desc limit 2;

-- https://school.programmers.co.kr/learn/courses/30/lessons/59414
SELECT ANIMAL_ID, NAME, date_format(DATETIME, "%Y-%m-%d") as '날짜'
FROM ANIMAL_INS
ORDER BY ANIMAL_ID






















