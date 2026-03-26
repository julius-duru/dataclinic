import streamlit as st
import pandas as pd

TITLE = "Cleaning Specialized Data Sources: Surveys, Customer Input, Sensors & Logs"
CATEGORY = "data-science"
KEYWORDS = ["data cleaning", "survey data", "customer data", "sensor data", "log data", "IoT", "data quality", "ETL", "data preprocessing"]


def show():

    st.title(" Cleaning Specialized Data Sources")
    st.caption("Category: data-science | Level: Intermediate → Advanced")
    st.markdown("---")
    
    # INTRO
    st.write(
        """
        Not all data is created equal. Different data sources present unique challenges that require specialized 
        cleaning approaches. This guide covers four common data types that data scientists and analysts frequently encounter:
        
        - **Survey Data:** Subjective human responses with biases and inconsistencies
        - **Customer Input Data:** Typo-ridden, unstructured, and often intentionally misleading
        - **Sensor Data:** Machine-generated time-series with noise, drift, and dropouts
        - **Log Data:** High-volume machine-generated records with inconsistent formats
        
        Each data type requires tailored cleaning strategies to transform raw, messy inputs into analysis-ready datasets.
        """
    )

    # ============================================
    # SECTION 1: SURVEY DATA
    # ============================================
    st.header(" 1. Cleaning Survey Data")

    st.write(
        """
        Survey datasets are uniquely challenging because they involve human behavior. Respondents may skip questions, 
        provide inconsistent answers, or rush through surveys without reading questions properly.
        """
    )

    st.subheader("Common Problems in Survey Data")

    st.markdown(
        """
        | Problem | Description |
        |---------|-------------|
        | Missing responses | Questions skipped intentionally or accidentally |
        | Duplicate responses | Same respondent submits multiple times |
        | Inconsistent rating scales | Mix of 1-5 and 0-10 scales across questions |
        | Invalid answers | Text entered in numeric fields |
        | Straight-lining | Respondent selects same option repeatedly |
        | Out-of-range values | Values outside acceptable ranges |
        | Unqualified respondents | Participants who don't meet screening criteria |
        | Typos in open-ended questions | Spelling errors, slang, gibberish |
        """
    )

    st.subheader("1. Remove Unwanted Rows (Screen Out Unqualified Respondents)")

    st.code(
        """
-- Remove respondents who don't meet screening criteria
DELETE FROM survey_responses 
WHERE age < 18 
   OR country NOT IN ('USA', 'UK', 'Canada', 'Australia');

-- Remove respondents who failed attention check questions
DELETE FROM survey_responses 
WHERE attention_check != 'Correct Answer';

-- Remove respondents who didn't consent
DELETE FROM survey_responses 
WHERE consent_given = FALSE;
        """,
        language="sql"
    )

    st.subheader("2. Handle Missing Values by Type")

    st.code(
        """
-- A. Skipped multiple-choice questions → Label as 'Skipped'
UPDATE survey_responses 
SET favorite_color = 'Skipped' 
WHERE favorite_color IS NULL;

-- B. Skipped open-ended questions → Label as 'No Response'
UPDATE survey_responses 
SET feedback_text = 'No Response' 
WHERE feedback_text IS NULL OR TRIM(feedback_text) = '';

-- C. Missing numeric ratings → Replace with median (safer than mean for surveys)
WITH median_score AS (
    SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY satisfaction_score) AS med
    FROM survey_responses 
    WHERE satisfaction_score IS NOT NULL
)
UPDATE survey_responses 
SET satisfaction_score = (SELECT med FROM median_score)
WHERE satisfaction_score IS NULL;

-- D. Missing demographic data → Label as 'Prefer not to say'
UPDATE survey_responses 
SET income_bracket = 'Prefer not to say' 
WHERE income_bracket IS NULL;
        """,
        language="sql"
    )

    st.subheader("3. Fix Inconsistent Rating Scales")

    st.code(
        """
-- Normalize all scores to 0-10 scale
-- If survey used 1-5 scale originally
UPDATE survey_responses 
SET normalized_score = (rating_1_5 - 1) * (10 - 0) / (5 - 1) + 0;

-- If survey used 0-10 scale, keep as is
-- If survey used 1-7 scale
UPDATE survey_responses 
SET normalized_score = (rating_1_7 - 1) * (10 - 0) / (7 - 1) + 0;

-- Create a unified rating column
ALTER TABLE survey_responses ADD COLUMN unified_rating DECIMAL(5,2);

UPDATE survey_responses 
SET unified_rating = CASE 
    WHEN rating_scale = '1-5' THEN (rating_value - 1) * 2.5
    WHEN rating_scale = '0-10' THEN rating_value
    WHEN rating_scale = '1-7' THEN (rating_value - 1) * (10 / 6)
    ELSE NULL
END;
        """,
        language="sql"
    )

    st.subheader("4. Detect Poor-Quality Responses")

    st.code(
        """
-- A. Straight-lining detection (respondent selects same option repeatedly)
WITH straight_line AS (
    SELECT 
        respondent_id,
        COUNT(DISTINCT likert_answer) AS unique_answers,
        COUNT(*) AS total_questions
    FROM survey_responses
    GROUP BY respondent_id
)
SELECT * FROM straight_line
WHERE unique_answers = 1 
   OR (unique_answers = 2 AND total_questions > 10);

-- Flag straight-liners for review
ALTER TABLE survey_responses ADD COLUMN is_low_quality BOOLEAN DEFAULT FALSE;

UPDATE survey_responses sr
SET is_low_quality = TRUE
WHERE respondent_id IN (
    SELECT respondent_id
    FROM survey_responses
    GROUP BY respondent_id
    HAVING COUNT(DISTINCT likert_answer) = 1
);

-- B. Extremely fast completion time
DELETE FROM survey_responses 
WHERE completion_time_seconds < 20;

-- C. Pattern detection (all answers are extreme)
SELECT 
    respondent_id,
    AVG(satisfaction_score) AS avg_score,
    STDDEV(satisfaction_score) AS score_variance
FROM survey_responses
GROUP BY respondent_id
HAVING AVG(satisfaction_score) IN (1, 5, 10)
   AND STDDEV(satisfaction_score) < 0.5;
        """,
        language="sql"
    )

    st.subheader("5. Clean Open-Ended Text Answers")

    st.code(
        """
-- Remove emojis and special characters (MySQL)
UPDATE survey_responses 
SET feedback_text = REGEXP_REPLACE(feedback_text, '[^a-zA-Z0-9 .,!?-]', '');

-- Remove meaningless answers (gibberish)
DELETE FROM survey_responses 
WHERE LENGTH(feedback_text) < 3 
   OR feedback_text REGEXP '^[asdfghjkl]+$'
   OR feedback_text REGEXP '^[.?!]+$'
   OR feedback_text REGEXP '^[0-9]+$';

-- Flag answers with profanity
UPDATE survey_responses 
SET has_profanity = TRUE
WHERE feedback_text REGEXP (SELECT GROUP_CONCAT(word SEPARATOR '|') FROM profanity_list);
        """,
        language="sql"
    )

    st.subheader("6. Deduplicate Multiple Submissions")

    st.code(
        """
-- Keep only the most recent submission per respondent
WITH ranked_responses AS (
    SELECT 
        *,
        ROW_NUMBER() OVER (
            PARTITION BY email, respondent_id 
            ORDER BY submitted_at DESC
        ) AS rn
    FROM survey_responses
)
DELETE FROM survey_responses 
WHERE (email, respondent_id) IN (
    SELECT email, respondent_id 
    FROM ranked_responses 
    WHERE rn > 1
);
        """,
        language="sql"
    )

    st.subheader("7. Validate Logic-Based Responses")

    st.code(
        """
-- Check conditional logic (Q5 only asked if Q4 = 'Yes')
SELECT * FROM survey_responses 
WHERE q4 = 'No' AND q5 IS NOT NULL;

-- Fix or remove inconsistent responses
DELETE FROM survey_responses 
WHERE (q4 = 'No' AND q5 IS NOT NULL)
   OR (q4 IS NULL AND q5 IS NOT NULL);

-- Check age vs income consistency
SELECT * FROM survey_responses 
WHERE age < 18 AND income_bracket IN ('$100k+', '$150k+');

-- Check contradictory answers
SELECT * FROM survey_responses 
WHERE uses_product = 'Never' AND frequency_of_use != 'Never';
        """,
        language="sql"
    )

    st.divider()

    # ============================================
    # SECTION 2: CUSTOMER INPUT DATA
    # ============================================
    st.header(" 2. Cleaning Customer Input Data")

    st.write(
        """
        Customer-entered data from web forms, registrations, and e-commerce platforms is notoriously messy. 
        Users make typos, use inconsistent formats, and sometimes intentionally provide fake information.
        """
    )

    st.subheader("Common Problems in Customer Data")

    st.markdown(
        """
        - Typos and spelling errors
        - Inconsistent formatting (case, spaces, special characters)
        - Fake emails and phone numbers
        - Incomplete forms
        - Duplicate accounts
        - Invalid addresses
        """
    )

    st.subheader("1. Standardize Text Fields")

    st.code(
        """
-- Trim leading/trailing spaces
UPDATE customers 
SET 
    first_name = TRIM(first_name),
    last_name = TRIM(last_name),
    city = TRIM(city);

-- Capitalize names properly (PostgreSQL)
UPDATE customers 
SET 
    first_name = INITCAP(LOWER(first_name)),
    last_name = INITCAP(LOWER(last_name));

-- Remove multiple spaces
UPDATE customers 
SET address = REGEXP_REPLACE(address, '\\\\s+', ' ');
        """,
        language="sql"
    )

    st.subheader("2. Validate and Clean Emails")

    st.code(
        """
-- Basic email format validation
SELECT * FROM customers 
WHERE email NOT LIKE '%_@__%.__%' 
   OR email LIKE '% %' 
   OR email = '';

-- Remove emails with disposable domains
DELETE FROM customers 
WHERE email LIKE '%@tempmail.com'
   OR email LIKE '%@mailinator.com'
   OR email LIKE '%@guerrillamail.com'
   OR email LIKE '%@10minutemail.com';

-- Clean emails (lowercase, trim spaces)
UPDATE customers 
SET email = LOWER(TRIM(email));

-- Extract domain for analysis
ALTER TABLE customers ADD COLUMN email_domain VARCHAR(100);

UPDATE customers 
SET email_domain = SUBSTRING(email, POSITION('@' IN email) + 1);
        """,
        language="sql"
    )

    st.subheader("3. Validate and Clean Phone Numbers")

    st.code(
        """
-- Remove all non-numeric characters (PostgreSQL)
UPDATE customers 
SET phone = REGEXP_REPLACE(phone, '[^0-9]', '', 'g');

-- Remove fake numbers
DELETE FROM customers 
WHERE phone = '' 
   OR phone IS NULL
   OR phone = '0000000000'
   OR phone = '1234567890'
   OR LENGTH(phone) < 10;

-- Standardize US numbers to (XXX) XXX-XXXX format
UPDATE customers 
SET phone = CONCAT(
    '(', SUBSTRING(phone, 1, 3), ') ',
    SUBSTRING(phone, 4, 3), '-',
    SUBSTRING(phone, 7, 4)
)
WHERE LENGTH(phone) = 10;
        """,
        language="sql"
    )

    st.subheader("4. Deduplicate Customer Records")

    st.code(
        """
-- Find duplicates by email
SELECT email, COUNT(*) 
FROM customers 
GROUP BY email 
HAVING COUNT(*) > 1;

-- Keep most recent record based on last activity
WITH ranked_customers AS (
    SELECT 
        *,
        ROW_NUMBER() OVER (
            PARTITION BY LOWER(email) 
            ORDER BY last_login_date DESC, created_at DESC
        ) AS rn
    FROM customers
)
DELETE FROM customers 
WHERE (email) IN (
    SELECT email 
    FROM ranked_customers 
    WHERE rn > 1
);
        """,
        language="sql"
    )

    st.subheader("5. Identify Fake or Low-Quality Data")

    st.code(
        """
-- Find names with numbers
SELECT * FROM customers 
WHERE first_name REGEXP '[0-9]' 
   OR last_name REGEXP '[0-9]';

-- Find obvious fake names
SELECT * FROM customers 
WHERE first_name IN ('Test', 'Testing', 'User', 'Admin', '123', 'Qwerty')
   OR last_name IN ('Test', 'Testing', 'User', 'Admin', '123', 'Qwerty');

-- Flag suspicious records
ALTER TABLE customers ADD COLUMN is_suspicious BOOLEAN DEFAULT FALSE;

UPDATE customers 
SET is_suspicious = TRUE 
WHERE email LIKE '%@tempmail.com'
   OR phone = '0000000000'
   OR first_name REGEXP '[0-9]'
   OR last_name = '';
        """,
        language="sql"
    )

    st.subheader("6. Correct Incorrect Date Formats")

    st.code(
        """
-- Identify ambiguous date formats
SELECT birth_date FROM customers 
WHERE birth_date REGEXP '^[0-9]{2}/[0-9]{2}/[0-9]{4}$';

-- Flag impossible future dates
UPDATE customers 
SET birth_date = NULL 
WHERE birth_date > CURRENT_DATE;

-- Flag unrealistic ages
UPDATE customers 
SET is_suspicious = TRUE 
WHERE birth_date < '1900-01-01' 
   OR birth_date > (CURRENT_DATE - INTERVAL '10' YEAR);
        """,
        language="sql"
    )

    st.subheader("7. Normalize Addresses")

    st.code(
        """
-- Convert state abbreviations to full names
UPDATE customers 
SET state = CASE 
    WHEN state = 'CA' THEN 'California'
    WHEN state = 'NY' THEN 'New York'
    WHEN state = 'TX' THEN 'Texas'
    WHEN state = 'FL' THEN 'Florida'
    ELSE state
END;

-- Standardize street abbreviations
UPDATE customers 
SET address = REPLACE(address, 'St.', 'Street');
UPDATE customers 
SET address = REPLACE(address, 'Ave.', 'Avenue');

-- Validate address completeness
SELECT * FROM customers 
WHERE address IS NULL 
   OR city IS NULL 
   OR state IS NULL;
        """,
        language="sql"
    )

    st.divider()

    # ============================================
    # SECTION 3: SENSOR DATA (IoT, Manufacturing)
    # ============================================
    st.header(" 3. Cleaning Sensor Data (IoT, Manufacturing, Energy)")

    st.write(
        """
        Sensor data is machine-generated at high velocity. Common issues include missing timestamps, out-of-order events, 
        unrealistic values, calibration drift, noise, spikes, and communication dropouts.
        """
    )

    st.subheader("Common Problems in Sensor Data")

    st.markdown(
        """
        - Missing timestamps
        - Out-of-order events (jitter)
        - Sudden unrealistic values (spikes)
        - Calibration drift over time
        - Noise and signal interference
        - Duplicate readings
        - Communication dropouts
        """
    )

    st.subheader("1. Remove Duplicate Sensor Readings")

    st.code(
        """
-- Keep the latest reading for each sensor at each timestamp
WITH ranked_readings AS (
    SELECT 
        *,
        ROW_NUMBER() OVER (
            PARTITION BY sensor_id, timestamp 
            ORDER BY received_at DESC
        ) AS rn
    FROM sensor_data
)
DELETE FROM sensor_data 
WHERE (sensor_id, timestamp) IN (
    SELECT sensor_id, timestamp 
    FROM ranked_readings 
    WHERE rn > 1
);
        """,
        language="sql"
    )

    st.subheader("2. Fix Out-of-Order Data")

    st.code(
        """
-- Sort data chronologically for processing
SELECT * FROM sensor_data 
ORDER BY sensor_id, timestamp ASC;

-- Flag out-of-order records
ALTER TABLE sensor_data ADD COLUMN is_out_of_order BOOLEAN DEFAULT FALSE;

WITH ordered AS (
    SELECT 
        sensor_id,
        timestamp,
        LAG(timestamp) OVER (PARTITION BY sensor_id ORDER BY timestamp) AS prev_timestamp
    FROM sensor_data
)
UPDATE sensor_data sd
SET is_out_of_order = TRUE
FROM ordered o
WHERE sd.sensor_id = o.sensor_id 
  AND sd.timestamp = o.timestamp
  AND o.prev_timestamp > o.timestamp;
        """,
        language="sql"
    )

    st.subheader("3. Detect and Handle Impossible Values")

    st.code(
        """
-- Define realistic ranges per sensor type
-- Flag impossible values
UPDATE sensor_data 
SET is_invalid = TRUE 
WHERE (sensor_type = 'temperature' AND (value < -50 OR value > 150))
   OR (sensor_type = 'pressure' AND (value < 0 OR value > 1000))
   OR (sensor_type = 'speed' AND (value < 0 OR value > 200));

-- Replace with NULL for imputation
UPDATE sensor_data 
SET value = NULL 
WHERE is_invalid = TRUE;

-- Remove completely invalid records
DELETE FROM sensor_data 
WHERE value IS NULL AND sensor_type IN ('temperature', 'pressure', 'speed');
        """,
        language="sql"
    )

    st.subheader("4. Fix Missing Values with Forward Fill")

    st.code(
        """
-- Forward-fill missing values
UPDATE sensor_data t1
SET value = (
    SELECT value 
    FROM sensor_data t2 
    WHERE t2.sensor_id = t1.sensor_id 
      AND t2.timestamp < t1.timestamp 
      AND t2.value IS NOT NULL
    ORDER BY t2.timestamp DESC 
    LIMIT 1
)
WHERE value IS NULL;
        """,
        language="sql"
    )

    st.subheader("5. Smooth Noisy Data with Rolling Averages")

    st.code(
        """
-- 5-point moving average
SELECT 
    sensor_id,
    timestamp,
    value,
    AVG(value) OVER (
        PARTITION BY sensor_id 
        ORDER BY timestamp 
        ROWS BETWEEN 2 PRECEDING AND 2 FOLLOWING
    ) AS smoothed_value
FROM sensor_data;

-- Create smoothed version in a new table
CREATE TABLE sensor_data_smoothed AS
SELECT 
    sensor_id,
    timestamp,
    AVG(value) OVER (
        PARTITION BY sensor_id 
        ORDER BY timestamp 
        ROWS BETWEEN 5 PRECEDING AND CURRENT ROW
    ) AS smoothed_value
FROM sensor_data;
        """,
        language="sql"
    )

    st.subheader("6. Handle Telemetry Dropouts")

    st.code(
        """
-- Detect gaps > 2 minutes
WITH gaps AS (
    SELECT 
        sensor_id,
        timestamp,
        LAG(timestamp) OVER (PARTITION BY sensor_id ORDER BY timestamp) AS prev_timestamp,
        EXTRACT(EPOCH FROM (timestamp - LAG(timestamp) OVER (PARTITION BY sensor_id ORDER BY timestamp))) AS gap_seconds
    FROM sensor_data
)
SELECT * FROM gaps 
WHERE gap_seconds > 120;

-- Flag dropout periods
ALTER TABLE sensor_data ADD COLUMN is_dropout BOOLEAN DEFAULT FALSE;

WITH gaps AS (
    SELECT 
        sensor_id,
        timestamp,
        CASE 
            WHEN EXTRACT(EPOCH FROM (timestamp - LAG(timestamp) OVER (PARTITION BY sensor_id ORDER BY timestamp))) > 120 
            THEN TRUE 
            ELSE FALSE 
        END AS is_gap
    FROM sensor_data
)
UPDATE sensor_data sd
SET is_dropout = TRUE
FROM gaps g
WHERE sd.sensor_id = g.sensor_id 
  AND sd.timestamp = g.timestamp 
  AND g.is_gap = TRUE;
        """,
        language="sql"
    )

    st.subheader("7. Resample to Consistent Time Intervals")

    st.code(
        """
-- Aggregate to per-minute averages (PostgreSQL)
SELECT 
    sensor_id,
    DATE_TRUNC('minute', timestamp) AS minute_slot,
    AVG(value) AS avg_value,
    MIN(value) AS min_value,
    MAX(value) AS max_value,
    COUNT(*) AS reading_count
FROM sensor_data
GROUP BY sensor_id, DATE_TRUNC('minute', timestamp)
ORDER BY sensor_id, minute_slot;
        """,
        language="sql"
    )

    st.divider()

    # ============================================
    # SECTION 4: LOG DATA
    # ============================================
    st.header(" 4. Cleaning Log Data (Web, API, Server, Audit)")

    st.write(
        """
        Logs are generated by machines at massive scale. They contain noise, redundant information, inconsistent formats, 
        timestamps from different time zones, missing fields, and corrupted lines.
        """
    )

    st.subheader("Common Problems in Log Data")

    st.markdown(
        """
        - Corrupted or malformed entries
        - Inconsistent timestamp formats and timezones
        - Missing fields
        - Duplicate log entries
        - Bot traffic and noise
        - Unstructured text requiring parsing
        - Mixed log levels and formats
        """
    )

    st.subheader("1. Standardize Timestamps to UTC")

    st.code(
        """
-- Convert timestamps to UTC (PostgreSQL)
UPDATE logs 
SET timestamp = timestamp AT TIME ZONE 'America/New_York' AT TIME ZONE 'UTC'
WHERE timezone = 'EST';

-- Flag records with invalid timestamps
ALTER TABLE logs ADD COLUMN has_valid_timestamp BOOLEAN DEFAULT FALSE;

UPDATE logs 
SET has_valid_timestamp = TRUE 
WHERE timestamp IS NOT NULL 
  AND timestamp > '2020-01-01' 
  AND timestamp < CURRENT_DATE + INTERVAL '1 day';
        """,
        language="sql"
    )

    st.subheader("2. Remove Corrupted Entries")

    st.code(
        """
-- Remove entries that don't match expected log format
DELETE FROM logs 
WHERE raw_log NOT REGEXP '^[0-9]{4}-[0-9]{2}-[0-9]{2}';

-- Filter out malformed lines
DELETE FROM logs 
WHERE raw_log IS NULL 
   OR TRIM(raw_log) = ''
   OR LENGTH(raw_log) < 10;
        """,
        language="sql"
    )

    st.subheader("3. Parse Log Strings into Structured Columns")

    st.code(
        """
-- Apache/Nginx log format example
-- 127.0.0.1 - - [10/Oct/2025:13:55:36 +0000] "GET /index HTTP/1.1" 200 2326

-- Extract IP (MySQL)
UPDATE logs 
SET ip_address = SUBSTRING_INDEX(raw_log, ' ', 1);

-- Extract HTTP method
UPDATE logs 
SET http_method = SUBSTRING_INDEX(
    SUBSTRING_INDEX(SUBSTRING_INDEX(raw_log, '"', 2), '"', -1), 
    ' ', 
    1
);

-- Extract status code
UPDATE logs 
SET status_code = CAST(
    SUBSTRING_INDEX(SUBSTRING_INDEX(raw_log, '"', -2), ' ', 2) AS UNSIGNED
);
        """,
        language="sql"
    )

    st.subheader("4. Deduplicate Log Entries")

    st.code(
        """
-- Keep unique entries based on event signature
WITH ranked_logs AS (
    SELECT 
        *,
        ROW_NUMBER() OVER (
            PARTITION BY event_id, timestamp, source_ip 
            ORDER BY received_at DESC
        ) AS rn
    FROM logs
)
DELETE FROM logs 
WHERE id IN (
    SELECT id FROM ranked_logs WHERE rn > 1
);
        """,
        language="sql"
    )

    st.subheader("5. Handle Missing Fields")

    st.code(
        """
-- Fill missing user agents
UPDATE logs 
SET user_agent = 'Unknown' 
WHERE user_agent IS NULL OR user_agent = '';

-- Fill missing referers
UPDATE logs 
SET referer = 'Direct' 
WHERE referer IS NULL OR referer = '';

-- Flag incomplete records
ALTER TABLE logs ADD COLUMN is_complete BOOLEAN DEFAULT FALSE;

UPDATE logs 
SET is_complete = TRUE 
WHERE ip_address IS NOT NULL 
  AND timestamp IS NOT NULL 
  AND endpoint IS NOT NULL;
        """,
        language="sql"
    )

    st.subheader("6. Detect and Filter Bot Traffic")

    st.code(
        """
-- Identify bots by user agent
UPDATE logs 
SET is_bot = TRUE 
WHERE user_agent LIKE '%bot%'
   OR user_agent LIKE '%crawler%'
   OR user_agent LIKE '%spider%'
   OR user_agent LIKE '%scraper%';

-- Detect bots by request frequency
WITH request_counts AS (
    SELECT 
        ip_address,
        COUNT(*) AS requests_per_minute,
        DATE_TRUNC('minute', timestamp) AS minute_slot
    FROM logs
    GROUP BY ip_address, DATE_TRUNC('minute', timestamp)
)
UPDATE logs 
SET is_bot = TRUE 
WHERE ip_address IN (
    SELECT ip_address 
    FROM request_counts 
    WHERE requests_per_minute > 100
);

-- Remove bot traffic from analytics
CREATE TABLE logs_human_only AS
SELECT * FROM logs 
WHERE is_bot = FALSE;
        """,
        language="sql"
    )

    st.subheader("7. Remove Noise and Irrelevant Entries")

    st.code(
        """
-- Remove health check pings
DELETE FROM logs 
WHERE endpoint = '/health' 
   OR endpoint = '/ping' 
   OR endpoint = '/favicon.ico';

-- Remove internal monitoring traffic
DELETE FROM logs 
WHERE user_agent LIKE '%monitoring%'
   OR source_ip IN ('127.0.0.1', 'localhost');

-- Filter to relevant log levels only
DELETE FROM logs 
WHERE log_level NOT IN ('ERROR', 'WARN', 'INFO');
        """,
        language="sql"
    )

    st.subheader("8. Sessionization from Clickstream Logs")

    st.code(
        """
-- Create sessions: new session after 30 minutes of inactivity
WITH sessionized AS (
    SELECT 
        user_id,
        timestamp,
        page_url,
        LAG(timestamp) OVER (PARTITION BY user_id ORDER BY timestamp) AS prev_timestamp,
        CASE 
            WHEN EXTRACT(EPOCH FROM (timestamp - LAG(timestamp) OVER (PARTITION BY user_id ORDER BY timestamp))) > 1800
            THEN 1
            ELSE 0
        END AS new_session_flag
    FROM clickstream_logs
),
session_numbers AS (
    SELECT 
        *,
        SUM(new_session_flag) OVER (PARTITION BY user_id ORDER BY timestamp) AS session_id
    FROM sessionized
)
SELECT 
    user_id,
    session_id,
    MIN(timestamp) AS session_start,
    MAX(timestamp) AS session_end,
    COUNT(*) AS page_views
FROM session_numbers
GROUP BY user_id, session_id;
        """,
        language="sql"
    )

    st.divider()

    # ============================================
    # SUMMARY TABLE
    # ============================================
    st.header(" Summary: Data Type Comparison")

    st.write(
        """
        Each data type requires specific cleaning approaches. This table summarizes the most critical issues and key techniques:
        """
    )

    summary_data = {
        "Data Type": ["Survey Data", "Customer Input", "Sensor Data", "Log Data"],
        "Most Critical Issues": [
            "Missing responses, bias, straight-lining, inconsistent scales",
            "Typos, duplicates, fake emails/phones, incomplete forms",
            "Noise, dropouts, drift, out-of-order, impossible values",
            "Corruption, inconsistent formats, bots, noise"
        ],
        "Key Cleaning Techniques": [
            "Imputation, logic validation, scale normalization, text cleaning",
            "Regex validation, standardization, deduplication, address normalization",
            "Smoothing, interpolation, drift correction, resampling",
            "Parsing, timestamp normalization, bot filtering, sessionization"
        ]
    }

    df_summary = pd.DataFrame(summary_data)
    st.dataframe(df_summary, use_container_width=True)

    st.divider()

    # ============================================
    # BEST PRACTICES
    # ============================================
    st.header(" Best Practices for Specialized Data Cleaning")

    st.markdown(
        """
        **1. Understand the Data Source**
        - Survey data: Consider human psychology and survey design
        - Customer data: Account for user behavior and intent
        - Sensor data: Understand physical constraints and hardware limitations
        - Log data: Know the logging framework and infrastructure
        
        **2. Document All Cleaning Decisions**
        - Record why certain records were removed
        - Document imputation methods and assumptions
        - Maintain audit trails for compliance
        
        **3. Create Clean Copies, Don't Overwrite Raw Data**
        - Always keep an untouched version of raw data
        - Create new tables or datasets for cleaned data
        """
    )