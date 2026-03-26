import streamlit as st
import pandas as pd

TITLE = "Comprehensive Guide to Data Cleaning in SQL"
CATEGORY = "data_engineering"
KEYWORDS = ["data cleaning", "SQL", "data preprocessing", "data quality", "ETL", "data wrangling", "MySQL", "PostgreSQL", "data validation"]


def show():

    st.title("Comprehensive Guide to Data Cleaning in SQL")
    st.caption("Category: data_engineering | Level: Intermediate → Advanced")
    st.markdown("---")
    
    # INTRO
    st.write(
        """
        Data cleaning (or data preprocessing) in SQL is the organized process of detecting, correcting, 
        and removing inaccurate, inconsistent, or incomplete data directly at the database level. 
        
        This guide provides a systematic approach to data cleaning that can be applied across various domains:
        finance, marketing, telecom, manufacturing, HR, sales, customer analytics, e-commerce, and more.
        
        The 8-step framework covered in this guide includes:
        
        1. Remove irrelevant data
        2. Remove duplicate data
        3. Fix structural errors
        4. Convert data types
        5. Handle missing data
        6. Deal with outliers
        7. Standardize/Normalize data
        8. Validate data
        """
    )

    # SECTION 1: UNDERSTAND THE DATA
    # -------------------------
    st.header("1. Understand the Data (The First Essential Step)")

    st.write(
        """
        Before cleaning, always explore your data. Understanding the structure, quality, and content of your dataset 
        is crucial for making informed cleaning decisions.
        """
    )

    st.subheader("Initial Data Exploration Queries")

    st.code(
        """
-- Preview the first 10 rows
SELECT * FROM table_name LIMIT 10;

-- Get total row count
SELECT COUNT(*) AS total_rows FROM table_name;

-- Inspect data types and structure
DESCRIBE table_name;
-- or for PostgreSQL
SELECT column_name, data_type 
FROM information_schema.columns 
WHERE table_name = 'table_name';

-- Check for NULL values in each column
SELECT 
    COUNT(*) AS total_rows,
    SUM(CASE WHEN column1 IS NULL THEN 1 ELSE 0 END) AS column1_nulls,
    SUM(CASE WHEN column2 IS NULL THEN 1 ELSE 0 END) AS column2_nulls,
    SUM(CASE WHEN column3 IS NULL THEN 1 ELSE 0 END) AS column3_nulls
FROM table_name;

-- Get summary statistics for numeric columns
SELECT 
    MIN(amount) AS min_value,
    MAX(amount) AS max_value,
    AVG(amount) AS avg_value,
    STDDEV(amount) AS std_dev,
    COUNT(*) AS total_count
FROM transactions;
        """,
        language="sql"
    )

    # SECTION 2: REMOVE DUPLICATES
    # -------------------------
    st.header("2. Remove Duplicate Data")

    st.write(
        """
        Duplicate records can bias analysis and lead to inaccurate insights. Here's how to identify and remove them.
        """
    )

    st.subheader("Find Duplicates")

    st.code(
        """
-- Find duplicates based on specific columns
SELECT 
    customer_id, 
    email, 
    COUNT(*) AS duplicate_count
FROM customers
GROUP BY customer_id, email
HAVING COUNT(*) > 1;

-- Find complete row duplicates
SELECT *, COUNT(*) AS duplicate_count
FROM customers
GROUP BY 
    customer_id, 
    first_name, 
    last_name, 
    email, 
    phone
HAVING COUNT(*) > 1;
        """,
        language="sql"
    )

    st.subheader("Remove Duplicates (Keep One Instance)")

    st.code(
        """
-- Method 1: Using ROW_NUMBER() (Works in MySQL 8+, PostgreSQL, SQL Server)
WITH ranked_rows AS (
    SELECT 
        *,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id, email 
            ORDER BY created_at DESC
        ) AS row_num
    FROM customers
)
DELETE FROM customers 
WHERE (customer_id, email) IN (
    SELECT customer_id, email 
    FROM ranked_rows 
    WHERE row_num > 1
);

-- Method 2: Create a clean table without duplicates (Safer approach)
CREATE TABLE customers_clean AS
SELECT DISTINCT * FROM customers;

-- Method 3: For tables with a unique ID, keep the latest record
WITH ranked_rows AS (
    SELECT 
        *,
        ROW_NUMBER() OVER (
            PARTITION BY email 
            ORDER BY created_at DESC
        ) AS row_num
    FROM customers
)
SELECT * INTO customers_clean
FROM ranked_rows 
WHERE row_num = 1;
        """,
        language="sql"
    )

    # SECTION 3: FIX STRUCTURAL ERRORS
    # -------------------------
    st.header("3. Fix Structural Errors")

    st.write(
        """
        Structural errors include inconsistent capitalization, misspellings, and inconsistent naming conventions.
        """
    )

    st.subheader("Standardize Capitalization")

    st.code(
        """
-- Convert to UPPER case
UPDATE customers 
SET country = UPPER(country);

-- Convert to PROPER case (First letter capitalized, rest lower)
-- MySQL
UPDATE customers 
SET city = CONCAT(UPPER(LEFT(city, 1)), LOWER(SUBSTRING(city, 2)));

-- PostgreSQL
UPDATE customers 
SET city = INITCAP(city);

-- Convert to LOWER case
UPDATE customers 
SET email = LOWER(email);
        """,
        language="sql"
    )

    st.subheader("Standardize Categorical Values")

    st.code(
        """
-- Standardize gender values
UPDATE customers 
SET gender = CASE 
    WHEN gender IN ('M', 'Male', 'male', 'MALE', 'm') THEN 'Male'
    WHEN gender IN ('F', 'Female', 'female', 'FEMALE', 'f') THEN 'Female'
    ELSE 'Unknown'
END;

-- Standardize status values
UPDATE orders 
SET status = CASE 
    WHEN status IN ('P', 'PENDING', 'pending', 'pend') THEN 'Pending'
    WHEN status IN ('C', 'COMPLETED', 'completed', 'complete') THEN 'Completed'
    WHEN status IN ('S', 'SHIPPED', 'shipped') THEN 'Shipped'
    WHEN status IN ('R', 'REFUNDED', 'refunded') THEN 'Refunded'
    ELSE 'Other'
END;
        """,
        language="sql"
    )

    st.subheader("Clean String Fields")

    st.code(
        """
-- Remove leading and trailing spaces
UPDATE customers 
SET first_name = TRIM(first_name),
    last_name = TRIM(last_name);

-- Remove multiple spaces within text
-- MySQL
UPDATE customers 
SET address = REGEXP_REPLACE(address, '\\s+', ' ');

-- PostgreSQL
UPDATE customers 
SET address = REGEXP_REPLACE(address, '\\s+', ' ', 'g');

-- Clean phone numbers (remove non-numeric characters)
-- MySQL
UPDATE customers 
SET phone = REGEXP_REPLACE(phone, '[^0-9]', '');

-- PostgreSQL
UPDATE customers 
SET phone = REGEXP_REPLACE(phone, '[^0-9]', '', 'g');
        """,
        language="sql"
    )

    st.info(
        "**Reservation:** Standardization should be domain-guided. Never overwrite values unless the rule is approved by business stakeholders."
    )

    # SECTION 4: CONVERT DATA TYPES
    # -------------------------
    st.header("4. Convert Data Types (Type Casting)")

    st.write(
        """
        Data often arrives with incorrect data types. Proper type conversion ensures accurate calculations and efficient storage.
        """
    )

    st.subheader("Convert VARCHAR to DATE")

    st.code(
        """
-- MySQL: STR_TO_DATE
UPDATE sales 
SET order_date = STR_TO_DATE(order_date, '%Y-%m-%d');

-- MySQL: Handle different date formats
UPDATE sales 
SET order_date = STR_TO_DATE(order_date, '%d/%m/%Y');

-- PostgreSQL: CAST or :: syntax
UPDATE sales 
SET order_date = order_date::DATE;

-- PostgreSQL: TO_DATE for custom formats
UPDATE sales 
SET order_date = TO_DATE(order_date, 'DD/MM/YYYY');
        """,
        language="sql"
    )

    st.subheader("Convert Strings with Symbols to Numeric")

    st.code(
        """
-- Remove currency symbols and convert to decimal
-- MySQL
UPDATE products 
SET price = CAST(REPLACE(REPLACE(price, '$', ''), ',', '') AS DECIMAL(10,2));

-- PostgreSQL
UPDATE products 
SET price = REPLACE(REPLACE(price, '$', ''), ',', '')::DECIMAL(10,2);

-- Convert percentage strings to decimal
UPDATE products 
SET discount = CAST(REPLACE(discount, '%', '') AS DECIMAL(5,2)) / 100;
        """,
        language="sql"
    )

    st.subheader("Convert Text to Numeric")

    st.code(
        """
-- MySQL: CAST
UPDATE transactions 
SET amount = CAST(amount_text AS DECIMAL(15,2));

-- Handle conversion errors with NULL
-- MySQL
UPDATE transactions 
SET amount = CASE 
    WHEN amount_text REGEXP '^[0-9]+\\.?[0-9]*$' 
    THEN CAST(amount_text AS DECIMAL(15,2))
    ELSE NULL 
END;
        """,
        language="sql"
    )

    # SECTION 5: HANDLE MISSING DATA
    # -------------------------
    st.header("5. Handle Missing Data (NULL Values)")

    st.write(
        """
        Missing data is common in real-world datasets. The strategy for handling it depends on the data type and business context.
        """
    )

    st.subheader("Find Missing Values")

    st.code(
        """
-- Check for NULL values in specific columns
SELECT * 
FROM customers 
WHERE occupation IS NULL;

-- Count NULL values per column
SELECT 
    SUM(CASE WHEN first_name IS NULL THEN 1 ELSE 0 END) AS missing_first_name,
    SUM(CASE WHEN last_name IS NULL THEN 1 ELSE 0 END) AS missing_last_name,
    SUM(CASE WHEN email IS NULL THEN 1 ELSE 0 END) AS missing_email,
    SUM(CASE WHEN phone IS NULL THEN 1 ELSE 0 END) AS missing_phone,
    COUNT(*) AS total_rows
FROM customers;

-- Calculate percentage of missing values
SELECT 
    ROUND(SUM(CASE WHEN email IS NULL THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS email_missing_pct
FROM customers;
        """,
        language="sql"
    )

    st.subheader("Handling Categorical Missing Data")

    st.code(
        """
-- Option 1: Label as 'Missing' or 'Unknown'
UPDATE customers 
SET occupation = 'Missing' 
WHERE occupation IS NULL;

UPDATE customers 
SET gender = 'Unknown' 
WHERE gender IS NULL;

-- Option 2: Fill with mode (most frequent value)
UPDATE customers c
SET occupation = (
    SELECT occupation 
    FROM customers 
    WHERE occupation IS NOT NULL 
    GROUP BY occupation 
    ORDER BY COUNT(*) DESC 
    LIMIT 1
)
WHERE occupation IS NULL;
        """,
        language="sql"
    )

    st.subheader("Handling Numerical Missing Data")

    st.code(
        """
-- Option 1: Replace with mean (average)
UPDATE customers 
SET income = (
    SELECT AVG(income) 
    FROM customers 
    WHERE income IS NOT NULL
)
WHERE income IS NULL;

-- Option 2: Replace with median (works in MySQL 8+, PostgreSQL)
-- MySQL (using window functions)
WITH median_calc AS (
    SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY income) OVER () AS median_income
    FROM customers
    WHERE income IS NOT NULL
    LIMIT 1
)
UPDATE customers 
SET income = (SELECT median_income FROM median_calc)
WHERE income IS NULL;

-- PostgreSQL (median calculation)
UPDATE customers 
SET income = (
    SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY income)
    FROM customers
    WHERE income IS NOT NULL
)
WHERE income IS NULL;

-- Option 3: Replace with zero (for count-based fields)
UPDATE inventory 
SET quantity = 0 
WHERE quantity IS NULL;
        """,
        language="sql"
    )

    st.info(
        "**Reservations:** Using mean assumes normally distributed data. Median is better for skewed distributions. "
        "Always validate imputation choices with domain experts."
    )

    # SECTION 6: DEAL WITH OUTLIERS
    # -------------------------
    st.header("6. Deal with Outliers")

    st.write(
        """
        Outliers are extreme values that can skew statistical measures and destabilize machine learning models.
        """
    )

    st.subheader("Calculate Quantiles and IQR")

    st.code(
        """
-- PostgreSQL: Calculate Q1, Q3, and IQR
WITH quartiles AS (
    SELECT 
        PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY amount) AS q1,
        PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY amount) AS q3
    FROM transactions
)
SELECT 
    q1,
    q3,
    (q3 - q1) AS iqr,
    q1 - (1.5 * (q3 - q1)) AS lower_bound,
    q3 + (1.5 * (q3 - q1)) AS upper_bound
FROM quartiles;

-- MySQL 8+: Calculate quartiles using window functions
WITH ordered AS (
    SELECT 
        amount,
        NTILE(4) OVER (ORDER BY amount) AS quartile
    FROM transactions
)
SELECT 
    MAX(CASE WHEN quartile = 1 THEN amount END) AS q1,
    MAX(CASE WHEN quartile = 3 THEN amount END) AS q3
FROM ordered;
        """,
        language="sql"
    )

    st.subheader("Detect Outliers")

    st.code(
        """
-- Detect outliers using IQR method
WITH stats AS (
    SELECT 
        PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY amount) AS q1,
        PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY amount) AS q3
    FROM transactions
)
SELECT t.*
FROM transactions t, stats s
WHERE t.amount < (s.q1 - 1.5 * (s.q3 - s.q1))
   OR t.amount > (s.q3 + 1.5 * (s.q3 - s.q1));

-- Detect outliers using Z-score (values beyond 3 standard deviations)
WITH stats AS (
    SELECT 
        AVG(amount) AS mean_val,
        STDDEV(amount) AS std_val
    FROM transactions
)
SELECT t.*
FROM transactions t, stats s
WHERE ABS(t.amount - s.mean_val) > 3 * s.std_val;
        """,
        language="sql"
    )

    st.subheader("Handle Outliers")

    st.code(
        """
-- Option 1: Remove outliers (DELETE)
WITH stats AS (
    SELECT 
        PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY amount) AS q1,
        PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY amount) AS q3
    FROM transactions
)
DELETE t
FROM transactions t, stats s
WHERE t.amount < (s.q1 - 1.5 * (s.q3 - s.q1))
   OR t.amount > (s.q3 + 1.5 * (s.q3 - s.q1));

-- Option 2: Cap outliers (Winsorizing)
WITH bounds AS (
    SELECT 
        PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY amount) AS q1,
        PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY amount) AS q3
    FROM transactions
)
UPDATE transactions t
SET amount = CASE 
    WHEN amount < (q1 - 1.5 * (q3 - q1)) THEN (q1 - 1.5 * (q3 - q1))
    WHEN amount > (q3 + 1.5 * (q3 - q1)) THEN (q3 + 1.5 * (q3 - q1))
    ELSE amount
END
FROM bounds;

-- Option 3: Flag outliers for manual review
ALTER TABLE transactions ADD COLUMN is_outlier BOOLEAN DEFAULT FALSE;

WITH bounds AS (
    SELECT 
        PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY amount) AS q1,
        PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY amount) AS q3
    FROM transactions
)
UPDATE transactions t
SET is_outlier = TRUE
FROM bounds
WHERE t.amount < (q1 - 1.5 * (q3 - q1))
   OR t.amount > (q3 + 1.5 * (q3 - q1));
        """,
        language="sql"
    )

    st.warning(
        "**Reservation:** Outliers may be legitimate (e.g., high-value customers, fraud detection signals). "
        "Never delete outliers until the business team confirms they are errors."
    )

    # SECTION 7: STANDARDIZE / NORMALIZE DATA
    # -------------------------
    st.header("7. Standardize / Normalize Data")

    st.write(
        """
        Scaling is used for machine learning algorithms that rely on distance calculations or gradient descent.
        """
    )

    st.subheader("Min-Max Scaling (Normalization)")

    st.code(
        """
-- Scale values to range [0, 1]
WITH stats AS (
    SELECT 
        MIN(amount) AS min_val,
        MAX(amount) AS max_val
    FROM transactions
)
UPDATE transactions t
SET amount_scaled = (t.amount - s.min_val) / (s.max_val - s.min_val)
FROM stats s;

-- Scale values to custom range [a, b], e.g., [0, 100]
WITH stats AS (
    SELECT 
        MIN(amount) AS min_val,
        MAX(amount) AS max_val
    FROM transactions
)
UPDATE transactions t
SET amount_scaled = a + (t.amount - s.min_val) * (b - a) / (s.max_val - s.min_val)
FROM stats s;
        """,
        language="sql"
    )

    st.subheader("Z-Score Standardization")

    st.code(
        """
-- Standardize to mean = 0, standard deviation = 1
WITH stats AS (
    SELECT 
        AVG(amount) AS mean_val,
        STDDEV(amount) AS std_val
    FROM transactions
)
UPDATE transactions t
SET amount_zscore = (t.amount - s.mean_val) / s.std_val
FROM stats s
WHERE s.std_val > 0;
        """,
        language="sql"
    )

    st.subheader("Robust Scaling (Using Median and IQR)")

    st.code(
        """
-- Robust scaling: less sensitive to outliers
WITH stats AS (
    SELECT 
        PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY amount) AS median_val,
        PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY amount) - 
        PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY amount) AS iqr_val
    FROM transactions
)
UPDATE transactions t
SET amount_robust = (t.amount - s.median_val) / s.iqr_val
FROM stats s
WHERE s.iqr_val > 0;
        """,
        language="sql"
    )

    st.info(
        "**Reservation:** Perform scaling only if required for the model. Do not scale fields like IDs, categorical codes, or binary flags."
    )

    # SECTION 8: CORRECT WRONG DATA
    # -------------------------
    st.header("8. Correct Wrong or Inaccurate Data")

    st.write(
        """
        Data may contain impossible values or errors that need correction.
        """
    )

    st.subheader("Clean Phone Numbers")

    st.code(
        """
-- Remove all non-numeric characters
-- MySQL
UPDATE customers 
SET phone = REGEXP_REPLACE(phone, '[^0-9]', '');

-- PostgreSQL
UPDATE customers 
SET phone = REGEXP_REPLACE(phone, '[^0-9]', '', 'g');

-- Format phone numbers consistently
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

    st.subheader("Remove Impossible Values")

    st.code(
        """
-- Remove records with impossible ages
DELETE FROM employees 
WHERE age < 15 OR age > 90;

-- Remove records with future dates
DELETE FROM sales 
WHERE sale_date > CURRENT_DATE;

-- Remove negative prices
DELETE FROM products 
WHERE price < 0;

-- Flag suspicious values instead of deleting
ALTER TABLE employees ADD COLUMN is_suspicious BOOLEAN DEFAULT FALSE;

UPDATE employees 
SET is_suspicious = TRUE 
WHERE age < 15 OR age > 90;
        """,
        language="sql"
    )

    st.subheader("Fix Email Addresses")

    st.code(
        """
-- Validate email format
SELECT email 
FROM customers 
WHERE email NOT LIKE '%_@__%.__%' 
   OR email LIKE '% %' 
   OR email = '';

-- Fix common email issues
UPDATE customers 
SET email = LOWER(TRIM(email))
WHERE email IS NOT NULL;

-- Remove spaces in emails
UPDATE customers 
SET email = REPLACE(email, ' ', '');
        """,
        language="sql"
    )

    # SECTION 9: JOIN & VALIDATE DATA
    # -------------------------
    st.header("9. Join & Validate Data")

    st.write(
        """
        After cleaning, validate data integrity across related tables.
        """
    )

    st.subheader("Check Foreign Key Consistency")

    st.code(
        """
-- Find orders with missing customers
SELECT o.* 
FROM orders o 
LEFT JOIN customers c ON o.customer_id = c.customer_id 
WHERE c.customer_id IS NULL;

-- Find transactions with invalid product IDs
SELECT t.* 
FROM transactions t 
LEFT JOIN products p ON t.product_id = p.product_id 
WHERE p.product_id IS NULL;

-- Check referential integrity summary
SELECT 
    COUNT(*) AS orphaned_records,
    (SELECT COUNT(*) FROM orders) AS total_orders,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM orders), 2) AS orphaned_percentage
