import streamlit as st
import pandas as pd

class FileUploader:
    def __init__(self):
        self.df = None

    # method to upload file
    def upload_file(self, label, file_type):
        uploaded_file = st.file_uploader(label, type=[file_type])
        if uploaded_file is not None:
            st.success("Parquet file uploaded successfully!")
            return uploaded_file
        else: 
            st.error("Please upload a Parquet file.")
        return None

    # method to read file
    def read_parquet(self, uploaded_file):
        try:
            self.df = pd.read_parquet(uploaded_file)
        except Exception as e:
            st.error(f"An error occurred while reading the Parquet file: {e}")
            self.df = None

    # get method for file df
    def get_dataframe(self):
        return self.df

