import streamlit as st
import pandas as pd
import openai
import json
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI


# Assuming df is your DataFrame with credit card data
#csv_file_path = 'testdata.csv'

# Read the CSV file into a DataFrame
#df = pd.read_csv(csv_file_path)

def talk_2_ai(df):
    llm = OpenAI(api_token=st.secrets.OPENAI_API_KEY)
    pandas_ai = PandasAI(llm)
    prompt = st.text_area("Enter your prompt:")
    if st.button("Generate"):
        if prompt:
            with st.spinner():
                # spark the run
                pandas_ai.run(df, prompt=prompt,show_code=True)

                #retrive the log
                mylog = pandas_ai.logs
                mylog = mylog[-2]['msg']
                # Remove the "Answer: " part
                mylog = mylog.replace("Answer: ", "")
                # Replace single quotes with double quotes to make it a valid JSON string
                mylog = mylog.replace("'", '"')
                # Parse the JSON string into a JSON object
                my_json = json.loads(mylog)

                if my_json['type'] == 'string':
                    st.write(my_json['value'])
                elif my_json['type'] == 'dataframe':
                    st.dataframe(my_json['value'])
                elif my_json['type'] == 'plot':
                    st.image("./temp_chart.png", caption='', use_column_width=True)

        else:
            st.warning("please enter a prompt")