FROM orders o 
LEFT JOIN customers c ON o.customer_id = c.customer_id 
WHERE c.customer_id IS NULL;
        """,
        language="sql"
    )

    st.subheader("Validate Business Rules")

    st.code(
        """
-- Check for negative quantities in orders
SELECT * FROM order_items WHERE quantity < 0;

-- Check for discount exceeding price
SELECT * FROM orders WHERE discount_amount > total_amount;

-- Check for orders without items
SELECT o.order_id 
FROM orders o 
LEFT JOIN order_items oi ON o.order_id = oi.order_id 
WHERE oi.order_id IS NULL;
        """,
        language="sql"
    )

    # SECTION 10: CREATE CLEAN VERSION
    # -------------------------
    st.header("10. Create Clean Version (Best Practice)")

    st.write(
        """
        Never clean directly on production data. Always create a clean copy for analysis.
        """
    )

    st.subheader("Create Clean Table")

    st.code(
        """
-- Create a clean version from raw data
CREATE TABLE customers_clean AS
SELECT * FROM customers_raw;

-- Or use CREATE OR REPLACE (if supported)
CREATE OR REPLACE TABLE customers_clean AS
SELECT * FROM customers_raw;

-- Create a clean table with applied transformations
CREATE TABLE customers_clean AS
SELECT 
    customer_id,
    UPPER(TRIM(first_name)) AS first_name,
    UPPER(TRIM(last_name)) AS last_name,
    LOWER(TRIM(email)) AS email,
    REGEXP_REPLACE(phone, '[^0-9]', '') AS phone,
    COALESCE(occupation, 'Unknown') AS occupation,
    CASE 
        WHEN age BETWEEN 18 AND 100 THEN age 
        ELSE NULL 
    END AS age
