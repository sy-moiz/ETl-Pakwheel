
<img width="1456" height="736" alt="Gemini_Generated_Image_4b0q814b0q814b0q" src="https://github.com/user-attachments/assets/7ce4d1d3-de99-4eb1-ae41-3e5f7623d22e" />


### **Pakwheels Data Analysis & Web App**

Overview

This project is a complete data pipeline built using Python. It starts by scraping car listing data from the Pakwheels website and ends with a fully interactive Streamlit dashboard. The data goes through cleaning, analysis, visualization, and is finally stored in a database.

It shows end-to-end skills in web scraping, data processing, EDA, visualization, and database integration.


## Main Features

### 1. Web Scraping
Automatically collects:
- Car details  
- Prices  
- Specifications  
- Mileage  
- City & model information  

Scraping is performed using **BeautifulSoup**.

---

### 2. Data Cleaning
- Raw data is first saved as **JSON**  
- Loaded into **Pandas**  
- Cleaned by fixing missing values, formatting, and datatype issues  
- Outliers are removed  
- Converts fields like **price** and **mileage** into numeric columns  

---

### 3. Exploratory Data Analysis (EDA)
Performed detailed analysis including:
- Summary statistics  
- Histograms for price and mileage distribution  
- Scatter plots to show relationships  
- Heatmaps to understand correlations  

---

### 4. Data Storage
- Cleaned data saved as **CSV**  
- Also stored in a **SQL database** using `pyodbc`  

---

### 5. Streamlit Interactive Web App
The interactive Streamlit app provides:
- Histograms  
- Scatter plots  
- Heatmaps  
- Interactive filters  
- Cleaned dataset preview  

This helps users visually understand market trends.

---

## Technologies Used
- **Python**  
- **BeautifulSoup**  
- **Pandas**, **NumPy**  
- **Matplotlib**, **Seaborn**  
- **Streamlit**  
- **SQL Database + pyodbc**  
- **JSON** & **CSV** formats


