-- https://leetcode.com/problems/average-time-of-process-per-machine/?envType=study-plan-v2&envId=top-sql-50
-- Write your PostgreSQL query statement below
select machine_id, round((sum(duration) / count(1))::numeric, 3) as processing_time
from (
    select 
        machine_id,
        process_id,
        (   
            max(case when activity_type = 'end' then timestamp end) -
            max(case when activity_type = 'start' then timestamp end)
        ) 
        as duration
    from activity
    group by machine_id, process_id
)
group by machine_id
order by machine_id;


