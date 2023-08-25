# ETL Project: Web Scraping, Excel Handling, and PostgreSQL Loading

This project focuses on extracting data from the Jumia website using Beautiful Soup, storing it in an Excel file with Pandas, and then transferring the data to a PostgreSQL database using SQLAlchemy and Pandas. The aim of this ETL (Extract, Transform, Load) project is to automate the process of collecting, storing, and organizing data from a website into a structured database.

## Table of Contents

1. [Introduction](#introduction)
2. [Project Overview](#project-overview)
3. [Tools Used](#tools-used)
4. [Project Steps](#project-steps)
    - [Step 1: Web Scraping](#step-1-web-scraping)
    - [Step 2: Excel File Creation](#step-2-excel-file-creation)
    - [Step 3: Data Extraction from Excel](#step-3-data-extraction-from-excel)
    - [Step 4: PostgreSQL Database Loading](#step-4-postgresql-database-loading)
5. [Configuration](#configuration)
6. [Readme](#readme)
7. [Contacts](#contacts)

## Introduction

This project involves creating an automated pipeline to collect product data from the Jumia website, store it in an Excel file, and then transfer it into a `PostgreSQL` database. By utilizing `Python` libraries like `BeautifulSoup`, `Pandas`, and `SQLAlchemy`, the process is streamlined and can be executed with ease.

## Project Overview

#### The WorkFlow
---
![Texte alternatif de l'image](image/etl_jumia.png)
---

1. **Web Scraping:** Utilize Beautiful Soup to extract product data (e.g., name, price, description) from the Jumia website.

2. **Excel File Creation:** Use Pandas to structure the scraped data into a DataFrame and save it as an Excel file for temporary storage.

3. **Data Extraction from Excel:** Retrieve data from the Excel file using Pandas, ensuring data integrity.

4. **PostgreSQL Database Loading:** Leverage SQLAlchemy to connect to a PostgreSQL database. Automatically generate table based on column names and data types. Load the extracted data into the appropriate table.(the table takes the same name of the excel file)

## Tools Used

- Python
- Beautiful Soup: For web scraping.
- Pandas: For data manipulation and Excel handling.
- PostgreSQL: Database management system.
- SQLAlchemy: To interact with the PostgreSQL database.

## Project Steps

### Step 1: Web Scraping

Use `BeautifulSoup` to scrape the desired data from the `Jumia` website [https://www.jumia.ma]. This may include product names, prices, descriptions and img url for each product. In my case I extracted data of xiaomi redmi product (smartphones).

### Step 2: Excel File Creation

Structurize the scraped data using `Pandas` and create an Excel file to store the data temporarily.

### Step 3: Data Extraction from Excel

Retrieve the data from the Excel file using `Pandas`. This step ensures data correctness before loading it into the database.

### Step 4: PostgreSQL Database Loading

Use `SQLAlchemy` API to establish a connection with the `PostgreSQL` database. Automatically generate tables based on column names and inferred data types. Load the extracted and processed data into the appropriate tables.

## Configuration

Ensure you have the necessary credentials and configuration settings :

- PostgreSQL database credentials (username, password, database name).
- Web scraping targets (Jumia website structure).
- Excel file paths for temporary storage.

it's necessary to consult the `Excel2PostgresLoader.py` script and change these parameters

## Readme

### Installation

1. Clone this repository to your local machine using the following command:
 ```bash
pip clone https://github.com/aymane-maghouti/Jumia-data-pipeline.git
```
   
2. Install the required libraries using the following command:
   
```bash
pip install beautifulsoup4 pandas sqlalchemy psycopg2
```

or just navigate to the project folder and run this command

```bash
pip install requirements.txt
```
### Usage

1. **Web Scraping:**

   - Update the web scraping script to match the structure of the Jumia website and the data you want to extract.

2. **Excel File Creation:**

   - Modify the Pandas code to structure the scraped data and save it as an Excel file.

3. **Data Extraction from Excel:**

   - Adapt the Pandas code to read the data from the Excel file and perform any necessary data cleaning.

4. **PostgreSQL Database Loading:**

   - Set up your PostgreSQL database and update the SQLAlchemy connection string in the script.
   - Adjust the code to automatically generate tables based on the column names and data types from the Excel file.

### Configuration

- Update the database credentials and connection details in the appropriate scripts as I mentioned before.

### Run

Execute each step's script in the following order:

1. Web scraping script (JumiaDataScraper.py)
2. PostgreSQL loading script (Excel2PostgresLoader.py)


Ensure that you have the required permissions and access rights for file manipulation and database operations.

This project automates the process of collecting data from a website, storing it temporarily in an Excel file, and eventually transferring it into a `PostgreSQL` database. It showcases the power of `Python` libraries such as `BeautifulSoup`, `Pandas`, and `SQLAlchemy` in creating an end-to-end `ETL pipeline`.

Feel free to customize the content and functionality  according to your specific requirements.

---

## Contacts

<a href="https://www.linkedin.com/in/aymane-maghouti/" target="_blank">Aymane Maghouti</a><br>