FROM customers_raw;
        """,
        language="sql"
    )

    st.subheader("Document Cleaning Steps")

    st.code(
        """
-- Create a metadata table to track cleaning operations
CREATE TABLE cleaning_log (
    table_name VARCHAR(100),
    cleaning_step VARCHAR(255),
    rows_affected INT,
    cleaning_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    notes TEXT
);

-- Log cleaning operations
INSERT INTO cleaning_log (table_name, cleaning_step, rows_affected, notes)
VALUES (
    'customers_clean',
    'Removed duplicates',
    150,
    'Removed duplicate records based on email, kept latest created_at'
);

INSERT INTO cleaning_log (table_name, cleaning_step, rows_affected, notes)
VALUES (
    'customers_clean',
    'Imputed missing occupation',
    45,
    'Replaced NULL occupation with "Unknown"'
);
        """,
        language="sql"
    )

    # SECTION 11: VALIDATE CLEANED DATA
    # -------------------------
    st.header("11. Validate Cleaned Data")

    st.write(
        """
        Verify that cleaning operations produced the expected results.
        """
    )

    st.subheader("Record Counts")

    st.code(
        """
-- Compare row counts
SELECT 
    (SELECT COUNT(*) FROM customers_raw) AS raw_count,
    (SELECT COUNT(*) FROM customers_clean) AS clean_count,
    (SELECT COUNT(*) FROM customers_raw) - (SELECT COUNT(*) FROM customers_clean) AS records_removed;

