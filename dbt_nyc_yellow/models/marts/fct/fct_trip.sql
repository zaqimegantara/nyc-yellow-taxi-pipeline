{{ config(materialized='table') }}

WITH trips AS (
    SELECT
        DATE(tpep_pickup_datetime) AS trip_date,
        pay.payment_description AS payment_description,
        rate.rate_description AS rate_description,
        passenger_count,
        trip_distance,
        total_amount,
        tip_amount,
        fare_amount
    FROM {{ ref('stg_taxi_data') }} t
    LEFT JOIN {{ ref('dim_payment_type') }} pay
        ON t.payment_type = pay.payment_type
    LEFT JOIN {{ ref('dim_rate_code') }} rate
        ON t.ratecodeid = rate.rate_code_id
)

SELECT
    trip_date,
    payment_description,
    rate_description,
    COUNT(*) AS total_trips,
    SUM(passenger_count) AS total_passengers,
    ROUND(AVG(trip_distance), 2) AS avg_trip_distance,
    ROUND(SUM(total_amount), 2) AS total_revenue,
    ROUND(SUM(tip_amount), 2) AS total_tips,
    ROUND(AVG(fare_amount), 2) AS avg_fare,
    ROUND(AVG(tip_amount), 2) AS avg_tip
FROM trips
GROUP BY trip_date, payment_description, rate_description
ORDER BY trip_date
