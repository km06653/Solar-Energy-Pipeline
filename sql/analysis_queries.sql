-- Total solar energy generated

SELECT
    ROUND(
        SUM(total_yield)::numeric,
        2
    ) AS total_energy_generated
FROM solar_measurements;

-- Average daily energy output

SELECT
    DATE(date_time) AS production_date,

    ROUND(
        AVG(daily_yield)::numeric,
        2
    ) AS avg_daily_yield

FROM solar_measurements

GROUP BY production_date

ORDER BY production_date;

-- Solar inverter performance ranking

SELECT

    source_key,

    ROUND(
        AVG(conversion_efficiency)::numeric,
        4
    ) AS avg_efficiency


FROM solar_measurements


GROUP BY source_key


ORDER BY avg_efficiency DESC;

-- Energy generation by hour

SELECT

    EXTRACT(
        HOUR FROM date_time
    ) AS hour,


    ROUND(
        AVG(ac_power)::numeric,
        2
    ) AS avg_ac_power


FROM solar_measurements


GROUP BY hour


ORDER BY hour;

-- Data quality validation checks


SELECT

COUNT(*) AS total_records,


SUM(
CASE 
WHEN dc_power < 0 
THEN 1 
ELSE 0 
END

) AS invalid_power_records,


SUM(
CASE 
WHEN date_time IS NULL
THEN 1
ELSE 0
END

) AS missing_timestamps


FROM solar_measurements;