-- Check for remaining NULLs
SELECT 
    COUNT(*) AS total_rows,
    SUM(CASE WHEN email IS NULL THEN 1 ELSE 0 END) AS email_nulls,
    SUM(CASE WHEN phone IS NULL THEN 1 ELSE 0 END) AS phone_nulls
FROM customers_clean;
        """,
        language="sql"
    )

    st.subheader("Range and Distribution Checks")

    st.code(
        """
-- Check min/max values
SELECT 
    MIN(age) AS min_age,
    MAX(age) AS max_age,
    AVG(age) AS avg_age,
    STDDEV(age) AS std_age
FROM customers_clean;

-- Check value distribution
SELECT 
    gender,
    COUNT(*) AS count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2) AS percentage
FROM customers_clean
GROUP BY gender
ORDER BY count DESC;
        """,
        language="sql"
    )

    # SECTION 12: ASSUMPTIONS & RESERVATIONS
    # -------------------------
    st.header(" Important Assumptions & Reservations")

    st.markdown(
        """
        **1. Business Logic Matters**
        
        Data cleaning must match business meaning. For example, deleting a "duplicate" transaction may actually be a legitimate purchase.
        
        **2. Statistical Assumptions**
        
        - Using mean for imputation assumes normally distributed data
        - Using median assumes skewed distribution
        - IQR method assumes symmetric distribution for outlier detection
        
        **3. Data Source Reliability**
        
        Data from surveys, customer input, sensors, and logs usually require different cleaning techniques:
        - **Surveys:** Handle missing responses, inconsistent scales
        - **Customer input:** Validate formats, correct typos
        - **Sensors:** Handle noise, calibration errors
        - **Logs:** Parse unstructured text, handle timezone differences
        
        **4. Regulatory/Compliance Concerns**
        
        Finance, healthcare, aviation industries may forbid deleting records. In these cases:
        - Flag records instead of deleting
        - Maintain audit trails
        - Document all transformations
        
        **5. Dataset Size**
        
        Cleaning strategies differ significantly:
        - **10,000 rows:** Can use complex joins and subqueries
        - **50 million rows:** Need batched updates, indexed columns, partitioned tables
        
        **6. Tool Limitations**
        
        SQL engines differ in functions and performance:
        - **MySQL:** `STR_TO_DATE`, `REGEXP_REPLACE` (limited), no `PERCENTILE_CONT`
        - **PostgreSQL:** `TO_DATE`, full regex support, `PERCENTILE_CONT`
        - **Snowflake:** `TRY_CAST`, `IFF`, `PERCENTILE_CONT`
        - **SQL Server:** `TRY_CONVERT`, `STUFF`, `PERCENTILE_CONT`
        """
    )

    # FULL CHEAT SHEET
    # -------------------------
    st.header(" Full Cheat Sheet - Copy/Paste Format")

    st.code(
        """
