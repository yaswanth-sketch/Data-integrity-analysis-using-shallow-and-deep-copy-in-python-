# 📄 README.md

## 📌 Project Title

Data Corruption Detection and Risk Analysis using Python

## 📖 Description

This project simulates a data replication system where incorrect copying can lead to hidden data corruption.
It uses Python, NumPy, and Pandas to analyze the data and predict system risk based on calculated metrics.

## 🎯 Objective

* To understand shallow copy and deep copy in Python
* To detect hidden corruption in nested data structures
* To analyze data using NumPy and Pandas
* To predict system risk using mathematical functions

## ⚙️ Technologies Used

* Python
* NumPy
* Pandas
* Random Module
* Math Module

## 🧩 Data Structure Used

The data is stored in nested format:

{
"zone": int,
"metrics": {
"traffic": int,
"pollution": int,
"energy": int
},
"history": [values]
}

## 🔄 Steps Involved

### 1. Data Generation

* Generated 15 zones with random values
* Stored using list, dictionary, and list

### 2. Personalization Rule

* If roll number is EVEN → dataset reversed
* If ODD → dataset rotated by 3

### 3. Copy Mechanism

* Assignment Copy
* Shallow Copy
* Deep Copy

### 4. Mutation

* Modified nested values
* Added new history values
* Calculated risk using logarithmic function

### 5. Data Analysis

* Converted data into Pandas DataFrame
* Calculated mean and variance
* Computed correlation manually using NumPy
* Detected anomalies (value > mean + standard deviation)

### 6. Advanced Detection

* Hidden Corruption Detection
* Predictive Risk Analysis
* Cluster Detection
* Stability Index Calculation

## ⚠️ Hidden Corruption Explanation

Shallow copy only copies the outer structure but shares inner objects like dictionaries and lists.
So, when nested data is modified in the shallow copy, the original data also gets affected.

## 📊 Output

The program displays:

* Original Data (Before Mutation)
* Data After Shallow Copy Mutation
* Original Data After Mutation (Corruption Proof)
* Pandas DataFrame
* Anomaly Zones
* Correlation Value
* Final Tuple → (max_risk, min_risk, stability_index)
* Clustered Risk Zones
* Final System Decision

## 📌 Sample Decision Output

* System Stable
* Moderate Risk
* High Corruption Risk
* Critical Failure

## 🧠 Key Concepts Used

* Lists, Tuples, Sets
* Dictionaries
* Functions
* NumPy (vector operations)
* Pandas (data analysis)
* Math functions (log)
* Shallow vs Deep Copy
* Conditional statements

## 🚀 Conclusion

This project demonstrates how improper copying techniques can lead to hidden data corruption.
It also shows how data science methods can be used to detect risks and improve system reliability.
