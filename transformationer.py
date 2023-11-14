import pandas as pd
import json
import streamlit as st

class DataTransformer:
    def __init__(self, parquet_data, json_rules):
        self.parquet_data_df = parquet_data
        self.transformation_rules_df = json_rules

    def apply_transformations(self):
        try:
            for index, rule in self.transformation_rules_df.iterrows():
                column = rule["Column"]
                transformation = rule["Transformation"]
                if column in self.parquet_data_df.columns:
                    for operation, params in transformation.items():
                        if operation == 'astype':
                            self.parquet_data_df[column] = self.parquet_data_df[column].replace(r'[^\d.]', '', regex=True).astype(params)
                        elif operation == 'map':
                            self.parquet_data_df[column] = self.parquet_data_df[column].map(params)
                        elif operation == 'to_datetime':
                            self.parquet_data_df[column] = pd.to_datetime(self.parquet_data_df[column], format=params['format'])
                        else:
                            print(f"Unsupported operation: {operation}")

            # Replace spaces with underscores in column names
            self.parquet_data_df.columns = [col.replace(' ', '_') for col in self.parquet_data_df.columns]
            # Print success message
            st.success("Transformations applied successfully!")
            
        except Exception as e:
            st.error(f"An error occurred while applying transformations: {e}")

    def get_transformed_dataframe(self):

        return self.parquet_data_df
