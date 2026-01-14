# Data_Science_Daily
Inspired by the idea that consistency compounds, this repository documents my daily journey in applied data science.


🔹 Day 1 – Initial EDA (Clean Dataset)

What I did:
==========================================
Loaded soil nutrition dataset
Checked shape, columns, datatypes
Verified missing values & outliers
-------------------------------------------
Key finding
===========================================
Dataset was already cleaned and preprocessed
No missing values or extreme outliers detected
----------------------------------------------
Learning
==============================================
Realized not all datasets need heavy cleaning
Importance of verifying before assuming



🔹 Day 2 – Climate Dataset Exploration (Messy Data)

What I did:
======================================================
Switched to Mumbai climate dataset
Identified mixed datatypes and invalid values
Faced date parsing and Excel-date issues
------------------------------------------------------
Problems faced
======================================================
Dates stored as strings + Excel serial numbers
Rain column contained values like Tr, -----
TypeErrors during comparisons
------------------------------------------------------
Learning
======================================================
Real-world data is messy
Dates require special handling
Not all missing values are explicit NaNs



🔹 Day 3 – Data Cleaning & Type Fixing

What I did:
======================================================
Converted date column properly
Used errors='coerce' for numeric conversion
Identified large number of missing rainfall values
Checked duplicates
------------------------------------------------------
Problems faced
======================================================
Unexpected NaNs after coercion
Confusion about why values disappeared
-------------------------------------------------------
Learning
=======================================================
errors='coerce' turns invalid strings into NaN
Cleaning reveals hidden data quality issues
Missing ≠ wrong, sometimes it’s reality




🔹 Day 4 – Distribution, Outliers & Relationships

What you did:
========================================================
Visualized rainfall and temperature distributions
Analyzed skewness and outliers
Studied Temp Min vs Temp Max relationship
--------------------------------------------------------
Key insights
========================================================
Rainfall is highly right-skewed (monsoon-driven)
Temperature follows near-normal distribution
Strong positive correlation between min & max temp
---------------------------------------------------------
Learning
=========================================================
Outliers can represent real-world events
Visualization without interpretation is incomplete
Climate data reflects geographical patterns
