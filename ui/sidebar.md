# Snowflake Data Ingestion Tool 

The Snowflake data ingestion tool offers features for uploading data, cleansing data, ingesting data, and AI-driven data analytics, all designed to enhance productivity.

## Instruction to Use

1. Upload Dataset
    - Only accept Parquet file format
    - Max file size is 200GB

2. Upload Transformation Rule 
    - Only accept JSON file format

3. Data Transformation
    - Both the Parquet file and the data transformation rules must be uploaded prior to initiating the transformation process

4. Download Feature
    - After the data has been transformed, it is available for download in CSV file format

5. Data Ingestion 
    - To ingest data, you have the option to create a new table by specifying a table name.
    - Alternatively, you can ingest data into an existing table by providing its name.

6. AI Data Analytics
    - The AI can be prompted to perform quick analyses, such as generating a graph or answering questions based on the dataset.


    - Sample Prompt 1: Provide summarized insights from the data
    - Sample Prompt 2: Graph scatter plot between credit limit and account open date
    - Sample Prompt 3: Graph distribution of the credit card brand