CREATE TABLE IF NOT EXISTS solar_measurements (

    measurement_id SERIAL PRIMARY KEY,

    date_time TIMESTAMP,

    plant_id VARCHAR(50),

    source_key VARCHAR(100),

    dc_power FLOAT,

    ac_power FLOAT,

    daily_yield FLOAT,

    total_yield FLOAT,

    conversion_efficiency FLOAT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);