-- ============================================
-- A. INITIAL CHECKS
-- ============================================
SELECT * FROM table_name LIMIT 10;                    -- Preview
SELECT COUNT(*) FROM table_name;                      -- Row count
DESCRIBE table_name;                                  -- Data types
SELECT COUNT(*) - COUNT(column_name) FROM table_name; -- NULL count

-- ============================================
-- B. REMOVE DUPLICATES
-- ============================================
WITH ranked AS (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY key_col ORDER BY date_col DESC) AS rn
    FROM table_name
)
DELETE FROM table_name WHERE (key_col) IN (SELECT key_col FROM ranked WHERE rn > 1);

-- ============================================
-- C. FIX STRUCTURAL ERRORS
-- ============================================
UPDATE table_name SET column = UPPER(column);                         -- Capitalization
UPDATE table_name SET column = TRIM(column);                          -- Trim spaces
UPDATE table_name SET phone = REGEXP_REPLACE(phone, '[^0-9]', '');    -- Clean phone

-- ============================================
-- D. TYPE CONVERSION
-- ============================================
-- VARCHAR to DATE (MySQL)
UPDATE table_name SET date_col = STR_TO_DATE(date_str, '%Y-%m-%d');

-- VARCHAR to DECIMAL
UPDATE table_name SET amount = CAST(REPLACE(price, '$', '') AS DECIMAL(10,2));

