import streamlit as st
import pandas as pd
import json

class JSONFileUploader:
    def __init__(self):
        self.json_data = None
        self.dataframe = None

    def upload_json_file(self):
        """Uploads a JSON file and converts it into a dictionary."""
        uploaded_file = st.file_uploader("Upload a JSON file", type=['json'])
        if uploaded_file is not None:
            # To read file as string:
            string_data = uploaded_file.getvalue().decode('utf-8')
            # To convert string to json
            self.json_data = json.loads(string_data)
            st.success("JSON file uploaded successfully!")
        else:
            st.error("Please upload a JSON file.")

    def get_json_data(self):
        """Returns the JSON data if it's been uploaded."""
        if self.json_data is not None:
            return self.json_data

    def display_dataframe(self):
        """Converts JSON data to a DataFrame and displays it in Streamlit."""
        if self.json_data is not None:
            # Convert the JSON object to a pandas DataFrame
            self.dataframe = pd.DataFrame([
                {"Column": key, "Transformation": str(value)}
                for key, value in self.json_data.items()
            ])
            # Display the DataFrame in Streamlit
            st.dataframe(self.dataframe)

    def get_dataframe(self):
        """Get method for converted JSON data to a DataFrame."""
        if self.json_data is not None:
            # Convert the JSON object to a pandas DataFrame
            self.dataframe = pd.DataFrame([
                {"Column": key, "Transformation": value}
                for key, value in self.json_data.items()
            ])
        return self.dataframe