-- ============================================
-- E. HANDLE MISSING DATA
-- ============================================
-- Categorical: Label as 'Missing'
UPDATE table_name SET col = 'Missing' WHERE col IS NULL;

-- Numerical: Replace with median
WITH median AS (
    SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY col) AS med
    FROM table_name WHERE col IS NOT NULL
)
UPDATE table_name SET col = (SELECT med FROM median) WHERE col IS NULL;

-- ============================================
-- F. OUTLIER TREATMENT
-- ============================================
-- Calculate bounds
WITH bounds AS (
    SELECT 
        PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY col) AS q1,
        PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY col) AS q3
    FROM table_name
)
-- Cap outliers
UPDATE table_name SET col = GREATEST(LEAST(col, q3 + 1.5*(q3-q1)), q1 - 1.5*(q3-q1));

-- ============================================
-- G. NORMALIZE / STANDARDIZE
-- ============================================
-- Min-Max (0 to 1)
WITH stats AS (SELECT MIN(col) AS min_val, MAX(col) AS max_val FROM table_name)
UPDATE table_name SET col_scaled = (col - min_val) / (max_val - min_val) FROM stats;

-- Z-score
WITH stats AS (SELECT AVG(col) AS mean_val, STDDEV(col) AS std_val FROM table_name)
UPDATE table_name SET col_zscore = (col - mean_val) / std_val FROM stats;

-- ============================================
-- H. VALIDATE + DOCUMENT
-- ============================================
-- Check distributions
SELECT MIN(col), MAX(col), AVG(col), COUNT(*) FROM table_name;

-- Log cleaning steps
INSERT INTO cleaning_log (table_name, cleaning_step, rows_affected, notes)
VALUES ('table_name', 'Step description', 100, 'Notes about cleaning');

-- Store cleaned version
CREATE TABLE table_name_clean AS SELECT * FROM table_name;
        """,
        language="sql"
    )

    st.success(
        "Mastering data cleaning in SQL is essential for building reliable data pipelines and trustworthy analytics. "
        "Remember: cleaning decisions directly impact business insights, so always document your steps and validate results."
    )